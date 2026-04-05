// ─── Types ──────────────────────────────────────────────────────────────────

export type ValidationResultType = "success" | "warning" | "error" | null;

export interface ValidationResult {
  type: ValidationResultType;
  message: string | null;
}

export interface FormField {
  id: string;
  label?: string;
  placeholder?: string;
  hint?: string;
  type: "string" | "number" | "boolean" | "enum" | "date";
  required?: boolean;
  options?: string[];
  eligibility_key?: string;
}

export interface FormStep {
  step_id: string;
  step_label?: string;
  fields: FormField[];
}

export interface EligibilityRules {
  allowed_categories?: string[] | null;
  max_annual_income?: number | null;
  course_levels?: string[] | null;
  min_disability_percentage?: number | null;
  required_disability_types?: string[] | null;
  max_age?: number | null;
  min_age?: number | null;
  income_field?: string | null;
  category_field?: string | null;
  age_field?: string | null;
  disability_field?: string | null;
  disability_type_field?: string | null;
}

export interface SchemeFormSchema {
  scheme_id: string;
  scheme_name: string;
  eligibility_rules?: EligibilityRules;
  form_steps: FormStep[];
}

export interface UserProfile {
  age?: string;
  income?: string;
  category?: string;
  gender?: string;
  educationLevel?: string;
}

// ─── Engine ─────────────────────────────────────────────────────────────────

export class FormEngine {
  private schema: SchemeFormSchema;
  private responses: Record<string, any> = {};
  private flatFields: FormField[] = [];
  private userProfile: UserProfile | null;

  constructor(schema: SchemeFormSchema, userProfile?: UserProfile) {
    this.schema = schema;
    this.userProfile = userProfile ?? null;
    this.flattenFields();
  }

  private flattenFields() {
    for (const step of this.schema.form_steps) {
      for (const field of step.fields) {
        this.flatFields.push(field);
      }
    }
  }

  // ── Helpers ───────────────────────────────────────────────────────────────

  private parseValue(fieldId: string, value: any) {
    const field = this.flatFields.find((f) => f.id === fieldId);
    if (!field) return value;
    switch (field.type) {
      case "number":
        return Number(value);
      case "boolean":
        return ["yes", "true", "1"].includes(String(value).toLowerCase());
      case "enum":
        return String(value).toLowerCase();
      default:
        return value;
    }
  }

  getField(fieldId: string): FormField | undefined {
    return this.flatFields.find((f) => f.id === fieldId);
  }

  answer(fieldId: string, value: any) {
    this.responses[fieldId] = this.parseValue(fieldId, value);
  }

  getResponses() {
    return this.responses;
  }

  isComplete(): boolean {
    return this.flatFields.every(
      (field) => !field.required || this.responses[field.id] !== undefined
    );
  }

  // ── Core Format Validation ────────────────────────────────────────────────

  validateFormat(fieldId: string, value: any): ValidationResult {
    const field = this.flatFields.find((f) => f.id === fieldId);
    if (!field) return { type: null, message: null };

    const isEmpty =
      value === undefined || value === null || String(value).trim() === "";

    if (isEmpty) {
      if (field.required) {
        return { type: "error", message: "This field is required." };
      }
      return { type: null, message: null };
    }

    // Number type
    if (field.type === "number") {
      if (isNaN(Number(value)) || String(value).trim() === "") {
        return { type: "error", message: "Please enter a valid number." };
      }
      if (Number(value) < 0) {
        return { type: "error", message: "Value cannot be negative." };
      }
    }

    // Boolean type
    if (field.type === "boolean") {
      if (!["yes", "no", "true", "false"].includes(String(value).toLowerCase())) {
        return { type: "error", message: "Please select Yes or No." };
      }
    }

    // Enum type
    if (field.type === "enum") {
      const normalized = String(value).toLowerCase();
      if (!field.options?.includes(normalized)) {
        const readable = field.options?.map((o) => o.replace(/_/g, " ")).join(", ");
        return { type: "error", message: `Please choose one of: ${readable}` };
      }
    }

    // Date type — basic check
    if (field.type === "date") {
      const d = new Date(value);
      if (isNaN(d.getTime())) {
        return { type: "error", message: "Please enter a valid date." };
      }
    }

    // Specific field patterns
    if (fieldId === "aadhaar_number" && !/^\d{12}$/.test(value)) {
      return { type: "error", message: "Aadhaar must be exactly 12 digits." };
    }

    if (fieldId === "bank_account_number" && !/^\d{9,18}$/.test(value)) {
      return {
        type: "error",
        message: "Bank account number must be 9 to 18 digits.",
      };
    }

    if (fieldId === "bank_ifsc" && !/^[A-Z]{4}0[A-Z0-9]{6}$/i.test(value)) {
      return {
        type: "error",
        message: "Invalid IFSC code. Example: SBIN0001234",
      };
    }

    if (fieldId === "mobile_number" && !/^[6-9]\d{9}$/.test(value)) {
      return {
        type: "error",
        message: "Enter a valid 10-digit Indian mobile number.",
      };
    }

    if (fieldId === "email" && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
      return {
        type: "error",
        message: "Enter a valid email address (e.g. name@example.com).",
      };
    }

    return { type: "success", message: "Looks good!" };
  }

  // ── Eligibility Validation ────────────────────────────────────────────────

  validateEligibility(fieldId: string, value: any): ValidationResult {
    const rules = this.schema.eligibility_rules;
    if (!rules) return { type: null, message: null };

    const strVal = String(value).toLowerCase().trim();

    // Category check
    if (
      fieldId === (rules.category_field ?? "category") &&
      rules.allowed_categories &&
      rules.allowed_categories.length > 0
    ) {
      if (!rules.allowed_categories.includes(strVal)) {
        const readable = rules.allowed_categories
          .map((c) => c.toUpperCase())
          .join(", ");
        return {
          type: "warning",
          message: `⚠️ This scheme is only for ${readable} applicants. Your selected category may not qualify.`,
        };
      }
      return {
        type: "success",
        message: `✅ Your category (${strVal.toUpperCase()}) is eligible for this scheme.`,
      };
    }

    // Income check
    if (
      fieldId === (rules.income_field ?? "annual_income") &&
      rules.max_annual_income != null
    ) {
      const income = Number(value);
      if (!isNaN(income)) {
        if (income > rules.max_annual_income) {
          return {
            type: "warning",
            message: `⚠️ Your annual income (₹${income.toLocaleString("en-IN")}) exceeds the eligibility limit of ₹${rules.max_annual_income.toLocaleString("en-IN")}. You may not qualify.`,
          };
        }
        return {
          type: "success",
          message: `✅ Income is within the eligibility limit (max ₹${rules.max_annual_income.toLocaleString("en-IN")}).`,
        };
      }
    }

    // Course level check
    if (fieldId === "course_level" && rules.course_levels) {
      if (!rules.course_levels.includes(strVal)) {
        const readable = rules.course_levels.map((c) => c.toUpperCase()).join(", ");
        return {
          type: "warning",
          message: `⚠️ Only ${readable} courses are eligible. Your course level may not qualify.`,
        };
      }
      return {
        type: "success",
        message: `✅ Course level (${strVal.toUpperCase()}) is eligible.`,
      };
    }

    // Disability percentage check
    if (
      fieldId === (rules.disability_field ?? "disability_percentage") &&
      rules.min_disability_percentage != null
    ) {
      const pct = Number(value);
      if (!isNaN(pct)) {
        if (pct < rules.min_disability_percentage) {
          return {
            type: "warning",
            message: `⚠️ Disability must be at least ${rules.min_disability_percentage}% to qualify. Entered: ${pct}%.`,
          };
        }
        if (pct > 100) {
          return {
            type: "error",
            message: "Disability percentage cannot exceed 100%.",
          };
        }
        return {
          type: "success",
          message: `✅ Disability percentage (${pct}%) meets the minimum requirement of ${rules.min_disability_percentage}%.`,
        };
      }
    }

    // Disability type check
    if (
      fieldId === (rules.disability_type_field ?? "disability_type") &&
      rules.required_disability_types
    ) {
      if (!rules.required_disability_types.includes(strVal)) {
        const readable = rules.required_disability_types
          .map((t) => t.replace(/_/g, " "))
          .join(", ");
        return {
          type: "warning",
          message: `⚠️ This scheme is specifically for: ${readable}.`,
        };
      }
      return {
        type: "success",
        message: `✅ Disability type matches the scheme's requirement.`,
      };
    }

    // Age checks
    if (fieldId === (rules.age_field ?? "age")) {
      const age = Number(value);
      if (!isNaN(age)) {
        if (rules.min_age != null && age < rules.min_age) {
          return {
            type: "warning",
            message: `⚠️ Minimum age required is ${rules.min_age} years. Entered: ${age}.`,
          };
        }
        if (rules.max_age != null && age > rules.max_age) {
          return {
            type: "warning",
            message: `⚠️ Maximum age allowed is ${rules.max_age} years. Entered: ${age}.`,
          };
        }
      }
    }

    return { type: null, message: null };
  }

  // ── Combined Validation ───────────────────────────────────────────────────

  /**
   * Returns the most relevant validation result for a field:
   * eligibility-aware warnings take priority, then format errors,
   * then profile consistency hints.
   */
  validate(fieldId: string, value: any): ValidationResult {
    // 1. Format validation first (errors block eligibility checks)
    const formatResult = this.validateFormat(fieldId, value);
    if (formatResult.type === "error") return formatResult;

    // 2. If value is empty and field is not required → no feedback
    const isEmpty =
      value === undefined || value === null || String(value).trim() === "";
    if (isEmpty) return { type: null, message: null };

    // 3. Eligibility check (scheme rules)
    const eligResult = this.validateEligibility(fieldId, value);
    if (eligResult.type !== null) return eligResult;

    // 4. Profile consistency hints
    if (this.userProfile) {
      const profileHint = this.checkProfileConsistency(fieldId, value);
      if (profileHint) return profileHint;
    }

    // 5. Format was success
    return formatResult;
  }

  private checkProfileConsistency(
    fieldId: string,
    value: any
  ): ValidationResult | null {
    if (!this.userProfile) return null;

    if (fieldId === "gender" && this.userProfile.gender) {
      const entered = String(value).toLowerCase();
      const stored = this.userProfile.gender.toLowerCase();
      if (entered !== stored && stored !== "") {
        return {
          type: "warning",
          message: `ℹ️ Your profile has gender set to "${this.userProfile.gender}". Please verify this is correct.`,
        };
      }
    }

    if (fieldId === "annual_income" && this.userProfile.income) {
      const storedIncome = Number(this.userProfile.income);
      const enteredIncome = Number(value);
      if (!isNaN(storedIncome) && !isNaN(enteredIncome) && storedIncome > 0) {
        const diff = Math.abs(enteredIncome - storedIncome) / storedIncome;
        if (diff > 0.3) {
          return {
            type: "warning",
            message: `ℹ️ This differs significantly from your profile income (₹${storedIncome.toLocaleString("en-IN")}). Ensure you are entering the correct figure.`,
          };
        }
      }
    }

    return null;
  }

  // ── Eligibility Summary ───────────────────────────────────────────────────

  /**
   * Returns a summary of all eligibility rule checks based on
   * currently entered responses, for display in the summary panel.
   */
  getEligibilitySummary(): Array<{
    rule: string;
    status: "pass" | "fail" | "warn" | "pending";
    message: string;
  }> {
    const rules = this.schema.eligibility_rules;
    if (!rules) return [];

    const summary: Array<{
      rule: string;
      status: "pass" | "fail" | "warn" | "pending";
      message: string;
    }> = [];

    // Category rule
    if (rules.allowed_categories && rules.allowed_categories.length > 0) {
      const catField = rules.category_field ?? "category";
      const catVal = this.responses[catField];
      if (!catVal) {
        summary.push({
          rule: "Social Category",
          status: "pending",
          message: "Not yet entered",
        });
      } else if (rules.allowed_categories.includes(String(catVal).toLowerCase())) {
        summary.push({
          rule: "Social Category",
          status: "pass",
          message: `${String(catVal).toUpperCase()} is eligible`,
        });
      } else {
        summary.push({
          rule: "Social Category",
          status: "fail",
          message: `${String(catVal).toUpperCase()} is not in allowed categories (${rules.allowed_categories.map((c) => c.toUpperCase()).join(", ")})`,
        });
      }
    }

    // Income rule
    if (rules.max_annual_income != null) {
      const incomeField = rules.income_field ?? "annual_income";
      const incomeVal = this.responses[incomeField];
      if (incomeVal == null) {
        summary.push({
          rule: "Annual Income",
          status: "pending",
          message: "Not yet entered",
        });
      } else if (Number(incomeVal) <= rules.max_annual_income) {
        summary.push({
          rule: "Annual Income",
          status: "pass",
          message: `₹${Number(incomeVal).toLocaleString("en-IN")} is within limit (max ₹${rules.max_annual_income.toLocaleString("en-IN")})`,
        });
      } else {
        summary.push({
          rule: "Annual Income",
          status: "fail",
          message: `₹${Number(incomeVal).toLocaleString("en-IN")} exceeds limit of ₹${rules.max_annual_income.toLocaleString("en-IN")}`,
        });
      }
    }

    // Disability percentage rule
    if (rules.min_disability_percentage != null) {
      const dpField = rules.disability_field ?? "disability_percentage";
      const dpVal = this.responses[dpField];
      if (dpVal == null) {
        summary.push({
          rule: "Disability Percentage",
          status: "pending",
          message: "Not yet entered",
        });
      } else if (Number(dpVal) >= rules.min_disability_percentage) {
        summary.push({
          rule: "Disability Percentage",
          status: "pass",
          message: `${dpVal}% meets minimum requirement (${rules.min_disability_percentage}%)`,
        });
      } else {
        summary.push({
          rule: "Disability Percentage",
          status: "fail",
          message: `${dpVal}% is below minimum requirement of ${rules.min_disability_percentage}%`,
        });
      }
    }

    // Disability type rule
    if (rules.required_disability_types && rules.required_disability_types.length > 0) {
      const dtField = rules.disability_type_field ?? "disability_type";
      const dtVal = this.responses[dtField];
      if (!dtVal) {
        summary.push({
          rule: "Disability Type",
          status: "pending",
          message: "Not yet selected",
        });
      } else if (rules.required_disability_types.includes(String(dtVal).toLowerCase())) {
        summary.push({
          rule: "Disability Type",
          status: "pass",
          message: `${String(dtVal).replace(/_/g, " ")} is a qualifying disability type`,
        });
      } else {
        summary.push({
          rule: "Disability Type",
          status: "fail",
          message: `${String(dtVal).replace(/_/g, " ")} is not a qualifying type`,
        });
      }
    }

    // Course level rule
    if (rules.course_levels && rules.course_levels.length > 0) {
      const clVal = this.responses["course_level"];
      if (!clVal) {
        summary.push({
          rule: "Course Level",
          status: "pending",
          message: "Not yet selected",
        });
      } else if (rules.course_levels.includes(String(clVal).toLowerCase())) {
        summary.push({
          rule: "Course Level",
          status: "pass",
          message: `${String(clVal).toUpperCase()} is eligible`,
        });
      } else {
        summary.push({
          rule: "Course Level",
          status: "fail",
          message: `${String(clVal).toUpperCase()} is not in eligible course levels`,
        });
      }
    }

    return summary;
  }

  // ── Progress ──────────────────────────────────────────────────────────────

  getProgress(): { filled: number; total: number; percent: number } {
    const required = this.flatFields.filter((f) => f.required);
    const filled = required.filter(
      (f) =>
        this.responses[f.id] !== undefined &&
        this.responses[f.id] !== null &&
        String(this.responses[f.id]).trim() !== ""
    );
    const percent =
      required.length === 0 ? 100 : Math.round((filled.length / required.length) * 100);
    return { filled: filled.length, total: required.length, percent };
  }

  getAllFields(): FormField[] {
    return this.flatFields;
  }

  getSchema(): SchemeFormSchema {
    return this.schema;
  }
}
import React, { useState, useEffect, useCallback, useRef } from "react";
import { useParams, Link, useNavigate } from "react-router-dom";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import Chatbot from "@/components/chatbot/Chatbot";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { cn } from "@/lib/utils";
import {
  ArrowLeft,
  CheckCircle2,
  XCircle,
  AlertTriangle,
  ClipboardList,
  Sparkles,
  ChevronDown,
  ChevronUp,
  Info,
  Volume2,
  ShieldCheck,
  Languages,
} from "lucide-react";

import { SCHEMES } from "@/ai_agentic/form_schemas/index";
import {
  FormEngine,
  ValidationResult,
  FormField,
  SchemeFormSchema,
} from "@/ai_agentic/agentEngine";

// ─── Helpers ──────────────────────────────────────────────────────────────────

function readableLabel(id: string): string {
  return id
    .split("_")
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(" ");
}

function readableOption(opt: string): string {
  return opt
    .split("_")
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(" ");
}

// ─── Generic Schema Builder ────────────────────────────────────────────────────
// Creates a universal practice form from raw backend scheme data

function buildGenericSchema(schemeData: any): SchemeFormSchema {
  const eligibility = schemeData.eligibility ?? {};
  const fields: FormField[] = [];

  // Determine eligibility rules from the raw scheme
  const eligibilityRules: SchemeFormSchema["eligibility_rules"] = {};

  // Always include personal info fields
  fields.push(
    {
      id: "full_name",
      label: "Full Name (as per Aadhaar)",
      placeholder: "Enter your full name",
      hint: "Must match the name on your Aadhaar card exactly.",
      type: "string",
      required: true,
    },
    {
      id: "aadhaar_number",
      label: "Aadhaar Number",
      placeholder: "Enter 12-digit Aadhaar number",
      hint: "Your 12-digit unique identification number.",
      type: "string",
      required: true,
    },
    {
      id: "date_of_birth",
      label: "Date of Birth",
      placeholder: "",
      hint: "As it appears in your official documents.",
      type: "date",
      required: true,
    },
    {
      id: "gender",
      label: "Gender",
      placeholder: "",
      hint: "Select your gender as registered in official records.",
      type: "enum",
      options: ["male", "female", "other"],
      required: true,
    }
  );

  // Age limit
  const ageLimit = eligibility.age_limit ?? eligibility.age ?? null;
  if (ageLimit) {
    const parsed = String(ageLimit).match(/\d+/);
    if (parsed) {
      eligibilityRules.max_age = parseInt(parsed[0]);
      eligibilityRules.age_field = "age";
    }
    fields.push({
      id: "age",
      label: "Age (in years)",
      placeholder: "e.g. 25",
      hint: `Age eligibility: ${ageLimit}`,
      type: "number",
      required: true,
      eligibility_key: "age",
    });
  }

  // Category
  const categoryKeys = [
    "category", "caste_category", "social_category",
    "target_group", "caste"
  ];
  for (const key of categoryKeys) {
    if (eligibility[key]) {
      fields.push({
        id: "category",
        label: "Social Category",
        placeholder: "",
        hint: `This scheme targets: ${eligibility[key]}`,
        type: "enum",
        options: ["sc", "st", "obc", "general", "ews"],
        required: true,
      });
      break;
    }
  }

  // Income
  const incomeRaw =
    eligibility.family_income_limit ??
    eligibility.annual_income_limit ??
    eligibility.income_limit ??
    eligibility.income ?? null;
  if (incomeRaw) {
    const parsed = String(incomeRaw).replace(/[^0-9]/g, "");
    if (parsed) {
      eligibilityRules.max_annual_income = parseInt(parsed);
      eligibilityRules.income_field = "annual_income";
    }
    fields.push({
      id: "annual_income",
      label: "Annual Family Income (₹)",
      placeholder: "e.g. 150000",
      hint: `Income limit: ${incomeRaw}`,
      type: "number",
      required: true,
      eligibility_key: "max_annual_income",
    });
  }

  // Disability percentage
  const disabilityPct =
    eligibility.disability_percentage ??
    eligibility.minimum_disability_percentage ?? null;
  if (disabilityPct) {
    const parsed = String(disabilityPct).match(/\d+/);
    if (parsed) {
      eligibilityRules.min_disability_percentage = parseInt(parsed[0]);
      eligibilityRules.disability_field = "disability_percentage";
    }
    fields.push({
      id: "disability_percentage",
      label: "Disability Percentage (%)",
      placeholder: "e.g. 50",
      hint: `Minimum disability: ${disabilityPct}`,
      type: "number",
      required: true,
      eligibility_key: "min_disability_percentage",
    });
  }

  // State/residence
  if (schemeData.state && schemeData.state !== "All India") {
    fields.push({
      id: "state",
      label: "State of Residence",
      placeholder: `e.g. ${schemeData.state}`,
      hint: `This scheme is applicable in: ${schemeData.state}`,
      type: "string",
      required: true,
    });
  }

  // Contact info
  fields.push(
    {
      id: "mobile_number",
      label: "Mobile Number",
      placeholder: "10-digit mobile number",
      hint: "Active mobile number for OTP and communication.",
      type: "string",
      required: true,
    },
    {
      id: "email",
      label: "Email Address",
      placeholder: "yourname@example.com",
      hint: "Valid email for correspondence.",
      type: "string",
      required: false,
    },
    {
      id: "permanent_address",
      label: "Permanent Address",
      placeholder: "House No., Street, Village/Town, District, State, PIN",
      hint: "Your permanent residential address as per official records.",
      type: "string",
      required: true,
    }
  );

  // Bank details
  fields.push(
    {
      id: "bank_account_number",
      label: "Bank Account Number",
      placeholder: "Enter your account number (9–18 digits)",
      hint: "Account where benefits will be credited.",
      type: "string",
      required: true,
    },
    {
      id: "bank_ifsc",
      label: "Bank IFSC Code",
      placeholder: "e.g. SBIN0001234",
      hint: "11-character IFSC code from your passbook.",
      type: "string",
      required: true,
    }
  );

  return {
    scheme_id: schemeData.scheme_id,
    scheme_name: schemeData.scheme_name,
    eligibility_rules: eligibilityRules,
    form_steps: [
      {
        step_id: "personal_information",
        step_label: "Personal Information",
        fields: fields.filter((f) =>
          ["full_name", "aadhaar_number", "date_of_birth", "gender", "age", "category", "annual_income", "disability_percentage"].includes(f.id)
        ),
      },
      {
        step_id: "contact_address",
        step_label: "Contact & Address",
        fields: fields.filter((f) =>
          ["state", "mobile_number", "email", "permanent_address"].includes(f.id)
        ),
      },
      {
        step_id: "bank_details",
        step_label: "Bank Details",
        fields: fields.filter((f) =>
          ["bank_account_number", "bank_ifsc"].includes(f.id)
        ),
      },
    ].filter((step) => step.fields.length > 0),
  };
}

// ─── Validation Badge ─────────────────────────────────────────────────────────

const ValidationBadge: React.FC<{ result: ValidationResult }> = ({ result }) => {
  if (!result.type || !result.message) return null;

  const cfg = {
    success: {
      icon: <CheckCircle2 className="w-3.5 h-3.5 shrink-0" />,
      cls: "text-emerald-700 bg-emerald-50 border-emerald-200 dark:text-emerald-400 dark:bg-emerald-950/40 dark:border-emerald-800",
    },
    warning: {
      icon: <AlertTriangle className="w-3.5 h-3.5 shrink-0" />,
      cls: "text-amber-700 bg-amber-50 border-amber-200 dark:text-amber-400 dark:bg-amber-950/40 dark:border-amber-800",
    },
    error: {
      icon: <XCircle className="w-3.5 h-3.5 shrink-0" />,
      cls: "text-red-700 bg-red-50 border-red-200 dark:text-red-400 dark:bg-red-950/40 dark:border-red-800",
    },
  };

  const { icon, cls } = cfg[result.type] ?? cfg.error;

  return (
    <div
      className={cn(
        "flex items-start gap-1.5 mt-1.5 px-2.5 py-1.5 rounded-lg border text-xs font-medium leading-snug transition-all duration-300 animate-in fade-in slide-in-from-top-1",
        cls
      )}
    >
      {icon}
      <span>{result.message}</span>
    </div>
  );
};

// ─── Single Field Renderer ────────────────────────────────────────────────────

interface FieldRendererProps {
  field: FormField;
  value: any;
  onChange: (val: string) => void;
  onBlur: () => void;
  validation: ValidationResult;
  touched: boolean;
}

const FieldRenderer: React.FC<FieldRendererProps> = ({
  field,
  value,
  onChange,
  onBlur,
  validation,
  touched,
}) => {
  const borderCls =
    touched && validation.type === "error"
      ? "border-red-400 focus:ring-red-300"
      : touched && validation.type === "warning"
      ? "border-amber-400 focus:ring-amber-300"
      : touched && validation.type === "success"
      ? "border-emerald-400 focus:ring-emerald-300"
      : "";

  if (field.type === "enum") {
    return (
      <div className="space-y-1.5">
        <select
          id={field.id}
          value={value ?? ""}
          onChange={(e) => onChange(e.target.value)}
          onBlur={onBlur}
          className={cn(
            "w-full rounded-xl border bg-background px-3 py-2.5 text-sm ring-offset-background focus:outline-none focus:ring-2 focus:ring-primary/40 transition-all",
            borderCls
          )}
        >
          <option value="" disabled>
            Select…
          </option>
          {field.options?.map((opt) => (
            <option key={opt} value={opt}>
              {readableOption(opt)}
            </option>
          ))}
        </select>
        {touched && <ValidationBadge result={validation} />}
      </div>
    );
  }

  if (field.type === "boolean") {
    return (
      <div className="space-y-1.5">
        <div className="flex gap-3">
          {[
            { label: "Yes", val: "yes" },
            { label: "No", val: "no" },
          ].map(({ label, val }) => (
            <button
              key={val}
              type="button"
              onClick={() => {
                onChange(val);
                onBlur();
              }}
              className={cn(
                "flex-1 py-2.5 rounded-xl border text-sm font-medium transition-all duration-200",
                value === val
                  ? "bg-primary text-primary-foreground border-primary shadow-sm"
                  : "bg-background hover:bg-muted border-border"
              )}
            >
              {label}
            </button>
          ))}
        </div>
        {touched && <ValidationBadge result={validation} />}
      </div>
    );
  }

  return (
    <div className="space-y-1.5">
      <Input
        id={field.id}
        type={
          field.type === "number"
            ? "number"
            : field.type === "date"
            ? "date"
            : "text"
        }
        value={value ?? ""}
        placeholder={field.placeholder ?? ""}
        onChange={(e) => onChange(e.target.value)}
        onBlur={onBlur}
        className={cn("rounded-xl transition-all", borderCls)}
      />
      {touched && <ValidationBadge result={validation} />}
    </div>
  );
};

// ─── Eligibility Summary Panel ────────────────────────────────────────────────

const EligibilitySummaryPanel: React.FC<{ engine: FormEngine }> = ({
  engine,
}) => {
  const items = engine.getEligibilitySummary();
  if (items.length === 0) return null;

  const statusCfg = {
    pass: {
      icon: <CheckCircle2 className="w-4 h-4 text-emerald-500" />,
      badge:
        "bg-emerald-100 text-emerald-700 dark:bg-emerald-900/40 dark:text-emerald-400",
      label: "Pass",
    },
    fail: {
      icon: <XCircle className="w-4 h-4 text-red-500" />,
      badge:
        "bg-red-100 text-red-700 dark:bg-red-900/40 dark:text-red-400",
      label: "Fail",
    },
    warn: {
      icon: <AlertTriangle className="w-4 h-4 text-amber-500" />,
      badge:
        "bg-amber-100 text-amber-700 dark:bg-amber-900/40 dark:text-amber-400",
      label: "Warning",
    },
    pending: {
      icon: <Info className="w-4 h-4 text-muted-foreground" />,
      badge: "bg-muted text-muted-foreground",
      label: "Pending",
    },
  };

  const passCount = items.filter((i) => i.status === "pass").length;
  const failCount = items.filter((i) => i.status === "fail").length;

  return (
    <div className="rounded-2xl border border-border bg-card p-6 space-y-4">
      <div className="flex items-center gap-2 mb-1">
        <ShieldCheck className="w-5 h-5 text-primary" />
        <h3 className="font-semibold text-foreground">
          Eligibility Assessment
        </h3>
        <div className="ml-auto flex gap-2 text-xs font-medium">
          {passCount > 0 && (
            <span className="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700 dark:bg-emerald-900/40 dark:text-emerald-400">
              {passCount} Passed
            </span>
          )}
          {failCount > 0 && (
            <span className="px-2 py-0.5 rounded-full bg-red-100 text-red-700 dark:bg-red-900/40 dark:text-red-400">
              {failCount} Failed
            </span>
          )}
        </div>
      </div>
      <div className="space-y-2">
        {items.map((item) => {
          const cfg = statusCfg[item.status];
          return (
            <div
              key={item.rule}
              className="flex items-start gap-3 p-3 rounded-xl bg-muted/40 border border-border"
            >
              {cfg.icon}
              <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2 flex-wrap">
                  <span className="text-sm font-medium text-foreground">
                    {item.rule}
                  </span>
                  <span
                    className={cn(
                      "text-xs px-2 py-0.5 rounded-full font-medium",
                      cfg.badge
                    )}
                  >
                    {cfg.label}
                  </span>
                </div>
                <p className="text-xs text-muted-foreground mt-0.5">
                  {item.message}
                </p>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

// ─── Success Screen ───────────────────────────────────────────────────────────

const SuccessScreen: React.FC<{
  schemeName: string;
  schemeId: string;
  responses: Record<string, any>;
  schema: SchemeFormSchema;
}> = ({ schemeName, schemeId, responses, schema }) => (
  <div className="min-h-screen bg-background">
    <Navbar />
    <main className="pt-24 pb-20">
      <div className="container mx-auto px-4 max-w-2xl">
        <div className="rounded-2xl border border-border bg-card p-8 text-center space-y-6">
          <div className="w-20 h-20 rounded-full bg-emerald-500/10 flex items-center justify-center mx-auto ring-4 ring-emerald-500/20">
            <CheckCircle2 className="w-10 h-10 text-emerald-500" />
          </div>

          <div>
            <h1 className="font-display text-2xl font-bold text-foreground mb-2">
              Practice Complete! 🎉
            </h1>
            <p className="text-muted-foreground">
              You've successfully completed the practice form for{" "}
              <strong>{schemeName}</strong>. Your responses have been reviewed
              by the AI validation agent.
            </p>
          </div>

          <div className="text-left rounded-xl border border-border bg-muted/30 divide-y divide-border overflow-hidden">
            {schema.form_steps.map((step) =>
              step.fields.map((field) => {
                const val = responses[field.id];
                if (
                  val === undefined ||
                  val === null ||
                  String(val).trim() === ""
                )
                  return null;
                return (
                  <div key={field.id} className="flex px-4 py-2.5 gap-3">
                    <span className="text-xs text-muted-foreground w-44 shrink-0 pt-0.5">
                      {field.label ?? readableLabel(field.id)}
                    </span>
                    <span className="text-sm font-medium text-foreground break-all">
                      {String(val).replace(/_/g, " ")}
                    </span>
                  </div>
                );
              })
            )}
          </div>

          <div className="flex gap-3 flex-col sm:flex-row">
            <Link to={`/scheme/${schemeId}`} className="flex-1">
              <Button variant="outline" size="lg" className="w-full gap-2">
                <ArrowLeft className="w-4 h-4" />
                Back to Scheme
              </Button>
            </Link>
            <a
              href="#"
              onClick={(e) => {
                e.preventDefault();
                window.location.reload();
              }}
              className="flex-1"
            >
              <Button size="lg" className="w-full gap-2">
                <Sparkles className="w-4 h-4" />
                Practice Again
              </Button>
            </a>
          </div>
        </div>
      </div>
    </main>
    <Footer />
    <Chatbot />
  </div>
);

// ─── Main PracticeForm Component ──────────────────────────────────────────────

const PracticeForm: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  const [schema, setSchema] = useState<SchemeFormSchema | null>(null);
  const [loading, setLoading] = useState(true);

  const [formValues, setFormValues] = useState<Record<string, string>>({});
  const [touched, setTouched] = useState<Record<string, boolean>>({});
  const [validations, setValidations] = useState<
    Record<string, ValidationResult>
  >({});
  const [openSteps, setOpenSteps] = useState<Record<string, boolean>>({});
  const [submitted, setSubmitted] = useState(false);
  const [tick, setTick] = useState(0);

  /* ---------------- VOICE STATES ---------------- */
  const [isPlaying, setIsPlaying] = useState<string | null>(null);
  const [selectedLanguage, setSelectedLanguage] = useState("en");
  const [voices, setVoices] = useState<SpeechSynthesisVoice[]>([]);

  /* ---------------- LOAD VOICES ---------------- */
  useEffect(() => {
    const synth = window.speechSynthesis;

    const loadVoices = () => {
      const voiceList = synth.getVoices();
      setVoices(voiceList);
    };

    loadVoices();

    if (synth.onvoiceschanged !== undefined) {
      synth.onvoiceschanged = loadVoices;
    }
  }, []);

  /* ---------------- VOICE HELPERS ---------------- */

  // Canonical BCP-47 locale per language code
  const LANG_LOCALES: Record<string, string> = {
    en: "en-IN",
    hi: "hi-IN",
    ml: "ml-IN",
  };

  /**
   * Pick the best voice using exact BCP-47 prefix matching.
   * e.g. "hi" matches "hi-IN" but NOT "zh" or "chi".
   */
  const pickVoice = (langCode: string): SpeechSynthesisVoice | undefined => {
    return (
      voices.find((v) => v.lang === `${langCode}-IN`) ||
      voices.find((v) => v.lang.startsWith(`${langCode}-`)) ||
      voices.find((v) => v.lang === langCode)
    );
  };

  /**
   * Translate English text to targetLang via Google Translate free endpoint.
   * Returns original text on any failure so audio still plays.
   */
  const translateText = async (text: string, targetLang: string): Promise<string> => {
    try {
      const res = await fetch(
        `https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=${targetLang}&dt=t&q=${encodeURIComponent(text)}`
      );
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      if (!Array.isArray(data?.[0])) throw new Error("Unexpected response shape");
      return data[0].map((item: any) => item?.[0] ?? "").join("");
    } catch (err) {
      console.error("Translation error:", err);
      return text; // fallback: read English text with target language voice
    }
  };

  /* ---------------- VOICE ASSISTANCE ---------------- */
  const handlePlayInstruction = async (fieldId: string, text: string) => {
    const synth = window.speechSynthesis;

    if (isPlaying === fieldId) {
      synth.cancel();
      setIsPlaying(null);
      return;
    }

    // Translate if needed
    const translatedText =
      selectedLanguage !== "en"
        ? await translateText(text, selectedLanguage)
        : text;

    // Pick voice with exact BCP-47 matching
    const voice = pickVoice(selectedLanguage);
    const locale = LANG_LOCALES[selectedLanguage] ?? "en-IN";

    const utterance = new SpeechSynthesisUtterance(translatedText);
    utterance.lang = voice ? voice.lang : locale; // always set correct locale
    if (voice) utterance.voice = voice;
    utterance.rate = 0.95;
    utterance.pitch = 1;

    utterance.onstart = () => setIsPlaying(fieldId);
    utterance.onend = () => setIsPlaying(null);
    utterance.onerror = () => setIsPlaying(null);

    // Cancel existing speech, then wait a tick before speaking.
    // Without the delay, Chromium can silently drop the new utterance.
    synth.cancel();
    setTimeout(() => synth.speak(utterance), 150);
  };

  const engineRef = useRef<FormEngine | null>(null);

  // ── Load schema: dedicated first, then generate from backend ────────────

  useEffect(() => {
    if (!id) return;

    // 1. Try dedicated schema
    const dedicated = SCHEMES[id] ?? null;
    if (dedicated) {
      setSchema(dedicated);
      engineRef.current = new FormEngine(dedicated);
      if (dedicated.form_steps.length > 0) {
        setOpenSteps({ [dedicated.form_steps[0].step_id]: true });
      }
      setLoading(false);
      return;
    }

    // 2. Fallback: fetch backend scheme and auto-generate form
    fetch(`${import.meta.env.VITE_API_URL}/scheme/${id}`)
      .then((r) => {
        if (!r.ok) throw new Error("not found");
        return r.json();
      })
      .then((data) => {
        const raw = data.scheme ?? data;
        const generated = buildGenericSchema(raw);
        setSchema(generated);
        engineRef.current = new FormEngine(generated);
        if (generated.form_steps.length > 0) {
          setOpenSteps({ [generated.form_steps[0].step_id]: true });
        }
      })
      .catch(() => {
        setSchema(null);
      })
      .finally(() => setLoading(false));
  }, [id]);

  // ── Handlers ─────────────────────────────────────────────────────────────

  const handleChange = useCallback((fieldId: string, val: string) => {
    setFormValues((prev) => ({ ...prev, [fieldId]: val }));
    const engine = engineRef.current;
    if (engine) {
      engine.answer(fieldId, val);
      setValidations((prev) => ({
        ...prev,
        [fieldId]: engine.validate(fieldId, val),
      }));
      setTick((t) => t + 1);
    }
  }, []);

  const handleBlur = useCallback((fieldId: string, val: string) => {
    setTouched((prev) => ({ ...prev, [fieldId]: true }));
    const engine = engineRef.current;
    if (engine) {
      setValidations((prev) => ({
        ...prev,
        [fieldId]: engine.validate(fieldId, val),
      }));
      setTick((t) => t + 1);
    }
  }, []);

  const toggleStep = (stepId: string) => {
    setOpenSteps((prev) => ({ ...prev, [stepId]: !prev[stepId] }));
  };

  const handleSubmit = () => {
    if (!schema || !engineRef.current) return;

    const allTouched: Record<string, boolean> = {};
    const allValidations: Record<string, ValidationResult> = {};
    const engine = engineRef.current;

    for (const step of schema.form_steps) {
      for (const field of step.fields) {
        allTouched[field.id] = true;
        const val = formValues[field.id] ?? "";
        engine.answer(field.id, val);
        allValidations[field.id] = engine.validate(field.id, val);
      }
    }

    setTouched(allTouched);
    setValidations(allValidations);
    setTick((t) => t + 1);

    const allOpen: Record<string, boolean> = {};
    schema.form_steps.forEach((s) => (allOpen[s.step_id] = true));
    setOpenSteps(allOpen);

    const hasErrors = schema.form_steps
      .flatMap((s) => s.fields)
      .some((f) => allValidations[f.id]?.type === "error");

    if (!hasErrors) setSubmitted(true);
  };

  // ── Progress ──────────────────────────────────────────────────────────────

  const progress = engineRef.current?.getProgress() ?? {
    filled: 0,
    total: 0,
    percent: 0,
  };

  // ── Loading ──────────────────────────────────────────────────────────────

  if (loading) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="flex flex-col items-center gap-3 text-muted-foreground">
          <div className="w-8 h-8 border-2 border-primary border-t-transparent rounded-full animate-spin" />
          <p className="text-sm">Loading practice form…</p>
        </div>
      </div>
    );
  }

  // ── No schema ─────────────────────────────────────────────────────────────

  if (!schema) {
    return (
      <div className="min-h-screen bg-background">
        <Navbar />
        <main className="pt-24 pb-20">
          <div className="container mx-auto px-4 max-w-2xl">
            <div className="rounded-2xl border border-border bg-card p-10 text-center space-y-4">
              <div className="w-16 h-16 rounded-full bg-muted flex items-center justify-center mx-auto">
                <ClipboardList className="w-8 h-8 text-muted-foreground" />
              </div>
              <h1 className="font-display text-xl font-bold text-foreground">
                Scheme Not Found
              </h1>
              <p className="text-muted-foreground text-sm max-w-sm mx-auto">
                Could not load the practice form for this scheme. The scheme
                may not exist or the backend is unavailable.
              </p>
              <Button
                variant="outline"
                onClick={() => navigate(-1)}
                className="gap-2"
              >
                <ArrowLeft className="w-4 h-4" />
                Go Back
              </Button>
            </div>
          </div>
        </main>
        <Footer />
        <Chatbot />
      </div>
    );
  }

  // ── Success screen ────────────────────────────────────────────────────────

  if (submitted) {
    return (
      <SuccessScreen
        schemeName={schema.scheme_name}
        schemeId={id!}
        responses={engineRef.current?.getResponses() ?? {}}
        schema={schema}
      />
    );
  }

  // ── Main form ─────────────────────────────────────────────────────────────

  const hasErrors = schema.form_steps
    .flatMap((s) => s.fields)
    .some((f) => touched[f.id] && validations[f.id]?.type === "error");

  return (
    <div className="min-h-screen bg-background">
      <Navbar />

      <main className="pt-24 pb-20">
        <div className="container mx-auto px-4 max-w-3xl">

          {/* Back link */}
          <button
            onClick={() => navigate(-1)}
            className="inline-flex items-center gap-2 text-muted-foreground hover:text-foreground transition-colors mb-6 text-sm"
          >
            <ArrowLeft className="w-4 h-4" />
            Back to Scheme Details
          </button>

          {/* Header card */}
          <div className="rounded-2xl bg-gradient-to-br from-primary/10 via-primary/5 to-background border border-primary/20 p-6 mb-6 relative overflow-hidden">
            <div className="absolute top-0 right-0 w-32 h-32 rounded-full bg-primary/5 -translate-y-8 translate-x-8" />
            <div className="relative">
              <div className="flex items-center justify-between mb-2">
                <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-primary/10 text-primary text-xs font-semibold">
                  <Sparkles className="w-3.5 h-3.5" />
                  AI-Guided Practice Form
                </span>
                <div className="flex items-center gap-2 z-10">
                  <Languages className="w-4 h-4 text-muted-foreground" />
                  <select
                    value={selectedLanguage}
                    onChange={(e) => setSelectedLanguage(e.target.value)}
                    className="border border-border rounded-lg px-2 py-1 text-xs bg-background text-foreground focus:outline-none focus:ring-1 focus:ring-primary"
                  >
                    <option value="en">English Voice</option>
                    <option value="hi">Hindi Voice</option>
                    <option value="ml">Malayalam Voice</option>
                  </select>
                </div>
              </div>
              <h1 className="font-display text-xl md:text-2xl font-bold text-foreground mb-1">
                {schema.scheme_name}
              </h1>
              <p className="text-muted-foreground text-sm">
                Fill in each field. The AI agent validates your inputs against
                the scheme's eligibility rules in real time.
              </p>

              {/* Progress bar */}
              <div className="mt-4">
                <div className="flex justify-between text-xs text-muted-foreground mb-1.5">
                  <span>
                    {progress.filled} / {progress.total} required fields filled
                  </span>
                  <span>{progress.percent}% complete</span>
                </div>
                <div className="w-full h-2 rounded-full bg-muted overflow-hidden">
                  <div
                    className="h-full rounded-full bg-primary transition-all duration-500"
                    style={{ width: `${progress.percent}%` }}
                  />
                </div>
              </div>
            </div>
          </div>

          {/* AI info banner */}
          <div className="flex items-start gap-3 p-4 rounded-xl bg-primary/5 border border-primary/15 mb-6">
            <Sparkles className="w-4 h-4 text-primary shrink-0 mt-0.5" />
            <div className="text-xs text-muted-foreground leading-relaxed">
              <span className="font-semibold text-foreground">
                Agentic AI Validation Active.
              </span>{" "}
              Every field is checked against eligibility rules (income limits,
              category, disability criteria, format rules). Look for{" "}
              <span className="text-emerald-600 font-medium">✅ green</span>,{" "}
              <span className="text-amber-600 font-medium">⚠️ yellow</span>, or{" "}
              <span className="text-red-600 font-medium">❌ red</span>{" "}
              indicators below each field.
            </div>
          </div>

          {/* Form steps */}
          <div className="space-y-4 mb-6">
            {schema.form_steps.map((step, stepIdx) => {
              const isOpen = openSteps[step.step_id] !== false;
              const stepFieldIds = step.fields.map((f) => f.id);
              const stepErrors = stepFieldIds.filter(
                (fid) => touched[fid] && validations[fid]?.type === "error"
              );
              const stepWarnings = stepFieldIds.filter(
                (fid) =>
                  touched[fid] && validations[fid]?.type === "warning"
              );
              const requiredFields = step.fields.filter((f) => f.required);
              const stepPassed = requiredFields.filter(
                (f) => touched[f.id] && validations[f.id]?.type === "success"
              );

              return (
                <div
                  key={step.step_id}
                  className="rounded-2xl border border-border bg-card overflow-hidden"
                >
                  {/* Step header */}
                  <button
                    type="button"
                    onClick={() => toggleStep(step.step_id)}
                    className="w-full flex items-center justify-between p-5 hover:bg-muted/30 transition-colors text-left"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-7 h-7 rounded-full bg-primary/10 flex items-center justify-center text-xs font-bold text-primary shrink-0">
                        {stepIdx + 1}
                      </div>
                      <div>
                        <h2 className="font-semibold text-foreground text-sm">
                          {step.step_label ?? readableLabel(step.step_id)}
                        </h2>
                        <p className="text-xs text-muted-foreground">
                          {step.fields.length} field
                          {step.fields.length !== 1 ? "s" : ""}
                        </p>
                      </div>
                    </div>
                    <div className="flex items-center gap-2">
                      {stepErrors.length > 0 && (
                        <span className="text-xs px-2 py-0.5 rounded-full bg-red-100 text-red-700 dark:bg-red-900/40 dark:text-red-400 font-medium">
                          {stepErrors.length} error
                          {stepErrors.length !== 1 ? "s" : ""}
                        </span>
                      )}
                      {stepWarnings.length > 0 && (
                        <span className="text-xs px-2 py-0.5 rounded-full bg-amber-100 text-amber-700 dark:bg-amber-900/40 dark:text-amber-400 font-medium">
                          {stepWarnings.length} warning
                          {stepWarnings.length !== 1 ? "s" : ""}
                        </span>
                      )}
                      {stepErrors.length === 0 &&
                        requiredFields.length > 0 &&
                        stepPassed.length === requiredFields.length && (
                          <CheckCircle2 className="w-4 h-4 text-emerald-500" />
                        )}
                      {isOpen ? (
                        <ChevronUp className="w-4 h-4 text-muted-foreground" />
                      ) : (
                        <ChevronDown className="w-4 h-4 text-muted-foreground" />
                      )}
                    </div>
                  </button>

                  {/* Step fields */}
                  {isOpen && (
                    <div className="px-5 pb-5 space-y-5 border-t border-border pt-5">
                      {step.fields.map((field) => {
                        const val = formValues[field.id] ?? "";
                        const validation = validations[field.id] ?? {
                          type: null,
                          message: null,
                        };
                        const isTouched = !!touched[field.id];

                        return (
                          <div key={field.id}>
                            <div className="flex items-start justify-between gap-2 mb-1.5">
                              <Label
                                htmlFor={field.id}
                                className="text-sm font-medium leading-snug"
                              >
                                {field.label ?? readableLabel(field.id)}
                                {field.required && (
                                  <span className="text-red-500 ml-0.5">
                                    *
                                  </span>
                                )}
                              </Label>

                              {field.hint && (
                                <button
                                  type="button"
                                  title="Listen to field instructions"
                                  onClick={() => {
                                    const text = (field.label ?? field.id) + ". " + field.hint;
                                    handlePlayInstruction(field.id, text);
                                  }}
                                  className={cn(
                                    "text-muted-foreground hover:text-primary transition-colors shrink-0",
                                    isPlaying === field.id && "text-primary animate-pulse"
                                  )}
                                >
                                  <Volume2 className="w-3.5 h-3.5" />
                                </button>
                              )}
                            </div>

                            {field.hint && (
                              <p className="text-xs text-muted-foreground mb-2 leading-relaxed">
                                {field.hint}
                              </p>
                            )}

                            <FieldRenderer
                              field={field}
                              value={val}
                              onChange={(v) => handleChange(field.id, v)}
                              onBlur={() => handleBlur(field.id, val)}
                              validation={validation}
                              touched={isTouched}
                            />
                          </div>
                        );
                      })}
                    </div>
                  )}
                </div>
              );
            })}
          </div>

          {/* Eligibility Summary */}
          {engineRef.current && tick >= 0 && (
            <div className="mb-6">
              <EligibilitySummaryPanel engine={engineRef.current} />
            </div>
          )}

          {/* Submit */}
          <div className="rounded-2xl border border-border bg-card p-5 flex flex-col sm:flex-row items-start sm:items-center gap-4">
            <div className="flex-1">
              <div className="flex items-center gap-2 mb-0.5">
                <ClipboardList className="w-4 h-4 text-muted-foreground" />
                <span className="text-sm font-medium text-foreground">
                  Ready to complete your practice?
                </span>
              </div>
              <p className="text-xs text-muted-foreground">
                The AI agent will do a final validation pass on all fields.
              </p>
            </div>
            <Button size="lg" className="gap-2 shrink-0" onClick={handleSubmit}>
              <Sparkles className="w-4 h-4" />
              Submit Practice Form
            </Button>
          </div>

          {hasErrors && (
            <div className="mt-4 flex items-center gap-2 p-4 rounded-xl bg-red-50 border border-red-200 dark:bg-red-950/30 dark:border-red-800 text-sm text-red-700 dark:text-red-400 animate-in fade-in slide-in-from-top-1">
              <XCircle className="w-4 h-4 shrink-0" />
              Some fields have errors. Please fix them before submitting.
            </div>
          )}

          {/* Practice-only disclaimer */}
          <div className="mt-6 flex items-start gap-3 p-4 rounded-xl bg-accent/50 border border-border">
            <Info className="w-4 h-4 text-muted-foreground shrink-0 mt-0.5" />
            <div>
              <p className="text-sm font-medium text-foreground">
                This is a practice form only
              </p>
              <p className="text-xs text-muted-foreground mt-0.5">
                Your entries are not submitted anywhere or saved. Use this to
                rehearse before applying on the official government portal.
              </p>
            </div>
          </div>
        </div>
      </main>

      <Footer />
      <Chatbot />
    </div>
  );
};

export default PracticeForm;

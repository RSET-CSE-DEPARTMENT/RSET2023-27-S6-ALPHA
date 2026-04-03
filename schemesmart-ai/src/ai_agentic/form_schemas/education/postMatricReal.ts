export const postMatricReal = {
  scheme_id: "EDU_SCH_002",

  scheme_name: "Post Matric Scholarship for SC/ST Students",

  eligibility_rules: {
    allowed_categories: ["sc", "st"],
    max_annual_income: 250000,
    course_levels: ["ug", "pg"],
    income_field: "annual_income",
    category_field: "category",
    age_field: null,
    disability_field: null,
  },

  form_steps: [
    {
      step_id: "personal_information",
      step_label: "Personal Information",

      fields: [
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
          hint: "Your 12-digit unique identification number issued by UIDAI.",
          type: "string",
          required: true,
        },

        {
          id: "date_of_birth",
          label: "Date of Birth",
          placeholder: "",
          hint: "Enter your date of birth as it appears in official documents.",
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
        },

        {
          id: "category",
          label: "Social Category",
          placeholder: "",
          hint: "This scholarship is exclusively for SC and ST students. Select your caste category.",
          type: "enum",
          options: ["sc", "st", "obc", "general"],
          required: true,
          eligibility_key: "allowed_categories",
        },

        {
          id: "annual_income",
          label: "Annual Family Income (₹)",
          placeholder: "e.g. 150000",
          hint: "Total annual income of your family from all sources. Must be below ₹2,50,000 to qualify.",
          type: "number",
          required: true,
          eligibility_key: "max_annual_income",
        },
      ],
    },

    {
      step_id: "contact_information",
      step_label: "Contact & Address",

      fields: [
        {
          id: "mobile_number",
          label: "Mobile Number",
          placeholder: "10-digit mobile number",
          hint: "An active mobile number for OTP verification.",
          type: "string",
          required: true,
        },

        {
          id: "email",
          label: "Email Address",
          placeholder: "yourname@example.com",
          hint: "A valid email address for correspondence and notifications.",
          type: "string",
          required: true,
        },

        {
          id: "permanent_address",
          label: "Permanent Address",
          placeholder: "House No., Street, Village/Town, District, State, PIN",
          hint: "Your permanent residential address as per official records.",
          type: "string",
          required: true,
        },
      ],
    },

    {
      step_id: "education_details",
      step_label: "Education Details",

      fields: [
        {
          id: "course_level",
          label: "Course Level",
          placeholder: "",
          hint: "Select the level of education you are currently pursuing. Both UG and PG are eligible.",
          type: "enum",
          options: ["ug", "pg"],
          required: true,
          eligibility_key: "course_levels",
        },

        {
          id: "institution_type",
          label: "Institution Type",
          placeholder: "",
          hint: "Select the type of institution where you are enrolled.",
          type: "enum",
          options: ["government", "private", "aided"],
          required: true,
        },

        {
          id: "university_name",
          label: "University / Institution Name",
          placeholder: "e.g. University of Kerala",
          hint: "Enter the full official name of your university or institution.",
          type: "string",
          required: true,
        },
      ],
    },

    {
      step_id: "bank_details",
      step_label: "Bank Details",

      fields: [
        {
          id: "bank_account_number",
          label: "Bank Account Number",
          placeholder: "Enter your account number (9–18 digits)",
          hint: "Enter the bank account number where scholarship amount will be credited.",
          type: "string",
          required: true,
        },

        {
          id: "bank_ifsc",
          label: "Bank IFSC Code",
          placeholder: "e.g. SBIN0001234",
          hint: "11-character IFSC code found on your cheque book or bank passbook.",
          type: "string",
          required: true,
        },
      ],
    },
  ],
};
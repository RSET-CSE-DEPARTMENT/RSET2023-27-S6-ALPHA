export const homesForIntellectuallyImpaired = {
  scheme_id: "HOUSING_001",

  scheme_name: "Homes For Intellectually Impaired Persons",

  eligibility_rules: {
    min_disability_percentage: 40,
    required_disability_types: ["mentally_deficient_child"],
    max_age: null,
    min_age: null,
    allowed_categories: null,
    income_field: null,
    category_field: null,
    age_field: "age",
    disability_field: "disability_percentage",
    disability_type_field: "disability_type",
  },

  form_steps: [
    {
      step_id: "applicant_details",
      step_label: "Applicant (Child) Details",

      fields: [
        {
          id: "child_full_name",
          label: "Child's Full Name",
          placeholder: "Enter the child's full name",
          hint: "Full name of the intellectually impaired child as per birth certificate or Aadhaar.",
          type: "string",
          required: true,
        },

        {
          id: "date_of_birth",
          label: "Date of Birth",
          placeholder: "",
          hint: "Child's date of birth as per official records.",
          type: "date",
          required: true,
        },

        {
          id: "age",
          label: "Age (in years)",
          placeholder: "e.g. 12",
          hint: "Current age of the child in completed years.",
          type: "number",
          required: true,
          eligibility_key: "age",
        },

        {
          id: "gender",
          label: "Gender",
          placeholder: "",
          hint: "Gender of the child as per official documents.",
          type: "enum",
          options: ["male", "female", "other"],
          required: true,
        },
      ],
    },

    {
      step_id: "disability_details",
      step_label: "Disability Details",

      fields: [
        {
          id: "disability_type",
          label: "Type of Disability",
          placeholder: "",
          hint: "This scheme is specifically for mentally deficient (intellectually impaired) children.",
          type: "enum",
          options: ["mentally_deficient_child"],
          required: true,
          eligibility_key: "required_disability_types",
        },

        {
          id: "disability_percentage",
          label: "Disability Percentage (%)",
          placeholder: "e.g. 50",
          hint: "As certified by the medical authority. Must be at least 40% to qualify for this scheme.",
          type: "number",
          required: true,
          eligibility_key: "min_disability_percentage",
        },

        {
          id: "disability_certificate_available",
          label: "Disability Certificate Available",
          placeholder: "",
          hint: "A valid disability certificate issued by a government-recognized medical authority is mandatory.",
          type: "boolean",
          required: true,
        },
      ],
    },

    {
      step_id: "guardian_details",
      step_label: "Guardian / Parent Details",

      fields: [
        {
          id: "guardian_name",
          label: "Guardian's Full Name",
          placeholder: "Enter guardian's name",
          hint: "Full name of the parent or legal guardian of the child.",
          type: "string",
          required: true,
        },

        {
          id: "guardian_mobile",
          label: "Guardian's Mobile Number",
          placeholder: "10-digit mobile number",
          hint: "Active mobile number of the guardian for communication purposes.",
          type: "string",
          required: true,
        },

        {
          id: "guardian_relationship",
          label: "Relationship with Child",
          placeholder: "e.g. Father, Mother, Legal Guardian",
          hint: "Specify the guardian's relationship with the child.",
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
          hint: "Bank account number of the guardian where benefits will be transferred.",
          type: "string",
          required: true,
        },

        {
          id: "bank_ifsc",
          label: "Bank IFSC Code",
          placeholder: "e.g. SBIN0001234",
          hint: "11-character IFSC code found on your cheque book or passbook.",
          type: "string",
          required: true,
        },
      ],
    },
  ],
};
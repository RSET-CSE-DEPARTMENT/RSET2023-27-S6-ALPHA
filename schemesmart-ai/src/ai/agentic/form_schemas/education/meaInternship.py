# src/ai/agentic/form_schemas/employment/meaInternship.py

meaInternship = {
    "scheme_id": "EMP_SCH_009",
    "scheme_name": "MEA Internship Programme",
    "form_steps": [
        {
            "step_id": "personal_information",
            "fields": [
                {"id": "full_name", "type": "string", "required": True},
                {"id": "date_of_birth", "type": "date", "required": True},
                {"id": "age", "type": "number", "required": True},
                {
                    "id": "gender",
                    "type": "enum",
                    "options": ["male", "female", "other"],
                    "required": True,
                },
                {"id": "email", "type": "string", "required": True},
                {"id": "phone_number", "type": "string", "required": True},
                {"id": "aadhaar_number", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "educational_qualification",
            "fields": [
                {"id": "current_status", "type": "enum", "options": ["final_year_student", "graduate"], "required": True},
                {"id": "degree", "type": "string", "required": True},
                {"id": "university_name", "type": "string", "required": True},
                {"id": "cgpa_or_percentage", "type": "number", "required": True},
            ],
        },
        {
            "step_id": "eligibility_confirmation",
            "fields": [
                {"id": "age_limit_met", "type": "boolean", "required": True, "description": "Applicant must be 25 years or below"},
                {"id": "qualification_met", "type": "boolean", "required": True, "description": "Applicant must be a graduate or final-year student"},
            ],
        },
        {
            "step_id": "internship_preferences",
            "fields": [
                {"id": "preferred_department", "type": "string", "required": True},
                {"id": "preferred_duration_months", "type": "number", "required": True, "description": "Select duration between 1–3 months"},
                {"id": "travel_support_required", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "aadhaar_linked", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "documents_upload",
            "fields": [
                {"id": "photograph", "type": "file", "required": True},
                {"id": "signature", "type": "file", "required": True},
                {"id": "aadhaar_card", "type": "file", "required": True},
                {"id": "degree_certificate_or_proof", "type": "file", "required": True},
            ],
        },
        {
            "step_id": "acknowledgements",
            "fields": [
                {"id": "agree_terms", "type": "boolean", "required": True},
                {"id": "signature_applicant", "type": "string", "required": True},
                {"id": "date_of_submission", "type": "date", "required": True},
            ],
        },
    ],
}
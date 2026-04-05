# src/ai/agentic/form_schemas/education/sainikSchoolImphal.py

sainikSchoolImphalScholarship = {
    "scheme_id": "EDU_SCH_010",
    "scheme_name": "Scholarship for Cadets of Sainik School Imphal",
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
                    "required": True
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "residence_state", "type": "enum", "options": ["Mizoram"], "required": True},
            ],
        },
        {
            "step_id": "education_details",
            "fields": [
                {"id": "school_name", "type": "string", "required": True, "default": "Sainik School Imphal"},
                {"id": "class_level", "type": "string", "required": True},
                {"id": "is_cadet", "type": "boolean", "required": True, "description": "Must be a cadet of Sainik School Imphal"},
            ],
        },
        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True, "description": "Must not exceed ₹2.5 lakh per annum"},
                {"id": "bpl_status", "type": "boolean", "required": False},
            ],
        },
        {
            "step_id": "benefits_details",
            "fields": [
                {"id": "tuition_fees", "type": "boolean", "required": True},
                {"id": "boarding_lodging", "type": "boolean", "required": True},
                {"id": "uniform_academic_expenses", "type": "boolean", "required": True},
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
                {"id": "aadhaar_card", "type": "file", "required": True},
                {"id": "income_certificate", "type": "file", "required": True},
                {"id": "school_certificate", "type": "file", "required": True, "description": "Proof of cadet status"},
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
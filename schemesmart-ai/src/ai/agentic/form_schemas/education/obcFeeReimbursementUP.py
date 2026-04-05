# src/ai/agentic/form_schemas/education/obcFeeReimbursementUP.py

obcFeeReimbursementUP = {
    "scheme_id": "EDU_SCH_008",
    "scheme_name": "OBC Fee Reimbursement Scheme (Uttar Pradesh)",
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
                {"id": "aadhaar_number", "type": "string", "required": True},
                {
                    "id": "caste_category",
                    "type": "enum",
                    "options": ["obc"],
                    "required": True,
                },
            ],
        },
        {
            "step_id": "residential_details",
            "fields": [
                {"id": "state", "type": "string", "required": True, "default": "Uttar Pradesh"},
                {"id": "district", "type": "string", "required": True},
                {"id": "address", "type": "string", "required": True},
                {"id": "pincode", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "education_details",
            "fields": [
                {"id": "is_student", "type": "boolean", "required": True},
                {"id": "course_level", "type": "enum", "options": ["ug", "pg", "diploma"], "required": True},
                {"id": "institution_type", "type": "enum", "options": ["government", "private", "aided"], "required": True},
                {"id": "institution_name", "type": "string", "required": True},
                {"id": "admission_status", "type": "enum", "options": ["admitted"], "required": True},
            ],
        },
        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {"id": "income_limit_met", "type": "boolean", "required": True, "description": "Income should not exceed ₹2,00,000 per annum"},
                {"id": "bpl_status", "type": "boolean", "required": False},
            ],
        },
        {
            "step_id": "scholarship_details",
            "fields": [
                {"id": "monthly_scholarship", "type": "number", "required": True, "description": "Monthly stipend, e.g., ₹150"},
                {"id": "annual_grant", "type": "number", "required": True, "description": "Annual grant, e.g., ₹750"},
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
                {"id": "aadhaar_card", "type": "file", "required": True},
                {"id": "income_certificate", "type": "file", "required": True},
                {"id": "admission_certificate", "type": "file", "required": True},
                {"id": "photograph", "type": "file", "required": True},
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
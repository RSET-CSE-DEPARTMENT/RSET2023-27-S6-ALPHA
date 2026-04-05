# src/ai/agentic/form_schemas/women/kanyashreePrakalpa.py

kanyashreePrakalpa = {
    "scheme_id": "EDU_SCH_012",
    "scheme_name": "Kanyashree Prakalpa",
    "form_steps": [
        {
            "step_id": "personal_information",
            "fields": [
                {"id": "full_name", "type": "string", "required": True},
                {"id": "date_of_birth", "type": "date", "required": True},
                {"id": "age", "type": "number", "required": True},
                {"id": "gender", "type": "enum", "options": ["female"], "required": True},
                {"id": "marital_status", "type": "enum", "options": ["unmarried"], "required": True},
                {"id": "residence_state", "type": "enum", "options": ["West Bengal"], "required": True},
                {"id": "aadhaar_number", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "education_details",
            "fields": [
                {"id": "is_student_enrolled", "type": "boolean", "required": True},
                {"id": "institution_name", "type": "string", "required": True},
                {"id": "class_level", "type": "string", "required": True},
                {"id": "program_type", "type": "enum", "options": ["K1", "K2"], "required": True},
            ],
        },
        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {"id": "income_certificate_available", "type": "boolean", "required": False},
            ],
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "account_in_applicant_name", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "documents_upload",
            "fields": [
                {"id": "birth_certificate", "type": "file", "required": True},
                {"id": "unmarried_status_declaration", "type": "file", "required": True},
                {"id": "income_certificate", "type": "file", "required": False},
                {"id": "bank_passbook_copy", "type": "file", "required": True},
                {"id": "disability_certificate", "type": "file", "required": False},
            ],
        },
        {
            "step_id": "acknowledgement",
            "fields": [
                {"id": "agree_terms", "type": "boolean", "required": True},
                {"id": "signature_applicant", "type": "string", "required": True},
                {"id": "date_of_submission", "type": "date", "required": True},
            ],
        },
    ],
}
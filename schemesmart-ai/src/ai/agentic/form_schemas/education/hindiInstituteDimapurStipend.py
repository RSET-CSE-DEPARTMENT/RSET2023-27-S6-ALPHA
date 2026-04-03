# src/ai/agentic/form_schemas/education/hindiInstituteDimapur.py

hindiInstituteDimapurStipend = {
    "scheme_id": "EDU_SCH_011",
    "scheme_name": "Stipend to Students Studying at Govt. Hindi Institute, Dimapur",
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
                {"id": "residence_state", "type": "enum", "options": ["Nagaland"], "required": True},
            ],
        },
        {
            "step_id": "education_details",
            "fields": [
                {"id": "institution_name", "type": "string", "required": True, "default": "Government Hindi Institute, Dimapur"},
                {"id": "course_name", "type": "string", "required": True},
                {"id": "class_level", "type": "string", "required": True},
                {"id": "is_student_enrolled", "type": "boolean", "required": True, "description": "Currently enrolled at the institute"},
            ],
        },
        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {"id": "bpl_status", "type": "boolean", "required": False},
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
                {"id": "residence_proof", "type": "file", "required": True},
                {"id": "family_income_proof", "type": "file", "required": True},
                {"id": "previous_marksheets", "type": "file", "required": True},
                {"id": "admission_proof", "type": "file", "required": True},
                {"id": "bank_passbook", "type": "file", "required": True},
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
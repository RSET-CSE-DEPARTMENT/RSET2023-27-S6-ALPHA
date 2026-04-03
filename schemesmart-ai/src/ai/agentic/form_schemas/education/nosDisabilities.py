# src/ai/agentic/form_schemas/education/nos_disabilities.py

nosDisabilities = {
    "scheme_id": "EDU_SCH_001",
    "scheme_name": "National Overseas Scholarship for Students with Disabilities",
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
                {"id": "voter_id", "type": "string", "required": False},
                {"id": "pan_card", "type": "string", "required": True},
                {"id": "residence_proof", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "disability_details",
            "fields": [
                {
                    "id": "disability_type",
                    "type": "enum",
                    "options": [
                        "visual",
                        "hearing",
                        "speech",
                        "loco-motor",
                        "mental_retardation",
                        "other"
                    ],
                    "required": True,
                },
                {"id": "disability_percentage", "type": "number", "required": True},
                {"id": "disability_certificate_number", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "education_details",
            "fields": [
                {"id": "is_student", "type": "boolean", "required": True},
                {
                    "id": "course_level",
                    "type": "enum",
                    "options": ["masters", "phd"],
                    "required": True,
                },
                {"id": "institution_name", "type": "string", "required": True},
                {
                    "id": "institution_accreditation",
                    "type": "string",
                    "required": True,
                },
                {"id": "admission_offer_letter", "type": "file", "required": True},
                {"id": "details_of_proposed_study", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {"id": "income_certificate", "type": "file", "required": True},
                {"id": "income_tax_returns", "type": "file", "required": False},
            ],
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "aadhaar_linked", "type": "boolean", "required": True},
                {"id": "pan_card_parent_guardian", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "documents_upload",
            "fields": [
                {"id": "application_form", "type": "file", "required": True},
                {"id": "proof_of_birth", "type": "file", "required": True},
                {"id": "disability_certificate", "type": "file", "required": True},
                {"id": "self_declaration_no_other_scholarship", "type": "file", "required": True},
            ],
        },
        {
            "step_id": "acknowledgements",
            "fields": [
                {"id": "agree_terms", "type": "boolean", "required": True},
                {"id": "signature", "type": "string", "required": True},
                {"id": "date_of_submission", "type": "date", "required": True},
            ],
        },
    ],
}
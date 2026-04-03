# src/ai/agentic/form_schemas/education/ugcEmeritus.py

ugcEmeritus = {
    "scheme_id": "EDU_SCH_005",
    "scheme_name": "UGC Emeritus Fellowship",
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
                    "required": False,
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "professional_details",
            "fields": [
                {
                    "id": "target_group",
                    "type": "enum",
                    "options": ["superannuated_teachers"],
                    "required": True,
                },
                {
                    "id": "institution_type",
                    "type": "enum",
                    "options": ["ugc_recognized_institution"],
                    "required": True,
                },
                {"id": "current_affiliation", "type": "string", "required": True},
                {"id": "award_letter", "type": "file", "required": True},
                {"id": "continuation_certificate", "type": "file", "required": True},
            ],
        },
        {
            "step_id": "fellowship_details",
            "fields": [
                {"id": "honorarium", "type": "string", "required": True},
                {"id": "contingency_amount", "type": "string", "required": True},
                {"id": "tenure_years", "type": "number", "required": True},
                {"id": "slots_available", "type": "number", "required": True},
            ],
        },
        {
            "step_id": "application_process",
            "fields": [
                {"id": "mode_online", "type": "boolean", "required": True},
                {"id": "portal_url", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "documents_upload",
            "fields": [
                {"id": "aadhaar_card_file", "type": "file", "required": True},
                {"id": "undertaking_certificate", "type": "file", "required": True},
                {"id": "award_letter_file", "type": "file", "required": True},
                {"id": "continuation_certificate_file", "type": "file", "required": True},
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
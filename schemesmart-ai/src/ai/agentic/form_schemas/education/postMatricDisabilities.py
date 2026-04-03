# src/ai/agentic/form_schemas/education/postMatricDisabilities.py

postMatricDisabilities = {
    "scheme_id": "EDU_SCH_002",
    "scheme_name": "Post-Matric Scholarship for Students with Disabilities",
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
                {
                    "id": "disability_type",
                    "type": "enum",
                    "options": [
                        "visual",
                        "hearing",
                        "speech",
                        "loco-motor",
                        "intellectual",
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
                    "options": [
                        "class_11",
                        "class_12",
                        "iti",
                        "polytechnic_diploma",
                        "bachelor_degree",
                        "bachelor_diploma",
                        "master_degree",
                        "master_diploma"
                    ],
                    "required": True,
                },
                {"id": "institution_name", "type": "string", "required": True},
                {
                    "id": "institution_type",
                    "type": "enum",
                    "options": ["government", "private", "aided"],
                    "required": True,
                },
                {"id": "tuition_fee_receipt", "type": "file", "required": True},
                {"id": "last_academic_qualification_certificate", "type": "file", "required": True},
            ],
        },
        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {"id": "income_certificate", "type": "file", "required": True},
                {"id": "bpl_status", "type": "boolean", "required": False},
            ],
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "aadhaar_linked", "type": "boolean", "required": True},
                {"id": "parent_guardian_bank_account_number", "type": "string", "required": False},
            ],
        },
        {
            "step_id": "documents_upload",
            "fields": [
                {"id": "photograph", "type": "file", "required": True},
                {"id": "proof_of_age", "type": "file", "required": True},
                {"id": "disability_certificate_file", "type": "file", "required": True},
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
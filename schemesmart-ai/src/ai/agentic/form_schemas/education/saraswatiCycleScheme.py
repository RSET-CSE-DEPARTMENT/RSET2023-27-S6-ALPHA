# src/ai/agentic/form_schemas/education/saraswatiCycleScheme.py

saraswatiCycleScheme = {
    "scheme_id": "EDU_SCH_015",
    "scheme_name": "Chhattisgarh Saraswati Cycle Scheme",
    "form_steps": [
        {
            "step_id": "personal_information",
            "fields": [
                {"id": "full_name", "type": "string", "required": True},
                {"id": "father_or_guardian_name", "type": "string", "required": True},
                {"id": "mother_name", "type": "string", "required": False},
                {"id": "date_of_birth", "type": "date", "required": True},
                {"id": "age", "type": "number", "required": True},
                {
                    "id": "gender",
                    "type": "enum",
                    "options": ["female"],
                    "required": True
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "mobile_number", "type": "string", "required": False}
            ],
        },

        {
            "step_id": "residence_details",
            "fields": [
                {
                    "id": "state",
                    "type": "enum",
                    "options": ["Chhattisgarh"],
                    "required": True
                },
                {"id": "district", "type": "string", "required": True},
                {"id": "block_or_tehsil", "type": "string", "required": True},
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "address", "type": "string", "required": True},
                {"id": "pincode", "type": "string", "required": True}
            ],
        },

        {
            "step_id": "education_details",
            "fields": [
                {"id": "is_student", "type": "boolean", "required": True},
                {
                    "id": "current_class",
                    "type": "enum",
                    "options": ["class_9"],
                    "required": True
                },
                {
                    "id": "institution_type",
                    "type": "enum",
                    "options": ["government", "government_aided"],
                    "required": True
                },
                {"id": "school_name", "type": "string", "required": True},
                {"id": "school_district", "type": "string", "required": True},
                {"id": "student_roll_number", "type": "string", "required": True},
                {"id": "student_id", "type": "string", "required": False}
            ],
        },

        {
            "step_id": "eligibility_details",
            "fields": [
                {
                    "id": "caste_category",
                    "type": "enum",
                    "options": ["sc", "st", "bpl"],
                    "required": True
                },
                {"id": "bpl_card_holder", "type": "boolean", "required": True},
                {"id": "family_income_annual", "type": "number", "required": False}
            ],
        },

        {
            "step_id": "bank_details",
            "fields": [
                {"id": "has_bank_account", "type": "boolean", "required": False},
                {"id": "bank_account_number", "type": "string", "required": False},
                {"id": "bank_ifsc", "type": "string", "required": False},
                {"id": "bank_name", "type": "string", "required": False}
            ],
        },

        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "residence_certificate", "type": "file", "required": True},
                {"id": "bpl_card_copy", "type": "file", "required": True},
                {"id": "caste_certificate", "type": "file", "required": True},
                {"id": "school_certificate", "type": "file", "required": True},
                {"id": "aadhaar_copy", "type": "file", "required": True},
                {"id": "student_photograph", "type": "file", "required": False}
            ],
        },

        {
            "step_id": "declaration",
            "fields": [
                {"id": "applicant_declaration", "type": "boolean", "required": True},
                {"id": "place", "type": "string", "required": True},
                {"id": "date_of_application", "type": "date", "required": True},
                {"id": "applicant_signature", "type": "string", "required": True}
            ],
        }
    ]
}
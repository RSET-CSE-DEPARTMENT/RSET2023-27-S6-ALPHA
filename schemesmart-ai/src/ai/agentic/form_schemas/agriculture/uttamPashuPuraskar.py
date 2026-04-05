# src/ai/agentic/form_schemas/agriculture/uttamPashuPuraskar.py

uttamPashuPuraskar = {
    "scheme_id": "AGR_SCH_003",
    "scheme_name": "Uttam Pashu Puraskar Yojana",
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
                {"id": "mobile_number", "type": "string", "required": True},
                {"id": "email", "type": "string", "required": False}
            ]
        },

        {
            "step_id": "address_information",
            "fields": [
                {"id": "state", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "village", "type": "string", "required": True},
                {"id": "pincode", "type": "number", "required": True},
                {"id": "residential_address", "type": "string", "required": True},
                {"id": "is_himachal_resident", "type": "boolean", "required": True}
            ]
        },

        {
            "step_id": "farmer_details",
            "fields": [
                {
                    "id": "livestock_owner",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "livestock_type",
                    "type": "enum",
                    "options": ["cow", "buffalo", "both"],
                    "required": True
                },
                {
                    "id": "number_of_animals_owned",
                    "type": "number",
                    "required": True
                }
            ]
        },

        {
            "step_id": "animal_information",
            "fields": [
                {
                    "id": "animal_1_type",
                    "type": "enum",
                    "options": ["cow", "buffalo"],
                    "required": True
                },
                {"id": "animal_1_tag_number", "type": "string", "required": True},
                {"id": "animal_1_daily_milk_yield_litres", "type": "number", "required": True},

                {
                    "id": "animal_2_type",
                    "type": "enum",
                    "options": ["cow", "buffalo", "none"],
                    "required": False
                },
                {"id": "animal_2_tag_number", "type": "string", "required": False},
                {"id": "animal_2_daily_milk_yield_litres", "type": "number", "required": False}
            ]
        },

        {
            "step_id": "milk_yield_verification",
            "fields": [
                {
                    "id": "milk_recorded_at_veterinary_center",
                    "type": "boolean",
                    "required": True
                },
                {"id": "veterinary_center_name", "type": "string", "required": True},
                {"id": "milk_recording_date", "type": "date", "required": True},
                {
                    "id": "milk_yield_above_15_litres",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_holder_name", "type": "string", "required": True},
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_name", "type": "string", "required": True},
                {"id": "bank_branch", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "aadhaar_linked_bank_account", "type": "boolean", "required": True}
            ]
        },

        {
            "step_id": "social_category",
            "fields": [
                {
                    "id": "caste_category",
                    "type": "enum",
                    "options": ["general", "obc", "sc", "st"],
                    "required": False
                },
                {"id": "bpl_status", "type": "boolean", "required": False}
            ]
        },

        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "upload_identity_proof", "type": "file", "required": True},
                {"id": "upload_residence_proof", "type": "file", "required": True},
                {"id": "upload_bank_passbook", "type": "file", "required": True},
                {"id": "upload_bpl_certificate", "type": "file", "required": False},
                {"id": "upload_caste_certificate", "type": "file", "required": False}
            ]
        },

        {
            "step_id": "declaration",
            "fields": [
                {
                    "id": "information_true",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "agree_terms_conditions",
                    "type": "boolean",
                    "required": True
                }
            ]
        }

    ]
}
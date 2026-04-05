# src/ai/agentic/form_schemas/agriculture/subsidyRIRBirdsUnit.py

subsidyRIRBirdsUnit = {
    "scheme_id": "AGR_SCH_005",
    "scheme_name": "Subsidy Scheme on Establishment of 25 RIR Birds Unit",
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
                {"id": "taluka", "type": "string", "required": True},
                {"id": "village", "type": "string", "required": True},
                {"id": "pincode", "type": "number", "required": True},
                {"id": "residential_address", "type": "string", "required": True},
                {"id": "is_gujarat_resident", "type": "boolean", "required": True}
            ]
        },

        {
            "step_id": "social_category_details",
            "fields": [
                {
                    "id": "caste_category",
                    "type": "enum",
                    "options": ["general", "obc", "sc", "st"],
                    "required": True
                },
                {"id": "is_st_beneficiary", "type": "boolean", "required": True},
                {"id": "bpl_status", "type": "boolean", "required": False},
                {"id": "is_woman_applicant", "type": "boolean", "required": False}
            ]
        },

        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {"id": "income_certificate_available", "type": "boolean", "required": True}
            ]
        },

        {
            "step_id": "poultry_training_details",
            "fields": [
                {
                    "id": "completed_poultry_training",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "training_institute_name",
                    "type": "string",
                    "required": False
                },
                {
                    "id": "training_completion_date",
                    "type": "date",
                    "required": False
                },
                {
                    "id": "training_certificate_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "poultry_unit_details",
            "fields": [
                {
                    "id": "apply_for_rir_25_bird_unit",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "poultry_shed_available",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "previous_poultry_farming_experience",
                    "type": "boolean",
                    "required": False
                },
                {
                    "id": "land_available_for_poultry_unit",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "livestock_support_details",
            "fields": [
                {
                    "id": "willing_for_regular_vaccination",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "nearest_veterinary_center",
                    "type": "string",
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
            "step_id": "document_uploads",
            "fields": [
                {"id": "upload_aadhaar_card", "type": "file", "required": True},
                {"id": "upload_income_certificate", "type": "file", "required": True},
                {"id": "upload_caste_certificate", "type": "file", "required": True},
                {"id": "upload_bank_passbook", "type": "file", "required": True},
                {"id": "upload_training_certificate", "type": "file", "required": True}
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
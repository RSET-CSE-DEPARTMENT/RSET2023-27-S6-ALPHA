krishakBakriPalan = {
    "scheme_id": "AGR_SCH_001",
    "scheme_name": "Krishak Bakri Palan Yojna",
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
                {"id": "mobile_number", "type": "string", "required": True},
                {"id": "email", "type": "string", "required": False}
            ],
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
            ],
        },

        {
            "step_id": "social_category_details",
            "fields": [
                {
                    "id": "caste_category",
                    "type": "enum",
                    "options": ["general", "obc", "sc", "st"],
                    "required": True,
                },
                {"id": "bpl_status", "type": "boolean", "required": True},
                {"id": "is_woman_applicant", "type": "boolean", "required": False},
                {
                    "id": "occupation_type",
                    "type": "enum",
                    "options": [
                        "small_farmer",
                        "marginal_farmer",
                        "landless_labourer",
                        "other"
                    ],
                    "required": True
                }
            ],
        },

        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {
                    "id": "income_below_2_lakh",
                    "type": "boolean",
                    "required": True
                }
            ],
        },

        {
            "step_id": "goat_farming_details",
            "fields": [
                {
                    "id": "goat_unit_requested",
                    "type": "enum",
                    "options": ["3_goats", "5_goats", "11_goats"],
                    "required": True
                },
                {
                    "id": "has_goat_shed",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "previous_experience_goat_farming",
                    "type": "boolean",
                    "required": False
                },
                {
                    "id": "land_available_for_goat_rearing",
                    "type": "boolean",
                    "required": True
                }
            ],
        },

        {
            "step_id": "training_information",
            "fields": [
                {
                    "id": "completed_goat_husbandry_training",
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
                }
            ],
        },

        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_holder_name", "type": "string", "required": True},
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_name", "type": "string", "required": True},
                {"id": "bank_branch", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "aadhaar_linked_bank", "type": "boolean", "required": True}
            ],
        },

        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "upload_aadhaar_card", "type": "file", "required": True},
                {"id": "upload_income_certificate", "type": "file", "required": True},
                {"id": "upload_bank_passbook", "type": "file", "required": True},
                {"id": "upload_bpl_certificate", "type": "file", "required": False},
                {"id": "upload_training_certificate", "type": "file", "required": True},
                {"id": "upload_caste_certificate", "type": "file", "required": False},
                {"id": "upload_unemployment_certificate", "type": "file", "required": False}
            ],
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
            ],
        }

    ],
}
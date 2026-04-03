mukhyaMantriKrishiSaSajuli = {
    "scheme_id": "AGR_SCH_002",
    "scheme_name": "Mukhya Mantri Krishi Sa Sajuli Yojana",
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
                {"id": "block", "type": "string", "required": True},
                {"id": "village", "type": "string", "required": True},
                {"id": "pincode", "type": "number", "required": True},
                {"id": "residential_address", "type": "string", "required": True},
                {"id": "is_assam_resident", "type": "boolean", "required": True}
            ]
        },

        {
            "step_id": "farmer_details",
            "fields": [
                {
                    "id": "farmer_category",
                    "type": "enum",
                    "options": ["small_farmer", "marginal_farmer"],
                    "required": True
                },
                {"id": "years_of_farming_experience", "type": "number", "required": True},
                {
                    "id": "farming_experience_above_3_years",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "primary_crop_type",
                    "type": "enum",
                    "options": [
                        "paddy",
                        "vegetables",
                        "fruits",
                        "cash_crops",
                        "mixed_farming",
                        "other"
                    ],
                    "required": False
                }
            ]
        },

        {
            "step_id": "land_information",
            "fields": [
                {"id": "land_owned", "type": "boolean", "required": True},
                {"id": "total_land_area_acres", "type": "number", "required": True},
                {
                    "id": "land_type",
                    "type": "enum",
                    "options": ["owned", "leased", "shared"],
                    "required": True
                },
                {"id": "land_document_available", "type": "boolean", "required": True}
            ]
        },

        {
            "step_id": "kisan_credit_card_details",
            "fields": [
                {"id": "has_kcc", "type": "boolean", "required": True},
                {"id": "kcc_number", "type": "string", "required": True},
                {"id": "kcc_bank_name", "type": "string", "required": True}
            ]
        },

        {
            "step_id": "farm_mechanization_details",
            "fields": [
                {
                    "id": "tool_to_be_purchased",
                    "type": "enum",
                    "options": [
                        "power_tiller",
                        "sprayer",
                        "seed_drill",
                        "weeder",
                        "mini_tractor",
                        "other"
                    ],
                    "required": True
                },
                {"id": "estimated_tool_cost", "type": "number", "required": True},
                {
                    "id": "has_used_mechanized_tools_before",
                    "type": "boolean",
                    "required": False
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
            "step_id": "family_information",
            "fields": [
                {"id": "family_members_count", "type": "number", "required": False},
                {
                    "id": "only_farmer_in_family",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "upload_aadhaar_card", "type": "file", "required": True},
                {"id": "upload_residence_certificate", "type": "file", "required": True},
                {"id": "upload_land_proof", "type": "file", "required": True},
                {"id": "upload_bank_passbook", "type": "file", "required": True},
                {"id": "upload_caste_certificate", "type": "file", "required": False},
                {"id": "upload_passport_photo", "type": "file", "required": True}
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
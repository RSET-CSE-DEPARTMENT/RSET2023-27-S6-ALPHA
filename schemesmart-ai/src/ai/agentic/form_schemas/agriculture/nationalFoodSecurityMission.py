# src/ai/agentic/form_schemas/agriculture/nationalFoodSecurityMission.py

nationalFoodSecurityMission = {
    "scheme_id": "AGR_SCH_006",
    "scheme_name": "National Food Security Mission",
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
                {"id": "residential_address", "type": "string", "required": True}
            ]
        },

        {
            "step_id": "farmer_profile",
            "fields": [
                {"id": "is_farmer", "type": "boolean", "required": True},
                {
                    "id": "farmer_category",
                    "type": "enum",
                    "options": [
                        "small_farmer",
                        "marginal_farmer",
                        "large_farmer"
                    ],
                    "required": True
                },
                {"id": "is_woman_farmer", "type": "boolean", "required": False},
                {
                    "id": "years_of_farming_experience",
                    "type": "number",
                    "required": False
                }
            ]
        },

        {
            "step_id": "land_details",
            "fields": [
                {"id": "land_owned", "type": "boolean", "required": True},
                {
                    "id": "land_type",
                    "type": "enum",
                    "options": ["owned", "leased", "shared"],
                    "required": True
                },
                {"id": "total_land_area_hectares", "type": "number", "required": True},
                {
                    "id": "area_for_scheme_hectares",
                    "type": "number",
                    "required": True
                }
            ]
        },

        {
            "step_id": "crop_information",
            "fields": [
                {
                    "id": "crop_type",
                    "type": "enum",
                    "options": [
                        "rice",
                        "wheat",
                        "pulses",
                        "coarse_cereals",
                        "oilseeds",
                        "other"
                    ],
                    "required": True
                },
                {
                    "id": "demonstration_type",
                    "type": "enum",
                    "options": [
                        "crop_demonstration",
                        "cropping_system_demonstration",
                        "coarse_cereal_demonstration"
                    ],
                    "required": True
                },
                {
                    "id": "season",
                    "type": "enum",
                    "options": [
                        "kharif",
                        "rabi",
                        "zaid"
                    ],
                    "required": True
                }
            ]
        },

        {
            "step_id": "assistance_requirements",
            "fields": [
                {
                    "id": "need_seed_assistance",
                    "type": "boolean",
                    "required": False
                },
                {
                    "id": "need_farm_implements_support",
                    "type": "boolean",
                    "required": False
                },
                {
                    "id": "need_bio_fertilizers",
                    "type": "boolean",
                    "required": False
                },
                {
                    "id": "need_bio_pesticides",
                    "type": "boolean",
                    "required": False
                }
            ]
        },

        {
            "step_id": "cluster_participation",
            "fields": [
                {
                    "id": "participate_in_cluster_demonstration",
                    "type": "boolean",
                    "required": False
                },
                {
                    "id": "participate_in_frontline_demonstration",
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
            "step_id": "social_category",
            "fields": [
                {
                    "id": "caste_category",
                    "type": "enum",
                    "options": ["general", "obc", "sc", "st"],
                    "required": False
                }
            ]
        },

        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "upload_aadhaar_card", "type": "file", "required": True},
                {"id": "upload_bank_passbook", "type": "file", "required": True},
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
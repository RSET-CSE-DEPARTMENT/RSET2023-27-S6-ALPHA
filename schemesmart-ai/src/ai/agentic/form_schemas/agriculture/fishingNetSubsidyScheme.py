# src/ai/agentic/form_schemas/fisheries/fishingNetSubsidyScheme.py

fishingNetSubsidyScheme = {
    "scheme_id": "AGR_SCH_009",
    "scheme_name": "Financial Assistance to Purchase Singel Net / Small Rampon Net",
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
                {"id": "village_or_coastal_area", "type": "string", "required": True},
                {"id": "pincode", "type": "number", "required": True},
                {"id": "residential_address", "type": "string", "required": True},
                {
                    "id": "goa_resident",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "community_information",
            "fields": [
                {
                    "id": "caste_category",
                    "type": "enum",
                    "options": ["general", "obc", "sc", "st"],
                    "required": True
                },
                {
                    "id": "belongs_to_kharvi_community",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "fisherman_details",
            "fields": [
                {
                    "id": "is_traditional_fisherman",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "fisherman_registration_number",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "years_of_fishing_experience",
                    "type": "number",
                    "required": False
                }
            ]
        },

        {
            "step_id": "fishing_vessel_information",
            "fields": [
                {
                    "id": "owns_registered_fishing_trawler",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "owns_small_fishing_boat",
                    "type": "boolean",
                    "required": False
                },
                {
                    "id": "boat_registration_number",
                    "type": "string",
                    "required": False
                }
            ]
        },

        {
            "step_id": "net_purchase_details",
            "fields": [
                {
                    "id": "type_of_net",
                    "type": "enum",
                    "options": ["singel_net", "small_rampon_net"],
                    "required": True
                },
                {
                    "id": "estimated_cost_of_net",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "apply_for_subsidy",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "last_time_received_net_subsidy",
                    "type": "number",
                    "required": False
                }
            ]
        },

        {
            "step_id": "scheme_eligibility_history",
            "fields": [
                {
                    "id": "received_subsidy_within_last_5_years",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "inspection_details",
            "fields": [
                {
                    "id": "inspection_completed",
                    "type": "boolean",
                    "required": False
                },
                {
                    "id": "inspection_officer_name",
                    "type": "string",
                    "required": False
                },
                {
                    "id": "inspection_date",
                    "type": "date",
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
            "step_id": "document_uploads",
            "fields": [
                {"id": "upload_fishing_net_license", "type": "file", "required": True},
                {"id": "upload_aadhaar_card", "type": "file", "required": True},
                {"id": "upload_bank_passbook", "type": "file", "required": True},
                {"id": "upload_inspection_report", "type": "file", "required": False}
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
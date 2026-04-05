# src/ai/agentic/form_schemas/fisheries/fishingCraftSubsidyScheme.py

fishingCraftSubsidyScheme = {
    "scheme_id": "AGR_SCH_011",
    "scheme_name": "Financial Assistance to Purchase/Construct New Fishing Craft",
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
                {"id": "goa_resident", "type": "boolean", "required": True}
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
                    "id": "is_woman_applicant",
                    "type": "boolean",
                    "required": False
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
            "step_id": "existing_vessel_information",
            "fields": [
                {
                    "id": "owns_registered_fishing_canoe",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "existing_vessel_registration_number",
                    "type": "string",
                    "required": False
                }
            ]
        },

        {
            "step_id": "craft_purchase_or_construction_details",
            "fields": [
                {
                    "id": "craft_type",
                    "type": "enum",
                    "options": ["purchase_new_craft", "construct_new_craft"],
                    "required": True
                },
                {
                    "id": "craft_material",
                    "type": "enum",
                    "options": ["wood", "fiberglass", "other"],
                    "required": False
                },
                {
                    "id": "craft_length_feet",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "estimated_cost_of_craft",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "boat_builder_or_dealer_name",
                    "type": "string",
                    "required": True
                }
            ]
        },

        {
            "step_id": "scheme_eligibility_history",
            "fields": [
                {
                    "id": "received_craft_subsidy_last_7_years",
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
                {"id": "upload_invoice", "type": "file", "required": True},
                {"id": "upload_vessel_registration_certificate", "type": "file", "required": True},
                {"id": "upload_aadhaar_card", "type": "file", "required": True},
                {"id": "upload_bank_passbook", "type": "file", "required": True}
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
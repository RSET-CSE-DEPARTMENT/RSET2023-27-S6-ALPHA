# src/ai/agentic/form_schemas/agriculture/supplyAgricultureMachineries.py

supplyAgricultureMachineries = {
    "scheme_id": "AGR_SCH_016",
    "scheme_name": "Supply of Agriculture Machineries Scheme",
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
            "step_id": "address_details",
            "fields": [
                {"id": "state", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "village_or_town", "type": "string", "required": True},
                {"id": "pincode", "type": "number", "required": True},
                {"id": "residential_address", "type": "string", "required": True},
                {
                    "id": "permanent_resident_of_meghalaya",
                    "type": "boolean",
                    "required": True
                }
            ],
        },

        {
            "step_id": "farmer_details",
            "fields": [
                {
                    "id": "is_bonafide_farmer",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "farmer_registration_number",
                    "type": "string",
                    "required": False
                },
                {
                    "id": "years_of_farming_experience",
                    "type": "number",
                    "required": False
                }
            ],
        },

        {
            "step_id": "land_details",
            "fields": [
                {
                    "id": "total_land_holding_hectares",
                    "type": "number",
                    "required": False
                },
                {
                    "id": "land_location",
                    "type": "string",
                    "required": False
                },
                {
                    "id": "land_ownership_type",
                    "type": "enum",
                    "options": [
                        "owned",
                        "leased",
                        "community_land",
                        "other"
                    ],
                    "required": False
                }
            ],
        },

        {
            "step_id": "machinery_request_details",
            "fields": [
                {
                    "id": "machinery_type_requested",
                    "type": "enum",
                    "options": [
                        "tractor",
                        "power_tiller",
                        "rotavator",
                        "seed_drill",
                        "sprayer",
                        "harvester",
                        "thresher",
                        "other"
                    ],
                    "required": True
                },
                {
                    "id": "machinery_brand_preference",
                    "type": "string",
                    "required": False
                },
                {
                    "id": "estimated_machine_cost",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "subsidy_percentage",
                    "type": "number",
                    "required": False
                },
                {
                    "id": "subsidy_requested_amount",
                    "type": "number",
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
                {"id": "aadhaar_linked", "type": "boolean", "required": True}
            ],
        },

        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "upload_identity_proof", "type": "file", "required": True},
                {"id": "upload_farmer_proof", "type": "file", "required": True},
                {"id": "upload_bank_passbook", "type": "file", "required": True},
                {"id": "upload_photograph", "type": "file", "required": True}
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
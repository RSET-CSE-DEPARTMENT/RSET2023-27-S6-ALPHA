# src/ai/agentic/form_schemas/agriculture/postHarvestMarketingScheme.py

postHarvestMarketingScheme = {
    "scheme_id": "AGR_SCH_015",
    "scheme_name": "Post Harvest Marketing Scheme",
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
                {"id": "identity_proof_number", "type": "string", "required": True},
                {"id": "mobile_number", "type": "string", "required": True},
                {"id": "email", "type": "string", "required": False}
            ]
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
            ]
        },

        {
            "step_id": "farmer_information",
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
            ]
        },

        {
            "step_id": "land_details",
            "fields": [
                {
                    "id": "total_land_holding_hectares",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "land_location",
                    "type": "string",
                    "required": True
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
                    "required": True
                }
            ]
        },

        {
            "step_id": "marketing_infrastructure_details",
            "fields": [
                {
                    "id": "assistance_type",
                    "type": "enum",
                    "options": [
                        "transport_vehicle",
                        "post_harvest_training",
                        "marketing_infrastructure",
                        "multiple"
                    ],
                    "required": True
                },
                {
                    "id": "vehicle_type",
                    "type": "string",
                    "required": False
                },
                {
                    "id": "estimated_vehicle_cost",
                    "type": "number",
                    "required": False
                },
                {
                    "id": "training_days_requested",
                    "type": "number",
                    "required": False
                }
            ]
        },

        {
            "step_id": "subsidy_calculation_details",
            "fields": [
                {
                    "id": "vehicle_subsidy_requested",
                    "type": "number",
                    "required": False
                },
                {
                    "id": "training_allowance_days",
                    "type": "number",
                    "required": False
                }
            ]
        },

        {
            "step_id": "bank_details",
            "fields": [
                {
                    "id": "bank_account_holder_name",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "bank_account_number",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "bank_name",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "bank_branch",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "bank_ifsc",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "aadhaar_linked",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "upload_identity_proof", "type": "file", "required": True},
                {"id": "upload_land_documents", "type": "file", "required": True},
                {"id": "upload_bank_passbook", "type": "file", "required": True},
                {"id": "upload_photograph", "type": "file", "required": True}
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
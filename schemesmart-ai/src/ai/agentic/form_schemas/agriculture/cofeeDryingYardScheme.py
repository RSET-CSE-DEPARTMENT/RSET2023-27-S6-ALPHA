# src/ai/agentic/form_schemas/agriculture/coffeeDryingYardScheme.py

coffeeDryingYardScheme = {
    "scheme_id": "AGR_SCH_008",
    "scheme_name": "Coffee Development Programme – Drying Yards",
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
                {
                    "id": "north_east_resident",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "tribal_status",
            "fields": [
                {
                    "id": "is_tribal_farmer",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "tribal_category",
                    "type": "enum",
                    "options": ["st", "other"],
                    "required": True
                }
            ]
        },

        {
            "step_id": "coffee_grower_details",
            "fields": [
                {
                    "id": "registered_coffee_grower",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "grower_registration_number",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "years_of_coffee_cultivation",
                    "type": "number",
                    "required": False
                }
            ]
        },

        {
            "step_id": "plantation_details",
            "fields": [
                {
                    "id": "land_owned",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "coffee_plantation_area_hectares",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "land_record_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "drying_yard_details",
            "fields": [
                {
                    "id": "apply_for_drying_yard_subsidy",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "existing_drying_yard",
                    "type": "boolean",
                    "required": False
                },
                {
                    "id": "drying_yard_area_sq_meters",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "estimated_construction_cost",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "holding_category",
                    "type": "enum",
                    "options": ["up_to_2_hectares", "above_2_hectares"],
                    "required": True
                }
            ]
        },

        {
            "step_id": "scheme_benefit_history",
            "fields": [
                {
                    "id": "availed_xii_plan_benefits",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "previous_coffee_board_subsidy",
                    "type": "boolean",
                    "required": False
                }
            ]
        },

        {
            "step_id": "inspection_details",
            "fields": [
                {
                    "id": "field_inspection_completed",
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
                {"id": "upload_identity_proof", "type": "file", "required": True},
                {"id": "upload_land_records", "type": "file", "required": True},
                {"id": "upload_bank_passbook", "type": "file", "required": True},
                {"id": "upload_work_completion_report", "type": "file", "required": False}
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
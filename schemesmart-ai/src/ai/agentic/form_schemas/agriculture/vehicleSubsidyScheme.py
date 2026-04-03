# src/ai/agentic/form_schemas/fisheries/vehicleSubsidyScheme.py

vehicleSubsidyScheme = {
    "scheme_id": "AGR_SCH_013",
    "scheme_name": "Grant of Subsidy for Procurement of Vehicle",
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
            "step_id": "address_details",
            "fields": [
                {"id": "state", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "village_or_town", "type": "string", "required": True},
                {"id": "pincode", "type": "number", "required": True},
                {"id": "residential_address", "type": "string", "required": True}
            ]
        },

        {
            "step_id": "community_information",
            "fields": [
                {
                    "id": "is_member_of_fishermen_community",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "member_of_fishermen_cooperative_society",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "cooperative_society_name",
                    "type": "string",
                    "required": True
                }
            ]
        },

        {
            "step_id": "driving_license_details",
            "fields": [
                {"id": "has_valid_driving_license", "type": "boolean", "required": True},
                {"id": "driving_license_number", "type": "string", "required": True},
                {"id": "license_issue_date", "type": "date", "required": False},
                {"id": "license_expiry_date", "type": "date", "required": False}
            ]
        },

        {
            "step_id": "vehicle_details",
            "fields": [
                {
                    "id": "vehicle_type",
                    "type": "enum",
                    "options": [
                        "mini_goods_vehicle",
                        "pickup_truck",
                        "refrigerated_fish_transport_vehicle",
                        "other_goods_vehicle"
                    ],
                    "required": True
                },
                {
                    "id": "vehicle_brand_model",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "vehicle_capacity_tons",
                    "type": "number",
                    "required": False
                },
                {
                    "id": "estimated_vehicle_cost",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "vehicle_dealer_name",
                    "type": "string",
                    "required": True
                }
            ]
        },

        {
            "step_id": "loan_details",
            "fields": [
                {"id": "loan_required", "type": "boolean", "required": True},
                {"id": "loan_sanctioned", "type": "boolean", "required": False},
                {"id": "loan_sanction_order_number", "type": "string", "required": False},
                {"id": "bank_name_for_loan", "type": "string", "required": False},
                {"id": "loan_amount", "type": "number", "required": False}
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
                {"id": "upload_loan_sanction_order", "type": "file", "required": True},
                {"id": "upload_driving_license", "type": "file", "required": True},
                {"id": "upload_vehicle_invoice", "type": "file", "required": True},
                {"id": "upload_bank_documents", "type": "file", "required": True}
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
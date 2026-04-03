# src/ai/agentic/form_schemas/fisheries/outboardMotorSubsidyScheme.py

outboardMotorSubsidyScheme = {
    "scheme_id": "AGR_SCH_010",
    "scheme_name": "Financial Assistance to Purchase Outboard Motor (2HP–5HP)",
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
            "step_id": "vessel_information",
            "fields": [
                {
                    "id": "owns_registered_fishing_canoe",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "vessel_registration_number",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "canoe_length_feet",
                    "type": "number",
                    "required": True
                }
            ]
        },

        {
            "step_id": "motor_purchase_details",
            "fields": [
                {
                    "id": "motor_power_hp",
                    "type": "enum",
                    "options": ["2hp", "3hp", "4hp", "5hp"],
                    "required": True
                },
                {
                    "id": "motor_brand",
                    "type": "string",
                    "required": False
                },
                {
                    "id": "authorized_dealer_name",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "estimated_motor_cost",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "apply_for_subsidy",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "scheme_eligibility_history",
            "fields": [
                {
                    "id": "received_motor_subsidy_last_5_years",
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
                {"id": "upload_vessel_registration_certificate", "type": "file", "required": True},
                {"id": "upload_invoice_from_authorized_dealer", "type": "file", "required": True},
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
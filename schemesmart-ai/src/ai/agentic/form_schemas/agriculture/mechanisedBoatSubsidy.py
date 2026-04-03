# src/ai/agentic/form_schemas/fisheries/mechanisedBoatSubsidy.py

mechanisedBoatSubsidy = {
    "scheme_id": "AGR_SCH_012",
    "scheme_name": "Subsidy for Purchase of Mechanised Fishing Boats",
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
            "step_id": "residence_details",
            "fields": [
                {"id": "state", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "village_or_town", "type": "string", "required": True},
                {"id": "pincode", "type": "number", "required": True},
                {"id": "residential_address", "type": "string", "required": True},
                {
                    "id": "years_of_residence_in_puducherry",
                    "type": "number",
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
                    "required": False
                },
                {
                    "id": "is_fisherman",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "is_fishing_entrepreneur",
                    "type": "boolean",
                    "required": False
                }
            ]
        },

        {
            "step_id": "fishing_experience_details",
            "fields": [
                {
                    "id": "years_of_fishing_experience",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "fishing_license_number",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "member_of_fishermen_cooperative",
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
            "step_id": "boat_details",
            "fields": [
                {
                    "id": "boat_type",
                    "type": "enum",
                    "options": [
                        "new_mechanised_boat_purchase",
                        "boat_modernization",
                        "boat_conversion"
                    ],
                    "required": True
                },
                {
                    "id": "boat_length_feet",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "engine_power_hp",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "boat_material",
                    "type": "enum",
                    "options": ["wood", "fiberglass", "steel", "other"],
                    "required": False
                },
                {
                    "id": "boat_builder_or_supplier",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "estimated_boat_cost",
                    "type": "number",
                    "required": True
                }
            ]
        },

        {
            "step_id": "loan_details",
            "fields": [
                {
                    "id": "loan_required",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "loan_sanctioned",
                    "type": "boolean",
                    "required": False
                },
                {
                    "id": "loan_sanction_letter_number",
                    "type": "string",
                    "required": False
                },
                {
                    "id": "bank_name_for_loan",
                    "type": "string",
                    "required": False
                },
                {
                    "id": "loan_amount",
                    "type": "number",
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
                {"id": "upload_aadhaar_card", "type": "file", "required": True},
                {"id": "upload_residence_certificate", "type": "file", "required": True},
                {"id": "upload_fishing_experience_proof", "type": "file", "required": True},
                {"id": "upload_loan_sanction_letter", "type": "file", "required": True}
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
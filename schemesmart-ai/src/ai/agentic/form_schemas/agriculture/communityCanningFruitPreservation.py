# src/ai/agentic/form_schemas/agriculture/communityCanningFruitPreservation.py

communityCanningFruitPreservation = {
    "scheme_id": "AGR_SCH_004",
    "scheme_name": "Community Canning and Training in Fruit Preservation",
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
                {"id": "block", "type": "string", "required": False},
                {"id": "village_or_town", "type": "string", "required": True},
                {"id": "pincode", "type": "number", "required": True},
                {"id": "residential_address", "type": "string", "required": True},
                {"id": "is_assam_resident", "type": "boolean", "required": True}
            ]
        },

        {
            "step_id": "applicant_category",
            "fields": [
                {
                    "id": "applicant_type",
                    "type": "enum",
                    "options": [
                        "woman",
                        "housewife",
                        "self_help_group_member",
                        "rural_youth",
                        "other"
                    ],
                    "required": True
                },
                {
                    "id": "member_of_shg",
                    "type": "boolean",
                    "required": False
                },
                {"id": "shg_name", "type": "string", "required": False},
                {"id": "occupation", "type": "string", "required": False}
            ]
        },

        {
            "step_id": "education_background",
            "fields": [
                {
                    "id": "highest_education_level",
                    "type": "enum",
                    "options": [
                        "no_formal_education",
                        "primary",
                        "secondary",
                        "higher_secondary",
                        "graduate",
                        "other"
                    ],
                    "required": False
                },
                {
                    "id": "has_food_processing_knowledge",
                    "type": "boolean",
                    "required": False
                }
            ]
        },

        {
            "step_id": "training_details",
            "fields": [
                {
                    "id": "interested_in_training",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "preferred_training_duration",
                    "type": "enum",
                    "options": [
                        "1_day",
                        "3_days",
                        "5_days",
                        "7_days",
                        "10_days",
                        "15_days"
                    ],
                    "required": True
                },
                {
                    "id": "preferred_training_center",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "previous_training_in_food_processing",
                    "type": "boolean",
                    "required": False
                }
            ]
        },

        {
            "step_id": "entrepreneurship_interest",
            "fields": [
                {
                    "id": "interested_in_starting_cottage_industry",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "type_of_products_interested",
                    "type": "enum",
                    "options": [
                        "fruit_jam",
                        "fruit_jelly",
                        "pickle",
                        "squash",
                        "canned_fruits",
                        "mixed_products"
                    ],
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
                {"id": "upload_voter_id", "type": "file", "required": True},
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
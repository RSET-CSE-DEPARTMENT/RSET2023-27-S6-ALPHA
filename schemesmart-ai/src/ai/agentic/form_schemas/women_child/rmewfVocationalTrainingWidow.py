rmewfVocationalTrainingWidow = {
    "scheme_id": "WOMEN_CHILD_001",
    "scheme_name": "RMEWF – Financial Assistance for Vocational Training of Widows of Ex-Servicemen",
    "form_steps": [

        {
            "step_id": "widow_personal_information",
            "fields": [
                {"id": "full_name", "type": "string", "required": True},
                {"id": "date_of_birth", "type": "date", "required": True},
                {"id": "age", "type": "number", "required": True},

                {
                    "id": "gender",
                    "type": "enum",
                    "options": ["female"],
                    "required": True
                },

                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "mobile_number", "type": "string", "required": True},
                {"id": "email_id", "type": "string", "required": False},

                {"id": "widow_identity_card_number", "type": "string", "required": True},

                {
                    "id": "marital_status",
                    "type": "enum",
                    "options": ["widow"],
                    "required": True
                }
            ]
        },

        {
            "step_id": "ex_serviceman_details",
            "fields": [
                {"id": "ex_serviceman_name", "type": "string", "required": True},

                {
                    "id": "relationship_with_ex_serviceman",
                    "type": "enum",
                    "options": ["wife"],
                    "required": True
                },

                {"id": "service_number", "type": "string", "required": True},

                {
                    "id": "rank_of_ex_serviceman",
                    "type": "enum",
                    "options": [
                        "sepoy",
                        "lance_naik",
                        "naik",
                        "havildar"
                    ],
                    "required": True
                },

                {
                    "id": "service_branch",
                    "type": "enum",
                    "options": [
                        "army",
                        "navy",
                        "air_force"
                    ],
                    "required": True
                },

                {"id": "date_of_retirement_or_death", "type": "date", "required": True},

                {
                    "id": "service_discharge_certificate_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "address_details",
            "fields": [
                {"id": "address_line1", "type": "string", "required": True},
                {"id": "address_line2", "type": "string", "required": False},
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "state", "type": "string", "required": True},
                {"id": "pincode", "type": "string", "required": True}
            ]
        },

        {
            "step_id": "vocational_training_details",
            "fields": [
                {"id": "training_course_name", "type": "string", "required": True},

                {
                    "id": "training_category",
                    "type": "enum",
                    "options": [
                        "tailoring",
                        "computer_training",
                        "beautician_course",
                        "handicrafts",
                        "food_processing",
                        "nursing_assistant",
                        "other"
                    ],
                    "required": True
                },

                {"id": "training_institute_name", "type": "string", "required": True},
                {"id": "training_institute_address", "type": "string", "required": True},

                {"id": "training_start_date", "type": "date", "required": True},
                {"id": "training_end_date", "type": "date", "required": True},

                {
                    "id": "training_completed",
                    "type": "boolean",
                    "required": True
                },

                {
                    "id": "training_completion_certificate_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "employment_and_recommendation_details",
            "fields": [
                {
                    "id": "employment_status_after_training",
                    "type": "enum",
                    "options": [
                        "self_employed",
                        "employed",
                        "not_employed"
                    ],
                    "required": True
                },

                {"id": "employment_details", "type": "string", "required": False},

                {
                    "id": "recommended_by_zila_sainik_board",
                    "type": "boolean",
                    "required": True
                },

                {"id": "zila_sainik_board_district", "type": "string", "required": True},

                {"id": "zsw_officer_name", "type": "string", "required": True},

                {
                    "id": "employment_certificate_from_zswo_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_holder_name", "type": "string", "required": True},

                {"id": "bank_name", "type": "string", "required": True},

                {
                    "id": "bank_type",
                    "type": "enum",
                    "options": [
                        "sbi",
                        "pnb"
                    ],
                    "required": True
                },

                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc_code", "type": "string", "required": True},

                {
                    "id": "aadhaar_linked_bank_account",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "document_uploads",
            "fields": [
                {
                    "id": "service_discharge_certificate",
                    "type": "file",
                    "required": True
                },

                {
                    "id": "widow_identity_card",
                    "type": "file",
                    "required": True
                },

                {
                    "id": "training_completion_certificate",
                    "type": "file",
                    "required": True
                },

                {
                    "id": "employment_certificate_zswo",
                    "type": "file",
                    "required": True
                },

                {
                    "id": "bank_passbook_copy",
                    "type": "file",
                    "required": True
                }
            ]
        }
    ]
}
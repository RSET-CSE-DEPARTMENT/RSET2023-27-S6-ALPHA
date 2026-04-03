# src/ai/agentic/form_schemas/employment/krishakUdyamiYojana.py

krishakUdyamiYojana = {
    "scheme_id": "AGR_SCH_014",
    "scheme_name": "Mukhya Mantri Krishak Udyami Yojana",
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
                {"id": "pan_number", "type": "string", "required": True},
                {"id": "mobile_number", "type": "string", "required": True},
                {"id": "email", "type": "string", "required": False}
            ]
        },

        {
            "step_id": "address_details",
            "fields": [
                {"id": "state", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "pincode", "type": "number", "required": True},
                {"id": "residential_address", "type": "string", "required": True},
                {
                    "id": "permanent_resident_of_mp",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "family_background",
            "fields": [
                {
                    "id": "father_or_mother_name",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "parent_is_farmer",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "farmer_registration_number",
                    "type": "string",
                    "required": False
                }
            ]
        },

        {
            "step_id": "education_details",
            "fields": [
                {
                    "id": "highest_qualification",
                    "type": "enum",
                    "options": [
                        "10th_pass",
                        "12th_pass",
                        "diploma",
                        "graduate",
                        "postgraduate",
                        "other"
                    ],
                    "required": True
                },
                {
                    "id": "board_or_university_name",
                    "type": "string",
                    "required": False
                },
                {
                    "id": "year_of_passing",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "percentage_or_grade",
                    "type": "string",
                    "required": False
                }
            ]
        },

        {
            "step_id": "income_details",
            "fields": [
                {
                    "id": "is_income_tax_payer",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "annual_family_income",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "bpl_status",
                    "type": "boolean",
                    "required": False
                }
            ]
        },

        {
            "step_id": "business_proposal",
            "fields": [
                {
                    "id": "proposed_business_type",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "business_sector",
                    "type": "enum",
                    "options": [
                        "manufacturing",
                        "service",
                        "agriculture_related",
                        "food_processing",
                        "retail",
                        "other"
                    ],
                    "required": True
                },
                {
                    "id": "project_location",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "estimated_project_cost",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "loan_required",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "loan_details",
            "fields": [
                {
                    "id": "loan_amount_requested",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "bank_name_for_loan",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "bank_branch",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "loan_sanctioned",
                    "type": "boolean",
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
                {"id": "upload_aadhaar_card", "type": "file", "required": True},
                {"id": "upload_pan_card", "type": "file", "required": True},
                {"id": "upload_income_certificate", "type": "file", "required": True},
                {"id": "upload_10th_marksheet", "type": "file", "required": True},
                {"id": "upload_bpl_certificate", "type": "file", "required": False}
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
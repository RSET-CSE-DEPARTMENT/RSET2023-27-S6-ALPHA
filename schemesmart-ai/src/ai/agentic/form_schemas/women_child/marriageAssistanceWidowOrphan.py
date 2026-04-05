marriageAssistanceWidowOrphan = {
    "scheme_id": "WOMEN_CHILD_002",
    "scheme_name": "Financial Assistance for Marriage of Daughters of Poor Widows and Orphan Girls",
    "form_steps": [
        {
            "step_id": "applicant_information",
            "fields": [
                {"id": "applicant_full_name", "type": "string", "required": True},
                {"id": "date_of_birth", "type": "date", "required": True},
                {"id": "age", "type": "number", "required": True},
                {
                    "id": "applicant_type",
                    "type": "enum",
                    "options": ["widow", "orphan_girl"],
                    "required": True,
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "mobile_number", "type": "string", "required": True},
                {"id": "email", "type": "string", "required": False},
            ],
        },
        {
            "step_id": "residency_details",
            "fields": [
                {"id": "state_of_residence", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "address_line1", "type": "string", "required": True},
                {"id": "address_line2", "type": "string", "required": False},
                {"id": "pincode", "type": "string", "required": True},
                {"id": "years_of_residence_in_delhi", "type": "number", "required": True},
            ],
        },
        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {"id": "income_below_one_lakh", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "girl_marriage_details",
            "fields": [
                {"id": "girl_full_name", "type": "string", "required": True},
                {"id": "girl_date_of_birth", "type": "date", "required": True},
                {"id": "girl_age", "type": "number", "required": True},
                {
                    "id": "marital_status",
                    "type": "enum",
                    "options": ["unmarried"],
                    "required": True,
                },
                {"id": "marriage_date", "type": "date", "required": True},
                {"id": "marriage_location", "type": "string", "required": True},
                {"id": "marriage_invitation_available", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "guardian_details",
            "fields": [
                {"id": "guardian_name", "type": "string", "required": False},
                {
                    "id": "guardian_relationship",
                    "type": "enum",
                    "options": ["mother", "relative", "legal_guardian"],
                    "required": False,
                },
                {"id": "husband_death_certificate_available", "type": "boolean", "required": False},
            ],
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_holder_name", "type": "string", "required": True},
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "aadhaar_linked", "type": "boolean", "required": True},
                {"id": "single_operated_account", "type": "boolean", "required": True},
            ],
        },
    ],
}
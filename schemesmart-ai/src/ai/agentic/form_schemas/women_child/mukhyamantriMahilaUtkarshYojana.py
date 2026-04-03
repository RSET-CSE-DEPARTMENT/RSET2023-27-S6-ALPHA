mukhyamantriMahilaUtkarshYojana = {
    "scheme_id": "WOMEN_CHILD_005",
    "scheme_name": "Mukhyamantri Mahila Utkarsh Yojana",
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
                    "options": ["female"],
                    "required": True,
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "mobile_number", "type": "string", "required": True},
                {"id": "email", "type": "string", "required": False},
            ],
        },
        {
            "step_id": "education_details",
            "fields": [
                {
                    "id": "highest_education",
                    "type": "enum",
                    "options": [
                        "below_8th",
                        "8th_pass",
                        "10th_pass",
                        "12th_pass",
                        "graduate",
                        "postgraduate"
                    ],
                    "required": True,
                },
                {"id": "education_certificate_available", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "residency_details",
            "fields": [
                {"id": "state", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "address_line1", "type": "string", "required": True},
                {"id": "address_line2", "type": "string", "required": False},
                {"id": "pincode", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "business_details",
            "fields": [
                {"id": "business_name", "type": "string", "required": True},
                {
                    "id": "business_type",
                    "type": "enum",
                    "options": [
                        "manufacturing",
                        "service",
                        "trading",
                        "agriculture_related",
                        "handicrafts",
                        "other"
                    ],
                    "required": True,
                },
                {"id": "business_experience", "type": "boolean", "required": False},
                {"id": "business_plan_submitted", "type": "boolean", "required": True},
                {"id": "loan_amount_requested", "type": "number", "required": True},
            ],
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_holder_name", "type": "string", "required": True},
                {"id": "bank_name", "type": "string", "required": True},
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "aadhaar_linked", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "document_details",
            "fields": [
                {"id": "aadhaar_card_uploaded", "type": "boolean", "required": True},
                {"id": "education_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "business_plan_uploaded", "type": "boolean", "required": True},
                {"id": "bank_details_uploaded", "type": "boolean", "required": True},
                {"id": "photographs_uploaded", "type": "boolean", "required": True},
            ],
        },
    ],
}
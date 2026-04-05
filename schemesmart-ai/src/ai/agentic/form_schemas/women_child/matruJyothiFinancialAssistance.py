matruJyothiFinancialAssistance = {
    "scheme_id": "WOMEN_CHILD_013",
    "scheme_name": "Matru Jyothi – Financial Assistance for PwD Mothers",
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
            "step_id": "disability_details",
            "fields": [
                {"id": "person_with_disability", "type": "boolean", "required": True},
                {"id": "disability_certificate_available", "type": "boolean", "required": True},
                {"id": "disability_percentage", "type": "number", "required": False},
            ],
        },
        {
            "step_id": "child_details",
            "fields": [
                {"id": "child_name", "type": "string", "required": True},
                {"id": "child_date_of_birth", "type": "date", "required": True},
                {"id": "child_age", "type": "number", "required": True},
                {"id": "child_age_below_two_years", "type": "boolean", "required": True},
                {"id": "hospital_discharge_certificate_available", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {"id": "income_below_limit", "type": "boolean", "required": True},
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
                {"id": "residence_certificate_available", "type": "boolean", "required": True},
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
                {"id": "disability_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "hospital_discharge_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "income_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "bank_passbook_uploaded", "type": "boolean", "required": True},
                {"id": "photograph_uploaded", "type": "boolean", "required": True},
            ],
        },
    ],
}
widowPensionWestBengal = {
    "scheme_id": "WOMEN_CHILD_019",
    "scheme_name": "Widow Pension",
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
                    "required": True
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "mobile_number", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "marital_status_details",
            "fields": [
                {
                    "id": "marital_status",
                    "type": "enum",
                    "options": ["widow"],
                    "required": True
                },
                {
                    "id": "husband_death_certificate_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "income_details",
            "fields": [
                {"id": "monthly_income", "type": "number", "required": True},
                {"id": "income_below_limit", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "residency_details",
            "fields": [
                {"id": "state", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "years_of_residency", "type": "number", "required": True},
                {"id": "address_line1", "type": "string", "required": True},
                {"id": "address_line2", "type": "string", "required": False},
                {"id": "pincode", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "identity_documents",
            "fields": [
                {"id": "ration_card_available", "type": "boolean", "required": True},
                {"id": "voter_id_available", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_holder_name", "type": "string", "required": True},
                {"id": "bank_name", "type": "string", "required": True},
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "bank_passbook_available", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "document_details",
            "fields": [
                {"id": "aadhaar_card_uploaded", "type": "boolean", "required": True},
                {"id": "ration_card_uploaded", "type": "boolean", "required": True},
                {"id": "voter_id_uploaded", "type": "boolean", "required": True},
                {"id": "income_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "husband_death_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "bank_passbook_uploaded", "type": "boolean", "required": True}
            ]
        }
    ]
}
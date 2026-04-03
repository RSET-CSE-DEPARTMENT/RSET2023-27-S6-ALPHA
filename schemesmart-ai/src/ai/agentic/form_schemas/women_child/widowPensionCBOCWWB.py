widowPensionCBOCWWB = {
    "scheme_id": "WOMEN_CHILD_020",
    "scheme_name": "Widow Pension (CBOCWWB)",
    "form_steps": [
        {
            "step_id": "personal_information",
            "fields": [
                {"id": "full_name", "type": "string", "required": True},
                {"id": "date_of_birth", "type": "date", "required": True},
                {"id": "age", "type": "number", "required": True},
                {"id": "gender", "type": "enum", "options": ["female"], "required": True},
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "mobile_number", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "employment_membership_details",
            "fields": [
                {
                    "id": "membership_type",
                    "type": "enum",
                    "options": ["construction_worker_widow"],
                    "required": True
                },
                {
                    "id": "membership_duration_months",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "application_within_1_year_of_death",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "not_covered_under_epf",
                    "type": "boolean",
                    "required": True
                },
                {"id": "bocw_card_available", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "income_and_pension_details",
            "fields": [
                {"id": "monthly_income", "type": "number", "required": False},
                {"id": "monthly_pension_expected", "type": "number", "required": True}
            ]
        },
        {
            "step_id": "residency_details",
            "fields": [
                {"id": "state", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "address_line1", "type": "string", "required": True},
                {"id": "address_line2", "type": "string", "required": False},
                {"id": "pincode", "type": "string", "required": True},
                {"id": "residency_proof_available", "type": "boolean", "required": True}
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
                {"id": "bocw_card_uploaded", "type": "boolean", "required": True},
                {"id": "death_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "bank_passbook_uploaded", "type": "boolean", "required": True},
                {"id": "salary_slip_uploaded", "type": "boolean", "required": True},
                {"id": "self_declaration_uploaded", "type": "boolean", "required": True}
            ]
        }
    ]
}
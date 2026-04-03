asangathitKarmakaarSilaiMachineSahayataYojana = {
    "scheme_id": "WOMEN_CHILD_017",
    "scheme_name": "Asangathit Karmakaar Silai Machine Sahayata Yojana",
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
                {"id": "mobile_number", "type": "string", "required": True},
                {"id": "aadhaar_number", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "occupation_details",
            "fields": [
                {
                    "id": "occupation_type",
                    "type": "enum",
                    "options": ["tailoring", "sewing"],
                    "required": True
                },
                {
                    "id": "experience_in_tailoring",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "labour_registration_details",
            "fields": [
                {"id": "labour_board_registered", "type": "boolean", "required": True},
                {"id": "labour_registration_number", "type": "string", "required": True},
                {"id": "labour_registration_card_available", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": False},
                {"id": "income_certificate_available", "type": "boolean", "required": True}
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
                {"id": "labour_registration_card_uploaded", "type": "boolean", "required": True},
                {"id": "age_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "income_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "bank_passbook_uploaded", "type": "boolean", "required": True}
            ]
        }
    ]
}
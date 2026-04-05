kanyashreePrakalpa = {
    "scheme_id": "WOMEN_CHILD_006",
    "scheme_name": "Kanyashree Prakalpa",
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
                {"id": "aadhaar_number", "type": "string", "required": False},
                {"id": "mobile_number", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "education_details",
            "fields": [
                {"id": "is_student", "type": "boolean", "required": True},
                {"id": "institution_name", "type": "string", "required": True},
                {
                    "id": "education_level",
                    "type": "enum",
                    "options": [
                        "class_8",
                        "class_9",
                        "class_10",
                        "class_11",
                        "class_12",
                        "undergraduate"
                    ],
                    "required": True,
                },
                {"id": "institution_id", "type": "string", "required": False},
            ],
        },
        {
            "step_id": "marital_status_details",
            "fields": [
                {
                    "id": "marital_status",
                    "type": "enum",
                    "options": ["unmarried"],
                    "required": True,
                },
                {"id": "unmarried_declaration_available", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {"id": "income_within_limit", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_holder_name", "type": "string", "required": True},
                {"id": "bank_name", "type": "string", "required": True},
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "bank_passbook_available", "type": "boolean", "required": True},
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
            "step_id": "document_details",
            "fields": [
                {"id": "birth_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "income_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "unmarried_declaration_uploaded", "type": "boolean", "required": True},
                {"id": "bank_passbook_uploaded", "type": "boolean", "required": True},
                {"id": "residence_proof_uploaded", "type": "boolean", "required": True},
            ],
        },
    ],
}
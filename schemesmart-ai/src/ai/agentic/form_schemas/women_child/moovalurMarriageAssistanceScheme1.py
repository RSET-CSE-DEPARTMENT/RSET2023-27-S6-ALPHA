moovalurMarriageAssistanceScheme1 = {
    "scheme_id": "WOMEN_CHILD_014",
    "scheme_name": "Moovalur Ramamirtham Ammaiyar Ninaivu Marriage Assistance Scheme-1",
    "form_steps": [
        {
            "step_id": "personal_information",
            "fields": [
                {"id": "bride_full_name", "type": "string", "required": True},
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
            "step_id": "education_details",
            "fields": [
                {
                    "id": "education_level",
                    "type": "enum",
                    "options": [
                        "class_5",
                        "class_10",
                        "class_12",
                        "graduate",
                        "post_graduate"
                    ],
                    "required": True
                },
                {
                    "id": "st_category",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "school_certificate_available",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "marksheet_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "marriage_details",
            "fields": [
                {"id": "marriage_date", "type": "date", "required": True},
                {"id": "marriage_invitation_available", "type": "boolean", "required": True},
                {"id": "first_girl_in_family", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {"id": "income_below_limit", "type": "boolean", "required": True}
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
                {"id": "ration_card_available", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_holder_name", "type": "string", "required": True},
                {"id": "bank_name", "type": "string", "required": True},
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "aadhaar_linked", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "document_details",
            "fields": [
                {"id": "income_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "community_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "marriage_invitation_uploaded", "type": "boolean", "required": True},
                {"id": "school_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "marksheet_uploaded", "type": "boolean", "required": True},
                {"id": "ration_card_uploaded", "type": "boolean", "required": True},
                {"id": "aadhaar_card_uploaded", "type": "boolean", "required": True},
                {"id": "bank_passbook_uploaded", "type": "boolean", "required": True}
            ]
        }
    ]
}
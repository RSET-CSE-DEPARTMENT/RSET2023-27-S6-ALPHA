saraswatiCycleYojana = {
    "scheme_id": "WOMEN_CHILD_007",
    "scheme_name": "Saraswati Cycle Yojana",
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
                {"id": "mobile_number", "type": "string", "required": False},
            ],
        },
        {
            "step_id": "education_details",
            "fields": [
                {"id": "is_student", "type": "boolean", "required": True},
                {
                    "id": "current_class",
                    "type": "enum",
                    "options": ["class_9"],
                    "required": True,
                },
                {"id": "school_name", "type": "string", "required": True},
                {"id": "school_id", "type": "string", "required": False},
                {
                    "id": "school_type",
                    "type": "enum",
                    "options": ["government", "government_aided"],
                    "required": True,
                },
            ],
        },
        {
            "step_id": "category_details",
            "fields": [
                {
                    "id": "category",
                    "type": "enum",
                    "options": ["bpl", "sc", "st"],
                    "required": True,
                },
                {"id": "bpl_card_available", "type": "boolean", "required": False},
                {"id": "caste_certificate_available", "type": "boolean", "required": False},
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
            "step_id": "school_verification",
            "fields": [
                {"id": "headmaster_name", "type": "string", "required": True},
                {"id": "school_certificate_available", "type": "boolean", "required": True},
                {"id": "application_verified_by_school", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "document_details",
            "fields": [
                {"id": "bpl_card_uploaded", "type": "boolean", "required": False},
                {"id": "caste_certificate_uploaded", "type": "boolean", "required": False},
                {"id": "school_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "aadhaar_card_uploaded", "type": "boolean", "required": True},
            ],
        },
    ],
}
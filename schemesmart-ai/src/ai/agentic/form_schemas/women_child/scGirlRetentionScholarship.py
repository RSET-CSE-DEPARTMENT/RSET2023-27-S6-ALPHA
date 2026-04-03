scGirlRetentionScholarship = {
    "scheme_id": "WOMEN_CHILD_018",
    "scheme_name": "Grant of Retention Scholarship to Scheduled Caste Girl Students",
    "form_steps": [
        {
            "step_id": "student_information",
            "fields": [
                {"id": "student_full_name", "type": "string", "required": True},
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
                    "id": "current_class",
                    "type": "enum",
                    "options": ["class_1", "class_2", "class_3", "class_4", "class_5"],
                    "required": True
                },
                {"id": "school_name", "type": "string", "required": True},
                {"id": "school_certificate_available", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "caste_details",
            "fields": [
                {
                    "id": "caste_category",
                    "type": "enum",
                    "options": ["scheduled_caste"],
                    "required": True
                },
                {"id": "caste_certificate_available", "type": "boolean", "required": True}
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
                {"id": "bank_account_linked_to_aadhaar", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "document_details",
            "fields": [
                {"id": "aadhaar_card_uploaded", "type": "boolean", "required": True},
                {"id": "caste_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "income_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "school_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "bank_details_uploaded", "type": "boolean", "required": True}
            ]
        }
    ]
}
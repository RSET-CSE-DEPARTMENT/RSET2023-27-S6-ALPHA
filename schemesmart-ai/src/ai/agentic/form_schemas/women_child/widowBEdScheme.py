widowBEdScheme = {
    "scheme_id": "WOMEN_CHILD_015",
    "scheme_name": "Widow B.Ed Scheme",
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
                    "options": ["widowed", "divorced", "abandoned"],
                    "required": True
                },
                {
                    "id": "status_certificate_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "education_details",
            "fields": [
                {
                    "id": "course_name",
                    "type": "enum",
                    "options": ["bed_regular"],
                    "required": True
                },
                {"id": "institution_name", "type": "string", "required": True},
                {"id": "attendance_percentage", "type": "number", "required": True},
                {"id": "minimum_attendance_met", "type": "boolean", "required": True}
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
                {"id": "domicile_certificate_available", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "identity_details",
            "fields": [
                {"id": "jan_aadhaar_number", "type": "string", "required": True},
                {"id": "sso_id_available", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "course_fee_details",
            "fields": [
                {"id": "fee_paid_amount", "type": "number", "required": True},
                {"id": "fee_receipt_available", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "document_details",
            "fields": [
                {"id": "aadhaar_card_uploaded", "type": "boolean", "required": True},
                {"id": "status_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "domicile_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "education_certificates_uploaded", "type": "boolean", "required": True},
                {"id": "fee_receipt_uploaded", "type": "boolean", "required": True},
                {"id": "jan_aadhaar_uploaded", "type": "boolean", "required": True}
            ]
        }
    ]
}
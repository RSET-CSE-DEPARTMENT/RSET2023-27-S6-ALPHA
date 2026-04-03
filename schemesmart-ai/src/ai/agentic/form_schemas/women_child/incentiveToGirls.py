incentiveToGirls = {
    "scheme_id": "WOMEN_CHILD_012",
    "scheme_name": "Incentive To Girls",
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
                {"id": "is_student", "type": "boolean", "required": True},
                {
                    "id": "education_level",
                    "type": "enum",
                    "options": [
                        "senior_secondary",
                        "graduation",
                        "post_graduation",
                        "phd"
                    ],
                    "required": True,
                },
                {"id": "institution_name", "type": "string", "required": True},
                {
                    "id": "institution_recognized",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "previous_year_passed",
                    "type": "boolean",
                    "required": True,
                },
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
                {"id": "domicile_certificate_available", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "identity_details",
            "fields": [
                {"id": "jan_aadhaar_number", "type": "string", "required": True},
                {"id": "sso_id_available", "type": "boolean", "required": True},
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
                {"id": "jan_aadhaar_uploaded", "type": "boolean", "required": True},
                {"id": "photograph_uploaded", "type": "boolean", "required": True},
                {"id": "age_proof_uploaded", "type": "boolean", "required": True},
                {"id": "address_proof_uploaded", "type": "boolean", "required": True},
                {"id": "educational_certificates_uploaded", "type": "boolean", "required": True},
                {"id": "bank_passbook_uploaded", "type": "boolean", "required": True},
            ],
        },
    ],
}
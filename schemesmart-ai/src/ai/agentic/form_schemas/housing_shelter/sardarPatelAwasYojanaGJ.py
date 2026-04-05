sardarPatelAwasYojanaGJ = {
    "scheme_id": "HOUSING_020",
    "scheme_name": "Sardar Patel Awas Yojana",
    "form_steps": [
        {
            "step_id": "applicant_personal_information",
            "fields": [
                {"id": "full_name", "type": "string", "required": True},
                {"id": "date_of_birth", "type": "date", "required": True},
                {"id": "age", "type": "number", "required": True},
                {
                    "id": "gender",
                    "type": "enum",
                    "options": ["male", "female", "other"],
                    "required": True
                },
                {"id": "aadhaar_number", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "residency_details",
            "fields": [
                {
                    "id": "citizenship",
                    "type": "enum",
                    "options": ["indian"],
                    "required": True
                },
                {
                    "id": "state_of_residence",
                    "type": "enum",
                    "options": ["gujarat"],
                    "required": True
                },
                {"id": "district", "type": "string", "required": True},
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "full_address", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "economic_status",
            "fields": [
                {
                    "id": "belongs_to_bpl_family",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "bpl_certificate_available",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "annual_family_income",
                    "type": "number",
                    "required": False
                }
            ]
        },
        {
            "step_id": "housing_status",
            "fields": [
                {
                    "id": "owns_house",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "owns_land_or_plot",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "land_records_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "local_verification",
            "fields": [
                {
                    "id": "sarpanch_certificate_available",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "panchayat_name",
                    "type": "string",
                    "required": True
                }
            ]
        },
        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "bpl_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "identity_proof_uploaded", "type": "boolean", "required": True},
                {"id": "address_proof_uploaded", "type": "boolean", "required": True},
                {"id": "land_records_uploaded", "type": "boolean", "required": True},
                {"id": "sarpanch_certificate_uploaded", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "declaration",
            "fields": [
                {"id": "information_true", "type": "boolean", "required": True},
                {"id": "applicant_signature_name", "type": "string", "required": True},
                {"id": "submission_date", "type": "date", "required": True}
            ]
        }
    ]
}
icdsScheme = {
    "scheme_id": "HEA_SCH_004",
    "scheme_name": "Integrated Child Development Services (ICDS)",
    "form_steps": [
        {
            "step_id": "beneficiary_type",
            "fields": [
                {
                    "id": "beneficiary_category",
                    "type": "enum",
                    "options": [
                        "child_0_6_years",
                        "pregnant_woman",
                        "lactating_mother"
                    ],
                    "required": True,
                }
            ],
        },
        {
            "step_id": "personal_information",
            "fields": [
                {"id": "full_name", "type": "string", "required": True},
                {"id": "date_of_birth", "type": "date", "required": False},
                {"id": "age", "type": "number", "required": True},
                {
                    "id": "gender",
                    "type": "enum",
                    "options": ["male", "female", "other"],
                    "required": True,
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "guardian_information",
            "fields": [
                {"id": "guardian_name", "type": "string", "required": False},
                {
                    "id": "guardian_relationship",
                    "type": "enum",
                    "options": ["mother", "father", "guardian"],
                    "required": False,
                },
                {"id": "guardian_mobile_number", "type": "string", "required": False},
            ],
        },
        {
            "step_id": "maternal_health_details",
            "fields": [
                {
                    "id": "is_pregnant",
                    "type": "boolean",
                    "required": False,
                },
                {
                    "id": "is_lactating_mother",
                    "type": "boolean",
                    "required": False,
                },
                {"id": "expected_delivery_date", "type": "date", "required": False},
                {
                    "id": "number_of_children",
                    "type": "number",
                    "required": False,
                },
            ],
        },
        {
            "step_id": "residency_details",
            "fields": [
                {
                    "id": "citizenship",
                    "type": "enum",
                    "options": ["indian"],
                    "required": True,
                },
                {
                    "id": "state_of_residence",
                    "type": "enum",
                    "options": ["nagaland"],
                    "required": True,
                },
                {"id": "district", "type": "string", "required": True},
                {"id": "village_or_town", "type": "string", "required": True},
                {"id": "full_address", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "anganwadi_details",
            "fields": [
                {"id": "anganwadi_center_name", "type": "string", "required": True},
                {"id": "anganwadi_worker_name", "type": "string", "required": False},
                {
                    "id": "registered_at_anganwadi",
                    "type": "boolean",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "aadhaar_uploaded", "type": "boolean", "required": True},
                {"id": "age_proof_uploaded", "type": "boolean", "required": True},
                {"id": "address_proof_uploaded", "type": "boolean", "required": True},
                {
                    "id": "passport_photograph_uploaded",
                    "type": "boolean",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "declaration",
            "fields": [
                {"id": "information_true", "type": "boolean", "required": True},
                {"id": "applicant_signature_name", "type": "string", "required": True},
                {"id": "submission_date", "type": "date", "required": True},
            ],
        },
    ],
}
mukhyamantriAwasYojnaHP = {
    "scheme_id": "HOUSING_014",
    "scheme_name": "Mukhyamantri Awas Yojna (HPBOCWWB)",
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
            "step_id": "worker_registration_details",
            "fields": [
                {
                    "id": "registered_hp_boc_worker",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "labour_card_available",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "active_membership",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "employment_details",
            "fields": [
                {
                    "id": "days_worked_last_12_months",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "occupation",
                    "type": "enum",
                    "options": ["construction_worker"],
                    "required": True
                }
            ]
        },
        {
            "step_id": "eligibility_age_details",
            "fields": [
                {
                    "id": "age_between_18_60",
                    "type": "boolean",
                    "required": True
                }
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
                    "options": ["himachal_pradesh"],
                    "required": True
                },
                {"id": "district", "type": "string", "required": True},
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "full_address", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_holder_name", "type": "string", "required": True},
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "bank_name", "type": "string", "required": True},
                {"id": "branch_name", "type": "string", "required": False}
            ]
        },
        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "labour_card_uploaded", "type": "boolean", "required": True},
                {"id": "identity_proof_uploaded", "type": "boolean", "required": True},
                {"id": "address_proof_uploaded", "type": "boolean", "required": True},
                {"id": "bank_passbook_uploaded", "type": "boolean", "required": True},
                {"id": "age_proof_uploaded", "type": "boolean", "required": True}
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
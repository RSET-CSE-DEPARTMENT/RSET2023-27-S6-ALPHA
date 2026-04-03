banglarAwaasYojana = {
    "scheme_id": "HOUSING_012",
    "scheme_name": "Banglar Awaas Yojana (BAY)",
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
            "step_id": "citizenship_details",
            "fields": [
                {
                    "id": "citizenship",
                    "type": "enum",
                    "options": ["indian"],
                    "required": True
                }
            ]
        },
        {
            "step_id": "secc_list_verification",
            "fields": [
                {
                    "id": "name_in_secc_2011_waiting_list",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "secc_reference_number",
                    "type": "string",
                    "required": False
                }
            ]
        },
        {
            "step_id": "housing_condition_details",
            "fields": [
                {
                    "id": "current_housing_status",
                    "type": "enum",
                    "options": ["houseless", "kutcha_house", "dilapidated_house"],
                    "required": True
                },
                {
                    "id": "owns_pucca_house",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "residency_details",
            "fields": [
                {
                    "id": "state_of_residence",
                    "type": "enum",
                    "options": ["west_bengal"],
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
            "step_id": "additional_support_details",
            "fields": [
                {
                    "id": "mgnregs_job_card_available",
                    "type": "boolean",
                    "required": False
                },
                {
                    "id": "toilet_construction_required",
                    "type": "boolean",
                    "required": False
                }
            ]
        },
        {
            "step_id": "document_uploads",
            "fields": [
                {
                    "id": "residence_proof_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "bank_details_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "other_documents_uploaded",
                    "type": "boolean",
                    "required": False
                }
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
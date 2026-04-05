chikitsaPratipoortiYojana = {
    "scheme_id": "HEA_SCH_005",
    "scheme_name": "Chikitsa Pratipoorti Yojana",
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
                    "options": ["male", "female", "other"],
                    "required": True,
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "worker_registration_details",
            "fields": [
                {
                    "id": "registered_with_bocw_board",
                    "type": "boolean",
                    "required": True,
                },
                {"id": "bocw_registration_number", "type": "string", "required": True},
                {"id": "eshram_card_number", "type": "string", "required": True},
                {
                    "id": "construction_worker",
                    "type": "boolean",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "medical_details",
            "fields": [
                {
                    "id": "suffering_from_serious_disease",
                    "type": "boolean",
                    "required": True,
                },
                {"id": "disease_name", "type": "string", "required": True},
                {
                    "id": "treatment_hospital_name",
                    "type": "string",
                    "required": True,
                },
                {
                    "id": "treatment_start_date",
                    "type": "date",
                    "required": False,
                },
                {
                    "id": "estimated_treatment_cost",
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
                    "options": ["jharkhand"],
                    "required": True,
                },
                {"id": "district", "type": "string", "required": True},
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "full_address", "type": "string", "required": True},
                {
                    "id": "domicile_certificate_available",
                    "type": "boolean",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_holder_name", "type": "string", "required": True},
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "bank_name", "type": "string", "required": True},
                {"id": "branch_name", "type": "string", "required": False},
                {
                    "id": "aadhaar_linked",
                    "type": "boolean",
                    "required": False,
                },
            ],
        },
        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "aadhaar_uploaded", "type": "boolean", "required": True},
                {
                    "id": "domicile_certificate_uploaded",
                    "type": "boolean",
                    "required": True,
                },
                {"id": "eshram_card_uploaded", "type": "boolean", "required": True},
                {"id": "medical_proof_uploaded", "type": "boolean", "required": True},
                {
                    "id": "bank_details_uploaded",
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
constructionWorkerHousingLoan = {
    "scheme_id": "HOUSING_008",
    "scheme_name": "Loans and Advances for Construction of a House",
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
                    "id": "registered_construction_worker",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "labor_card_number",
                    "type": "string",
                    "required": True,
                },
                {
                    "id": "labor_card_active",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "registration_certificate_available",
                    "type": "boolean",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "housing_loan_details",
            "fields": [
                {
                    "id": "requested_loan_amount",
                    "type": "number",
                    "required": True,
                },
                {
                    "id": "construction_purpose",
                    "type": "enum",
                    "options": [
                        "new_house_construction",
                        "house_extension",
                        "house_repair"
                    ],
                    "required": True,
                },
                {
                    "id": "construction_estimate_available",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "surety_bond_available",
                    "type": "boolean",
                    "required": True,
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
                    "options": ["manipur"],
                    "required": True,
                },
                {"id": "district", "type": "string", "required": True},
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "full_address", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "contribution_details",
            "fields": [
                {
                    "id": "contribution_receipt_available",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "last_contribution_date",
                    "type": "date",
                    "required": False,
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
            ],
        },
        {
            "step_id": "document_uploads",
            "fields": [
                {
                    "id": "registration_certificate_uploaded",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "contribution_receipt_uploaded",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "construction_estimate_uploaded",
                    "type": "boolean",
                    "required": True,
                },
                {"id": "aadhaar_uploaded", "type": "boolean", "required": True},
                {
                    "id": "bank_passbook_uploaded",
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
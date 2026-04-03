interestSubsidyHomeLoanKSB = {
    "scheme_id": "HOUSING_017",
    "scheme_name": "Financial Assistance as Interest Subsidy on Home Loan",
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
            "step_id": "service_details",
            "fields": [
                {
                    "id": "service_category",
                    "type": "enum",
                    "options": ["war_widow", "disabled_ex_serviceman"],
                    "required": True
                },
                {
                    "id": "ex_servicemen_identity_card_available",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "discharge_book_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "home_loan_details",
            "fields": [
                {
                    "id": "home_loan_taken",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "loan_amount",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "loan_from_approved_institution",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "loan_start_year",
                    "type": "number",
                    "required": False
                }
            ]
        },
        {
            "step_id": "interest_payment_details",
            "fields": [
                {
                    "id": "interest_payment_statement_available",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "bank_certificate_available",
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
                {"id": "state_of_residence", "type": "string", "required": True},
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
                {
                    "id": "ex_servicemen_identity_card_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "discharge_book_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "bank_certificate_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "interest_payment_statement_uploaded",
                    "type": "boolean",
                    "required": True
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
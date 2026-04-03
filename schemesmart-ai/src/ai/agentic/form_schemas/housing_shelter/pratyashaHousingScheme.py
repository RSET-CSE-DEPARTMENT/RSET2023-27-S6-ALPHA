pratyashaHousingScheme = {
    "scheme_id": "HOUSING_003",
    "scheme_name": "Pratyasha Housing Scheme",
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
                    "required": True,
                },
                {"id": "pan_number", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "police_service_details",
            "fields": [
                {
                    "id": "police_force",
                    "type": "enum",
                    "options": ["west_bengal_police", "kolkata_police"],
                    "required": True,
                },
                {"id": "designation", "type": "string", "required": True},
                {"id": "service_id_number", "type": "string", "required": True},
                {"id": "years_of_service", "type": "number", "required": True},
                {
                    "id": "currently_in_service",
                    "type": "boolean",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "income_details",
            "fields": [
                {"id": "monthly_salary", "type": "number", "required": True},
                {"id": "annual_income", "type": "number", "required": True},
                {
                    "id": "salary_certificate_available",
                    "type": "boolean",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "housing_preferences",
            "fields": [
                {
                    "id": "flat_category",
                    "type": "enum",
                    "options": ["category_a", "category_b", "category_c"],
                    "required": True,
                },
                {
                    "id": "first_time_applicant",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "agree_lottery_allotment",
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
            ],
        },
        {
            "step_id": "payment_details",
            "fields": [
                {"id": "demand_draft_number", "type": "string", "required": True},
                {"id": "demand_draft_bank", "type": "string", "required": True},
                {"id": "demand_draft_amount", "type": "number", "required": True},
                {"id": "demand_draft_date", "type": "date", "required": True},
            ],
        },
        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "demand_draft_uploaded", "type": "boolean", "required": True},
                {"id": "pan_card_uploaded", "type": "boolean", "required": True},
                {"id": "salary_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "photographs_uploaded", "type": "boolean", "required": True},
                {"id": "cancelled_cheque_uploaded", "type": "boolean", "required": True},
                {"id": "bank_passbook_copy_uploaded", "type": "boolean", "required": True},
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
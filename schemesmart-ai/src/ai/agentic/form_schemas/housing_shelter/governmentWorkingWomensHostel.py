governmentWorkingWomensHostel = {
    "scheme_id": "HOUSING_006",
    "scheme_name": "Government Working Women’s Hostel",
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
            ],
        },
        {
            "step_id": "employment_details",
            "fields": [
                {
                    "id": "is_working_woman",
                    "type": "boolean",
                    "required": True,
                },
                {"id": "employer_name", "type": "string", "required": True},
                {"id": "designation", "type": "string", "required": True},
                {
                    "id": "monthly_income",
                    "type": "number",
                    "required": True,
                },
                {
                    "id": "income_within_limit",
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
                    "options": ["tamil_nadu"],
                    "required": True,
                },
                {"id": "district", "type": "string", "required": True},
                {"id": "city_or_town", "type": "string", "required": True},
                {"id": "full_address", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "hostel_preferences",
            "fields": [
                {
                    "id": "preferred_city",
                    "type": "enum",
                    "options": ["chennai", "other_district"],
                    "required": True,
                },
                {
                    "id": "willing_to_stay_three_years",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "first_time_applicant",
                    "type": "boolean",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "verification_details",
            "fields": [
                {
                    "id": "csc_application",
                    "type": "boolean",
                    "required": False,
                },
                {
                    "id": "biometric_verification_completed",
                    "type": "boolean",
                    "required": False,
                },
            ],
        },
        {
            "step_id": "document_uploads",
            "fields": [
                {
                    "id": "employer_certificate_uploaded",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "income_certificate_uploaded",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "residence_certificate_uploaded",
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
            "step_id": "declaration",
            "fields": [
                {"id": "information_true", "type": "boolean", "required": True},
                {"id": "applicant_signature_name", "type": "string", "required": True},
                {"id": "submission_date", "type": "date", "required": True},
            ],
        },
    ],
}
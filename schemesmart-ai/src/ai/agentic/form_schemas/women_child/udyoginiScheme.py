udyoginiScheme = {
    "scheme_id": "WOMEN_CHILD_004",
    "scheme_name": "Udyogini Scheme",
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
            "step_id": "residency_details",
            "fields": [
                {"id": "state", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "address_line1", "type": "string", "required": True},
                {"id": "address_line2", "type": "string", "required": False},
                {"id": "pincode", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "income_and_category_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {
                    "id": "category",
                    "type": "enum",
                    "options": ["general", "sc", "st", "obc", "widow", "disabled"],
                    "required": True,
                },
                {"id": "income_within_limit", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "business_details",
            "fields": [
                {"id": "business_name", "type": "string", "required": True},
                {
                    "id": "business_type",
                    "type": "enum",
                    "options": [
                        "manufacturing",
                        "service",
                        "trading",
                        "agriculture_related",
                        "handicrafts",
                        "other",
                    ],
                    "required": True,
                },
                {"id": "project_cost", "type": "number", "required": True},
                {"id": "loan_amount_requested", "type": "number", "required": True},
                {"id": "project_report_submitted", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_name", "type": "string", "required": True},
                {"id": "bank_account_holder_name", "type": "string", "required": True},
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "aadhaar_linked", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "document_details",
            "fields": [
                {"id": "photographs_uploaded", "type": "boolean", "required": True},
                {"id": "project_report_uploaded", "type": "boolean", "required": True},
                {"id": "income_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "caste_certificate_uploaded", "type": "boolean", "required": False},
                {"id": "identity_proof_uploaded", "type": "boolean", "required": True},
                {"id": "machinery_quotation_uploaded", "type": "boolean", "required": False},
            ],
        },
    ],
}
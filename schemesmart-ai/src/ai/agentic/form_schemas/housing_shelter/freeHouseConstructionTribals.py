freeHouseConstructionTribals = {
    "scheme_id": "HOUSING_009",
    "scheme_name": "Construction of Free Houses for Tribals",
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
                {"id": "aadhaar_number", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "community_details",
            "fields": [
                {
                    "id": "community_category",
                    "type": "enum",
                    "options": ["sc", "st"],
                    "required": True,
                },
                {
                    "id": "caste_certificate_available",
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
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "full_address", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "land_and_house_details",
            "fields": [
                {
                    "id": "house_site_patta_available",
                    "type": "boolean",
                    "required": True,
                },
                {"id": "patta_number", "type": "string", "required": False},
                {"id": "land_location", "type": "string", "required": False},
                {
                    "id": "own_house_already",
                    "type": "boolean",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "family_details",
            "fields": [
                {
                    "id": "family_members_count",
                    "type": "number",
                    "required": True,
                },
                {
                    "id": "below_poverty_line",
                    "type": "boolean",
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
                {"id": "aadhaar_uploaded", "type": "boolean", "required": True},
                {
                    "id": "caste_certificate_uploaded",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "house_site_patta_uploaded",
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
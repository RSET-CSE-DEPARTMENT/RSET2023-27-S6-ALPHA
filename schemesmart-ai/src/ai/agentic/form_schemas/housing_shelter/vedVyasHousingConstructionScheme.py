vedVyasHousingConstructionScheme = {
    "scheme_id": "HOUSING_010",
    "scheme_name": "Ved-Vyas Housing Construction Scheme",
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
            "step_id": "occupation_details",
            "fields": [
                {
                    "id": "occupation",
                    "type": "enum",
                    "options": ["fish_farmer"],
                    "required": True,
                },
                {
                    "id": "fish_farming_certificate_available",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "years_of_fish_farming",
                    "type": "number",
                    "required": False,
                },
            ],
        },
        {
            "step_id": "economic_status_details",
            "fields": [
                {
                    "id": "below_poverty_line",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "income_certificate_available",
                    "type": "boolean",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "housing_condition_details",
            "fields": [
                {
                    "id": "current_house_type",
                    "type": "enum",
                    "options": ["kutcha", "thatched"],
                    "required": True,
                },
                {
                    "id": "kutcha_house_photo_available",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "owns_pucca_house",
                    "type": "boolean",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "land_ownership_details",
            "fields": [
                {
                    "id": "land_owned",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "land_ownership_documents_available",
                    "type": "boolean",
                    "required": True,
                },
                {"id": "land_location", "type": "string", "required": False},
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
                    "id": "applicant_photograph_uploaded",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "kutcha_house_photograph_uploaded",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "income_certificate_uploaded",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "land_ownership_documents_uploaded",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "fish_farming_certificate_uploaded",
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
sportsHostelRajasthan = {
    "scheme_id": "HOUSING_016",
    "scheme_name": "Operation of Sports Hostels",
    "form_steps": [
        {
            "step_id": "student_personal_information",
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
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "jan_aadhaar_number", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "community_details",
            "fields": [
                {
                    "id": "community_category",
                    "type": "enum",
                    "options": ["scheduled_tribe"],
                    "required": True
                },
                {
                    "id": "caste_certificate_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "education_details",
            "fields": [
                {
                    "id": "current_class",
                    "type": "enum",
                    "options": [
                        "class_6",
                        "class_7",
                        "class_8",
                        "class_9",
                        "class_10",
                        "class_11",
                        "class_12"
                    ],
                    "required": True
                },
                {
                    "id": "institution_name",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "marksheet_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "sports_selection_details",
            "fields": [
                {
                    "id": "passed_selection_test",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "sport_specialization",
                    "type": "string",
                    "required": False
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
                    "options": ["rajasthan"],
                    "required": True
                },
                {"id": "district", "type": "string", "required": True},
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "full_address", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "economic_details",
            "fields": [
                {
                    "id": "income_certificate_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "aadhaar_uploaded", "type": "boolean", "required": True},
                {"id": "jan_aadhaar_uploaded", "type": "boolean", "required": True},
                {"id": "caste_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "income_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "marksheet_uploaded", "type": "boolean", "required": True}
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
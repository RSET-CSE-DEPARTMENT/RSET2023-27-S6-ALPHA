scHostelMP = {
    "scheme_id": "HOUSING_013",
    "scheme_name": "Running of Scheduled Caste Hostel",
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
                {"id": "samagra_id", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "community_details",
            "fields": [
                {
                    "id": "community_category",
                    "type": "enum",
                    "options": ["scheduled_caste"],
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
                    "id": "currently_enrolled",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "education_level",
                    "type": "enum",
                    "options": [
                        "school",
                        "higher_secondary",
                        "undergraduate",
                        "postgraduate"
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
                    "options": ["madhya_pradesh"],
                    "required": True
                },
                {"id": "district", "type": "string", "required": True},
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "full_address", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "hostel_requirement_details",
            "fields": [
                {
                    "id": "requires_hostel_accommodation",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "distance_from_institution_km",
                    "type": "number",
                    "required": False
                }
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
                    "id": "aadhaar_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "domicile_certificate_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "caste_certificate_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "marksheet_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "samagra_id_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "bank_details_uploaded",
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
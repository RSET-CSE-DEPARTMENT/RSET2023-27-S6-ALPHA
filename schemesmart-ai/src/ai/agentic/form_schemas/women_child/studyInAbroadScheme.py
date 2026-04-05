studyInAbroadScheme = {
    "scheme_id": "WOMEN_CHILD_011",
    "scheme_name": "Scheme For Study In Abroad",
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
                {"id": "email", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "education_details",
            "fields": [
                {"id": "is_student", "type": "boolean", "required": True},
                {"id": "school_name", "type": "string", "required": True},
                {
                    "id": "school_type",
                    "type": "enum",
                    "options": ["government_school"],
                    "required": True,
                },
                {
                    "id": "board",
                    "type": "enum",
                    "options": ["rbse"],
                    "required": True,
                },
                {"id": "class_10_percentage", "type": "number", "required": True},
                {"id": "class_12_percentage", "type": "number", "required": False},
                {
                    "id": "state_rank_top_three",
                    "type": "boolean",
                    "required": True,
                },
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
                {"id": "domicile_certificate_available", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "study_abroad_details",
            "fields": [
                {"id": "intended_course", "type": "string", "required": True},
                {"id": "preferred_country", "type": "string", "required": True},
                {"id": "university_applied", "type": "boolean", "required": False},
                {"id": "sat_coaching_taken", "type": "boolean", "required": False},
                {"id": "sat_registration_completed", "type": "boolean", "required": False},
            ],
        },
        {
            "step_id": "guardian_details",
            "fields": [
                {"id": "guardian_name", "type": "string", "required": True},
                {"id": "guardian_relationship", "type": "string", "required": True},
                {"id": "guardian_mobile_number", "type": "string", "required": True},
                {"id": "parental_consent_available", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "document_details",
            "fields": [
                {"id": "aadhaar_card_uploaded", "type": "boolean", "required": True},
                {"id": "age_proof_uploaded", "type": "boolean", "required": True},
                {"id": "address_proof_uploaded", "type": "boolean", "required": True},
                {"id": "domicile_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "class_10_marksheet_uploaded", "type": "boolean", "required": True},
                {"id": "class_12_marksheet_uploaded", "type": "boolean", "required": False},
                {"id": "passport_uploaded", "type": "boolean", "required": True},
            ],
        },
    ],
}
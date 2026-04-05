residentialSchoolForBlinds = {
    "scheme_id": "HOUSING_002",
    "scheme_name": "Residential School For Blinds",
    "form_steps": [
        {
            "step_id": "student_personal_information",
            "fields": [
                {"id": "student_full_name", "type": "string", "required": True},
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
            "step_id": "guardian_information",
            "fields": [
                {"id": "guardian_name", "type": "string", "required": True},
                {
                    "id": "guardian_relationship",
                    "type": "enum",
                    "options": ["father", "mother", "guardian", "relative"],
                    "required": True,
                },
                {"id": "guardian_mobile_number", "type": "string", "required": True},
                {"id": "guardian_address", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "disability_details",
            "fields": [
                {
                    "id": "disability_type",
                    "type": "enum",
                    "options": ["total_blindness", "partial_blindness"],
                    "required": True,
                },
                {"id": "disability_percentage", "type": "number", "required": True},
                {
                    "id": "disability_certificate_number",
                    "type": "string",
                    "required": True,
                },
                {
                    "id": "issuing_medical_authority",
                    "type": "string",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "education_details",
            "fields": [
                {"id": "currently_studying", "type": "boolean", "required": True},
                {"id": "last_class_completed", "type": "string", "required": False},
                {"id": "previous_school_name", "type": "string", "required": False},
                {
                    "id": "willing_for_residential_school",
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
                    "options": ["jammu_and_kashmir"],
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
                {"id": "aadhaar_linked", "type": "boolean", "required": False},
            ],
        },
        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "domicile_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "disability_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "passport_photos_uploaded", "type": "boolean", "required": True},
                {"id": "aadhaar_uploaded", "type": "boolean", "required": True},
                {"id": "age_proof_uploaded", "type": "boolean", "required": True},
                {"id": "educational_certificates_uploaded", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "declaration",
            "fields": [
                {"id": "information_true", "type": "boolean", "required": True},
                {"id": "guardian_signature_name", "type": "string", "required": True},
                {"id": "submission_date", "type": "date", "required": True},
            ],
        },
    ],
}
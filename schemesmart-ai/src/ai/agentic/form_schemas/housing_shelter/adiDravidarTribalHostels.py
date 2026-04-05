adiDravidarTribalHostels = {
    "scheme_id": "HOUSING_007",
    "scheme_name": "Adi Dravidar and Tribal Welfare Department Hostels",
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
            "step_id": "community_details",
            "fields": [
                {
                    "id": "community_category",
                    "type": "enum",
                    "options": ["adi_dravidar", "tribal"],
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
            "step_id": "education_details",
            "fields": [
                {
                    "id": "currently_studying",
                    "type": "boolean",
                    "required": True,
                },
                {"id": "current_class", "type": "string", "required": True},
                {
                    "id": "education_level",
                    "type": "enum",
                    "options": [
                        "primary",
                        "middle_school",
                        "secondary",
                        "higher_secondary"
                    ],
                    "required": True,
                },
                {"id": "school_name", "type": "string", "required": True},
                {
                    "id": "school_enrollment_proof_available",
                    "type": "boolean",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "guardian_information",
            "fields": [
                {"id": "guardian_name", "type": "string", "required": True},
                {
                    "id": "guardian_relationship",
                    "type": "enum",
                    "options": ["father", "mother", "guardian"],
                    "required": True,
                },
                {"id": "guardian_mobile_number", "type": "string", "required": True},
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
            "step_id": "hostel_application_details",
            "fields": [
                {
                    "id": "contacted_hostel_warden",
                    "type": "boolean",
                    "required": True,
                },
                {"id": "preferred_hostel_name", "type": "string", "required": False},
                {
                    "id": "first_time_hostel_applicant",
                    "type": "boolean",
                    "required": True,
                },
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
                    "id": "income_certificate_uploaded",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "school_enrollment_proof_uploaded",
                    "type": "boolean",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_holder_name", "type": "string", "required": False},
                {"id": "bank_account_number", "type": "string", "required": False},
                {"id": "bank_ifsc", "type": "string", "required": False},
                {"id": "bank_name", "type": "string", "required": False},
                {"id": "branch_name", "type": "string", "required": False},
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
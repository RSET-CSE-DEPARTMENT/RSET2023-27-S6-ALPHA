savitribaiPhuleSingleGirlPhd = {
    "scheme_id": "WOMEN_CHILD_003",
    "scheme_name": "Savitribai Jyotirao Phule Fellowship for Single Girl Child",
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
                {"id": "single_girl_child_affidavit_available", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "phd_program_details",
            "fields": [
                {"id": "phd_program_name", "type": "string", "required": True},
                {"id": "research_field", "type": "string", "required": True},
                {"id": "university_name", "type": "string", "required": True},
                {
                    "id": "institution_type",
                    "type": "enum",
                    "options": ["central_university", "state_university", "deemed_university", "private_university"],
                    "required": True,
                },
                {
                    "id": "phd_mode",
                    "type": "enum",
                    "options": ["full_time"],
                    "required": True,
                },
                {
                    "id": "phd_admission_status",
                    "type": "enum",
                    "options": ["admitted", "provisional_admission"],
                    "required": True,
                },
                {"id": "phd_start_year", "type": "number", "required": True},
            ],
        },
        {
            "step_id": "academic_qualification",
            "fields": [
                {"id": "masters_degree_subject", "type": "string", "required": True},
                {"id": "masters_university", "type": "string", "required": True},
                {"id": "masters_passing_year", "type": "number", "required": True},
                {"id": "masters_percentage_or_cgpa", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "category_and_age_details",
            "fields": [
                {
                    "id": "category",
                    "type": "enum",
                    "options": ["general", "sc", "st", "obc", "ews"],
                    "required": True,
                },
                {"id": "age_within_limit", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "research_details",
            "fields": [
                {"id": "research_proposal_title", "type": "string", "required": True},
                {"id": "research_proposal_submitted", "type": "boolean", "required": True},
                {"id": "research_supervisor_name", "type": "string", "required": True},
                {"id": "research_department", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "document_details",
            "fields": [
                {"id": "photograph_uploaded", "type": "boolean", "required": True},
                {"id": "signature_uploaded", "type": "boolean", "required": True},
                {"id": "degree_certificates_uploaded", "type": "boolean", "required": True},
                {"id": "application_form_signed", "type": "boolean", "required": True},
            ],
        },
    ],
}
# src/ai/agentic/form_schemas/education/sjpFellowship.py

sjpFellowship = {
    "scheme_id": "EDU_SCH_003",
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
                {"id": "pan_card", "type": "string", "required": True},
                {
                    "id": "family_status",
                    "type": "enum",
                    "options": ["single_girl_child", "twins"],
                    "required": True,
                },
                {"id": "affidavit_single_girl_child", "type": "file", "required": True},
            ],
        },
        {
            "step_id": "education_details",
            "fields": [
                {"id": "is_student", "type": "boolean", "required": True},
                {
                    "id": "program",
                    "type": "enum",
                    "options": ["full_time_phd"],
                    "required": True,
                },
                {"id": "university_name", "type": "string", "required": True},
                {
                    "id": "institution_type",
                    "type": "enum",
                    "options": ["government", "private", "aided"],
                    "required": True,
                },
                {"id": "research_proposal", "type": "file", "required": True},
            ],
        },
        {
            "step_id": "fellowship_details",
            "fields": [
                {
                    "id": "fellowship_type",
                    "type": "enum",
                    "options": ["JRF", "SRF"],
                    "required": True,
                },
                {"id": "contingency_category", "type": "enum",
                 "options": ["humanities_social_sciences", "science_engineering"],
                 "required": True},
                {"id": "escort_reader_needed", "type": "boolean", "required": False},
                {"id": "hra_applicable", "type": "boolean", "required": False},
            ],
        },
        {
            "step_id": "age_eligibility",
            "fields": [
                {"id": "age_limit_general", "type": "number", "required": True},
                {"id": "age_limit_sc_st_obc_pwd", "type": "number", "required": True},
            ],
        },
        {
            "step_id": "exclusions_acknowledgement",
            "fields": [
                {"id": "acknowledge_part_time_distance", "type": "boolean", "required": True},
                {"id": "acknowledge_no_siblings", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "documents_upload",
            "fields": [
                {"id": "photograph", "type": "file", "required": True},
                {"id": "signature", "type": "file", "required": True},
                {"id": "signed_application_form", "type": "file", "required": True},
            ],
        },
        {
            "step_id": "acknowledgements",
            "fields": [
                {"id": "agree_terms", "type": "boolean", "required": True},
                {"id": "signature_applicant", "type": "string", "required": True},
                {"id": "date_of_submission", "type": "date", "required": True},
            ],
        },
    ],
}
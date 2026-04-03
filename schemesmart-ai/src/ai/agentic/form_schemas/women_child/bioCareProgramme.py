bioCareProgramme = {
    "scheme_id": "WOMEN_CHILD_008",
    "scheme_name": "Biotechnology Career Advancement and Re-orientation (BioCARe) Programme",
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
            "step_id": "education_and_qualification",
            "fields": [
                {
                    "id": "highest_qualification",
                    "type": "enum",
                    "options": ["phd", "mtech", "mpharma"],
                    "required": True,
                },
                {"id": "specialization", "type": "string", "required": True},
                {"id": "university_name", "type": "string", "required": True},
                {"id": "year_of_completion", "type": "number", "required": True},
                {"id": "degree_certificates_available", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "employment_status",
            "fields": [
                {"id": "currently_employed", "type": "boolean", "required": True},
                {
                    "id": "career_break",
                    "type": "enum",
                    "options": ["yes", "no"],
                    "required": True,
                },
                {"id": "years_of_research_experience", "type": "number", "required": False},
            ],
        },
        {
            "step_id": "research_project_details",
            "fields": [
                {"id": "research_project_title", "type": "string", "required": True},
                {"id": "research_area", "type": "string", "required": True},
                {"id": "research_proposal_submitted", "type": "boolean", "required": True},
                {"id": "expected_project_duration_years", "type": "number", "required": True},
            ],
        },
        {
            "step_id": "mentor_and_institution_details",
            "fields": [
                {"id": "mentor_name", "type": "string", "required": True},
                {"id": "mentor_designation", "type": "string", "required": True},
                {"id": "host_institution_name", "type": "string", "required": True},
                {"id": "host_institution_department", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "publication_details",
            "fields": [
                {"id": "number_of_publications", "type": "number", "required": False},
                {"id": "publication_record_submitted", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "document_details",
            "fields": [
                {"id": "aadhaar_card_uploaded", "type": "boolean", "required": True},
                {"id": "degree_certificates_uploaded", "type": "boolean", "required": True},
                {"id": "research_proposal_uploaded", "type": "boolean", "required": True},
                {"id": "mentor_details_uploaded", "type": "boolean", "required": True},
                {"id": "publications_record_uploaded", "type": "boolean", "required": True},
            ],
        },
    ],
}
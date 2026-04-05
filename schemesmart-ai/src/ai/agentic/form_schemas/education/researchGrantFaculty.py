# src/ai/agentic/form_schemas/education/researchGrantFaculty.py

researchGrantFaculty = {
    "scheme_id": "EDU_SCH_006",
    "scheme_name": "Research Grant for In-Service Faculty Members",
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
                    "options": ["male", "female", "other"],
                    "required": False,
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "employee_id", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "professional_details",
            "fields": [
                {"id": "designation", "type": "string", "required": True},
                {"id": "department", "type": "string", "required": True},
                {"id": "institution_name", "type": "string", "required": True},
                {
                    "id": "institution_type",
                    "type": "enum",
                    "options": ["government", "private", "aided"],
                    "required": True,
                },
                {"id": "years_of_service", "type": "number", "required": True},
                {"id": "phd_scholars_guided", "type": "number", "required": True},
                {"id": "sponsored_projects_completed", "type": "number", "required": True},
            ],
        },
        {
            "step_id": "grant_details",
            "fields": [
                {"id": "grant_amount", "type": "string", "required": True},
                {"id": "tenure_years", "type": "number", "required": True},
            ],
        },
        {
            "step_id": "eligibility_acknowledgement",
            "fields": [
                {
                    "id": "age_below_50",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "minimum_service_10_years",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "research_experience_met",
                    "type": "boolean",
                    "required": True,
                },
            ],
        },
        {
            "step_id": "application_process",
            "fields": [
                {"id": "mode_online", "type": "boolean", "required": True},
                {"id": "portal_url", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "documents_upload",
            "fields": [
                {"id": "aadhaar_card_file", "type": "file", "required": True},
                {"id": "employment_proof", "type": "file", "required": True},
                {"id": "research_experience_certificate", "type": "file", "required": True},
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
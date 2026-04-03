# src/ai/agentic/form_schemas/research/biocareWomenScientists.py

bioCareWomenScientists = {
    "scheme_id": "EDU_SCH_017",
    "scheme_name": "Biotechnology Career Advancement and Re-orientation (BioCARe)",
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
                    "required": True
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "mobile_number", "type": "string", "required": True},
                {"id": "email_id", "type": "string", "required": True},
                {"id": "nationality", "type": "string", "required": True}
            ],
        },

        {
            "step_id": "residence_details",
            "fields": [
                {"id": "state", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "city_or_town", "type": "string", "required": True},
                {"id": "address", "type": "string", "required": True},
                {"id": "pincode", "type": "string", "required": True}
            ],
        },

        {
            "step_id": "education_details",
            "fields": [
                {
                    "id": "highest_qualification",
                    "type": "enum",
                    "options": ["phd", "mtech", "mpharma", "mvsc", "md", "mds"],
                    "required": True
                },
                {"id": "specialization", "type": "string", "required": True},
                {"id": "university_name", "type": "string", "required": True},
                {"id": "year_of_completion", "type": "number", "required": True},
                {"id": "research_experience_years", "type": "number", "required": False}
            ],
        },

        {
            "step_id": "employment_status",
            "fields": [
                {
                    "id": "current_employment_status",
                    "type": "enum",
                    "options": ["unemployed"],
                    "required": True
                },
                {"id": "career_break_reason", "type": "string", "required": False},
                {"id": "career_break_duration_years", "type": "number", "required": False}
            ],
        },

        {
            "step_id": "research_project_details",
            "fields": [
                {"id": "research_project_title", "type": "string", "required": True},
                {"id": "research_area", "type": "string", "required": True},
                {"id": "research_objectives", "type": "string", "required": True},
                {"id": "research_duration_years", "type": "number", "required": True},
                {
                    "id": "funding_category",
                    "type": "enum",
                    "options": ["category_I", "category_II"],
                    "required": True
                }
            ],
        },

        {
            "step_id": "mentor_details",
            "fields": [
                {"id": "mentor_name", "type": "string", "required": True},
                {"id": "mentor_designation", "type": "string", "required": True},
                {"id": "mentor_institution", "type": "string", "required": True},
                {"id": "mentor_email", "type": "string", "required": True},
                {"id": "mentor_mobile", "type": "string", "required": False}
            ],
        },

        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_holder_name", "type": "string", "required": True},
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_name", "type": "string", "required": True},
                {"id": "branch_name", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "aadhaar_linked", "type": "boolean", "required": False}
            ],
        },

        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "educational_certificates", "type": "file", "required": True},
                {"id": "research_proposal_document", "type": "file", "required": True},
                {"id": "mentor_consent_letter", "type": "file", "required": True},
                {"id": "identity_proof", "type": "file", "required": True},
                {"id": "applicant_photograph", "type": "file", "required": False}
            ],
        },

        {
            "step_id": "declaration",
            "fields": [
                {"id": "applicant_declaration", "type": "boolean", "required": True},
                {"id": "place_of_application", "type": "string", "required": True},
                {"id": "date_of_application", "type": "date", "required": True},
                {"id": "applicant_signature", "type": "string", "required": True}
            ],
        }

    ],
}
backToLabPostDoctoralFellowship = {
    "scheme_id": "WOMEN_CHILD_016",
    "scheme_name": "Back-To-Lab Post-Doctoral Fellowship Programme",
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
                {"id": "email", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "education_details",
            "fields": [
                {
                    "id": "phd_completed",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "phd_field",
                    "type": "enum",
                    "options": ["science", "engineering"],
                    "required": True
                },
                {"id": "phd_university", "type": "string", "required": True},
                {"id": "pg_degree_completed", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "career_break_details",
            "fields": [
                {"id": "career_break_taken", "type": "boolean", "required": True},
                {
                    "id": "career_break_reason",
                    "type": "enum",
                    "options": ["family_reasons", "maternity", "child_care", "other"],
                    "required": True
                },
                {"id": "career_break_certificate_available", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "research_details",
            "fields": [
                {"id": "research_area", "type": "string", "required": True},
                {"id": "mentor_name", "type": "string", "required": True},
                {"id": "mentor_institution", "type": "string", "required": True},
                {"id": "mentor_consent_available", "type": "boolean", "required": True},
                {"id": "research_publications_available", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "residency_details",
            "fields": [
                {"id": "state", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "address_line1", "type": "string", "required": True},
                {"id": "address_line2", "type": "string", "required": False},
                {"id": "pincode", "type": "string", "required": True},
                {"id": "residency_proof_available", "type": "boolean", "required": True}
            ]
        },
        {
            "step_id": "document_details",
            "fields": [
                {"id": "aadhaar_card_uploaded", "type": "boolean", "required": True},
                {"id": "residency_proof_uploaded", "type": "boolean", "required": True},
                {"id": "pg_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "phd_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "research_publications_uploaded", "type": "boolean", "required": True},
                {"id": "career_break_certificate_uploaded", "type": "boolean", "required": True},
                {"id": "mentor_consent_letter_uploaded", "type": "boolean", "required": True}
            ]
        }
    ]
}
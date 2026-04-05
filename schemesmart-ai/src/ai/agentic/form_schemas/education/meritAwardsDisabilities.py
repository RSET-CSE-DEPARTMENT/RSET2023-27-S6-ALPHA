# src/ai/agentic/form_schemas/education/meritAwardsDisabilities.py

meritAwardsDisabilities = {
    "scheme_id": "EDU_SCH_013",
    "scheme_name": "Merit Awards for Students with Disabilities",
    "form_steps": [
        {
            "step_id": "personal_information",
            "fields": [
                {"id": "full_name", "type": "string", "required": True},
                {"id": "date_of_birth", "type": "date", "required": True},
                {"id": "age", "type": "number", "required": True},
                {"id": "gender", "type": "enum", "options": ["male", "female", "other"], "required": True},
                {"id": "residence_state", "type": "enum", "options": ["Maharashtra"], "required": True},
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "disability_type", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "education_achievement",
            "fields": [
                {"id": "exam_type", "type": "enum", "options": ["SSC", "HSC"], "required": True},
                {"id": "rank_obtained", "type": "number", "required": True},
                {"id": "school_name", "type": "string", "required": True},
                {"id": "institution_type", "type": "enum", "options": ["government", "private"], "required": True},
            ],
        },
        {
            "step_id": "documents_upload",
            "fields": [
                {"id": "disability_certificate", "type": "file", "required": True},
                {"id": "mark_sheets", "type": "file", "required": True},
                {"id": "bonafide_certificate", "type": "file", "required": True},
                {"id": "aadhaar_card", "type": "file", "required": True},
                {"id": "domicile_certificate", "type": "file", "required": True},
                {"id": "bank_details", "type": "file", "required": True},
            ],
        },
        {
            "step_id": "benefit_details",
            "fields": [
                {"id": "cash_award_amount", "type": "number", "required": True, "default": 1000},
                {"id": "certificate_awarded", "type": "boolean", "required": True, "default": True},
                {"id": "travel_allowance", "type": "number", "required": False, "default": 100},
            ],
        },
        {
            "step_id": "acknowledgement",
            "fields": [
                {"id": "agree_terms", "type": "boolean", "required": True},
                {"id": "signature_applicant", "type": "string", "required": True},
                {"id": "date_of_submission", "type": "date", "required": True},
            ],
        },
    ],
}
# src/ai/agentic/form_schemas/education/postMatricReal.py

postMatricReal = {
    "scheme_id": "EDU_SCH_007",
    "scheme_name": "Post Matric Scholarship for SC/ST Students",
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
                    "required": True,
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
                {
                    "id": "caste_category",
                    "type": "enum",
                    "options": ["general", "obc", "sc", "st"],
                    "required": True,
                },
            ],
        },
        {
            "step_id": "education_details",
            "fields": [
                {"id": "is_student", "type": "boolean", "required": True},
                {
                    "id": "course_level",
                    "type": "enum",
                    "options": ["ug", "pg"],
                    "required": True,
                },
                {
                    "id": "institution_type",
                    "type": "enum",
                    "options": ["government", "private", "aided"],
                    "required": True,
                },
                {"id": "university_name", "type": "string", "required": True},
                {
                    "id": "admission_status",
                    "type": "enum",
                    "options": ["admitted"],
                    "required": True,
                },
            ],
        },
        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {"id": "bpl_status", "type": "boolean", "required": False},
            ],
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "aadhaar_linked", "type": "boolean", "required": True},
            ],
        },
    ],
}
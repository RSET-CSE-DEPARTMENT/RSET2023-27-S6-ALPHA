# src/ai/agentic/form_schemas/education/icarJrf.py

icarJrf = {
    "scheme_id": "EDU_SCH_004",
    "scheme_name": "ICAR Junior Research Fellowship (PGS)",
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
                {"id": "government_id", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "educational_qualification",
            "fields": [
                {"id": "bachelor_degree_discipline", "type": "string", "required": True},
                {"id": "minimum_marks", "type": "number", "required": True},
                {"id": "institution_name", "type": "string", "required": True},
                {
                    "id": "course_type",
                    "type": "enum",
                    "options": ["bachelor", "bachelor_diploma"],
                    "required": True,
                },
            ],
        },
        {
            "step_id": "selection_process_acknowledgement",
            "fields": [
                {
                    "id": "selection_based_on_icar_exam",
                    "type": "boolean",
                    "required": True,
                }
            ],
        },
        {
            "step_id": "fellowship_details",
            "fields": [
                {
                    "id": "discipline_category",
                    "type": "enum",
                    "options": ["veterinary_sciences", "other_disciplines"],
                    "required": True,
                },
                {"id": "fellowship_amount", "type": "string", "required": True},
                {"id": "contingency_amount", "type": "string", "required": True},
                {"id": "tenure_years", "type": "number", "required": True},
            ],
        },
        {
            "step_id": "application_process",
            "fields": [
                {"id": "registration_done_online", "type": "boolean", "required": True},
                {"id": "application_fee_paid", "type": "boolean", "required": True},
                {"id": "hard_copy_sent_by_post", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "documents_upload",
            "fields": [
                {"id": "photograph", "type": "file", "required": True},
                {"id": "signature", "type": "file", "required": True},
                {"id": "thumb_impression", "type": "file", "required": True},
                {"id": "government_id_file", "type": "file", "required": True},
                {"id": "fee_payment_receipt", "type": "file", "required": True},
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
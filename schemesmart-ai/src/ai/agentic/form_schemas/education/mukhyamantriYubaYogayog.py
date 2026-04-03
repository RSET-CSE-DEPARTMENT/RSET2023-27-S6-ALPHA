# src/ai/agentic/form_schemas/education/mukhyamantriYubaYogayog.py

mukhyamantriYubaYogayog = {
    "scheme_id": "EDU_SCH_014",
    "scheme_name": "Mukhyamantri Yuba Yogayog Yojana – Special",
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
                    "required": True
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "mobile_number", "type": "string", "required": True},
                {"id": "email_id", "type": "string", "required": False},
            ],
        },
        {
            "step_id": "residence_details",
            "fields": [
                {"id": "state", "type": "enum", "options": ["Tripura"], "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "address", "type": "string", "required": True},
                {"id": "pincode", "type": "string", "required": True},
                {"id": "ration_card_number", "type": "string", "required": True},
                {"id": "ration_card_holder", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "education_details",
            "fields": [
                {"id": "is_student", "type": "boolean", "required": True},
                {
                    "id": "course_level",
                    "type": "enum",
                    "options": ["undergraduate"],
                    "required": True,
                },
                {
                    "id": "course_year",
                    "type": "enum",
                    "options": ["final_year"],
                    "required": True,
                },
                {
                    "id": "institution_type",
                    "type": "enum",
                    "options": ["government"],
                    "required": True,
                },
                {"id": "institution_name", "type": "string", "required": True},
                {"id": "university_name", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "smartphone_purchase_details",
            "fields": [
                {"id": "mobile_brand", "type": "string", "required": True},
                {"id": "mobile_model", "type": "string", "required": True},
                {"id": "invoice_number", "type": "string", "required": True},
                {"id": "invoice_date", "type": "date", "required": True},
                {"id": "mobile_cost", "type": "number", "required": True},
            ],
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "bank_name", "type": "string", "required": True},
                {"id": "aadhaar_linked", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "documents_upload",
            "fields": [
                {"id": "mobile_invoice", "type": "file", "required": True},
                {"id": "final_year_marksheet", "type": "file", "required": True},
                {"id": "bank_passbook_copy", "type": "file", "required": True},
                {"id": "ration_card_copy", "type": "file", "required": True},
                {"id": "applicant_photograph", "type": "file", "required": True},
            ],
        },
        {
            "step_id": "declaration",
            "fields": [
                {"id": "agree_terms", "type": "boolean", "required": True},
                {"id": "signature_applicant", "type": "string", "required": True},
                {"id": "date_of_submission", "type": "date", "required": True},
            ],
        },
    ],
}
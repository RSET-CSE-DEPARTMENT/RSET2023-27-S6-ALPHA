# src/ai/agentic/form_schemas/education/biharStudentCreditCard.py

biharStudentCreditCard = {
    "scheme_id": "EDU_SCH_018",
    "scheme_name": "Bihar Student Credit Card Scheme",
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
                    "options": ["male", "female", "transgender"],
                    "required": True
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "pan_number", "type": "string", "required": False},
                {"id": "mobile_number", "type": "string", "required": True},
                {"id": "email_id", "type": "string", "required": True}
            ],
        },

        {
            "step_id": "residence_details",
            "fields": [
                {"id": "state", "type": "enum", "options": ["bihar"], "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "block", "type": "string", "required": True},
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "address", "type": "string", "required": True},
                {"id": "pincode", "type": "string", "required": True}
            ],
        },

        {
            "step_id": "guardian_details",
            "fields": [
                {"id": "father_name", "type": "string", "required": True},
                {"id": "mother_name", "type": "string", "required": False},
                {"id": "guardian_name", "type": "string", "required": False},
                {"id": "guardian_mobile_number", "type": "string", "required": True},
                {"id": "guardian_occupation", "type": "string", "required": False}
            ],
        },

        {
            "step_id": "education_details",
            "fields": [
                {"id": "is_student", "type": "boolean", "required": True},
                {
                    "id": "highest_qualification",
                    "type": "enum",
                    "options": ["class_12_pass"],
                    "required": True
                },
                {"id": "board_name", "type": "string", "required": True},
                {"id": "year_of_passing", "type": "number", "required": True},
                {"id": "percentage_or_grade", "type": "string", "required": True}
            ],
        },

        {
            "step_id": "course_admission_details",
            "fields": [
                {"id": "course_name", "type": "string", "required": True},
                {
                    "id": "course_level",
                    "type": "enum",
                    "options": ["diploma", "ug", "pg", "professional"],
                    "required": True
                },
                {"id": "institution_name", "type": "string", "required": True},
                {
                    "id": "institution_type",
                    "type": "enum",
                    "options": ["government", "private", "recognized"],
                    "required": True
                },
                {"id": "university_or_board", "type": "string", "required": True},
                {"id": "admission_status", "type": "enum", "options": ["admitted"], "required": True},
                {"id": "course_duration_years", "type": "number", "required": True}
            ],
        },

        {
            "step_id": "loan_details",
            "fields": [
                {"id": "loan_amount_requested", "type": "number", "required": True},
                {
                    "id": "loan_purpose",
                    "type": "enum",
                    "options": [
                        "tuition_fee",
                        "hostel_fee",
                        "books_and_materials",
                        "other_academic_expenses"
                    ],
                    "required": True
                },
                {
                    "id": "special_category",
                    "type": "enum",
                    "options": ["general", "girl_student", "divyang", "transgender"],
                    "required": True
                }
            ],
        },

        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {"id": "income_certificate_available", "type": "boolean", "required": True},
                {"id": "bpl_status", "type": "boolean", "required": False}
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
                {"id": "aadhaar_linked", "type": "boolean", "required": True}
            ],
        },

        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "aadhaar_card", "type": "file", "required": True},
                {"id": "pan_card", "type": "file", "required": False},
                {"id": "class_12_marksheet", "type": "file", "required": True},
                {"id": "admission_letter", "type": "file", "required": True},
                {"id": "income_certificate", "type": "file", "required": True},
                {"id": "bank_statement", "type": "file", "required": True}
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
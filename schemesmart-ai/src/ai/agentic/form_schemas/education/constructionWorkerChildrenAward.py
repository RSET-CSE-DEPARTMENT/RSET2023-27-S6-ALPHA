# src/ai/agentic/form_schemas/education/constructionWorkerChildrenAward.py

constructionWorkerChildrenAward = {
    "scheme_id": "EDU_SCH_016",
    "scheme_name": "Cash Award for Children of Construction Workers",
    "form_steps": [

        {
            "step_id": "worker_details",
            "fields": [
                {"id": "worker_full_name", "type": "string", "required": True},
                {"id": "worker_registration_number", "type": "string", "required": True},
                {"id": "worker_registration_valid", "type": "boolean", "required": True},
                {"id": "worker_mobile_number", "type": "string", "required": True},
                {"id": "worker_identity_proof_number", "type": "string", "required": True}
            ]
        },

        {
            "step_id": "student_information",
            "fields": [
                {"id": "student_full_name", "type": "string", "required": True},
                {"id": "father_or_guardian_name", "type": "string", "required": True},
                {"id": "date_of_birth", "type": "date", "required": True},
                {"id": "age", "type": "number", "required": True},
                {
                    "id": "gender",
                    "type": "enum",
                    "options": ["male", "female", "other"],
                    "required": True
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "student_mobile_number", "type": "string", "required": False}
            ]
        },

        {
            "step_id": "residence_details",
            "fields": [
                {
                    "id": "state",
                    "type": "enum",
                    "options": ["Arunachal Pradesh"],
                    "required": True
                },
                {"id": "district", "type": "string", "required": True},
                {"id": "village_or_town", "type": "string", "required": True},
                {"id": "address", "type": "string", "required": True},
                {"id": "pincode", "type": "string", "required": True}
            ]
        },

        {
            "step_id": "education_details",
            "fields": [
                {"id": "is_student", "type": "boolean", "required": True},
                {
                    "id": "qualification_passed",
                    "type": "enum",
                    "options": ["class_10", "class_12"],
                    "required": True
                },
                {"id": "school_or_college_name", "type": "string", "required": True},
                {"id": "board_or_university", "type": "string", "required": True},
                {"id": "year_of_passing", "type": "number", "required": True},
                {"id": "percentage_or_grade", "type": "string", "required": True}
            ]
        },

        {
            "step_id": "award_category",
            "fields": [
                {
                    "id": "award_amount_category",
                    "type": "enum",
                    "options": ["500", "750", "1000"],
                    "required": True
                }
            ]
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
            ]
        },

        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "worker_registration_card", "type": "file", "required": True},
                {"id": "student_marksheet", "type": "file", "required": True},
                {"id": "bank_passbook_copy", "type": "file", "required": True},
                {"id": "identity_proof", "type": "file", "required": True},
                {"id": "student_photograph", "type": "file", "required": True}
            ]
        },

        {
            "step_id": "declaration",
            "fields": [
                {"id": "applicant_declaration", "type": "boolean", "required": True},
                {"id": "place_of_application", "type": "string", "required": True},
                {"id": "date_of_application", "type": "date", "required": True},
                {"id": "applicant_signature", "type": "string", "required": True}
            ]
        }
    ]
}
# src/ai/agentic/form_schemas/education/oecPreMatricAssistance.py

oecPreMatricAssistance = {
    "scheme_id": "EDU_SCH_019",
    "scheme_name": "OEC Pre-matric Educational Assistance",
    "form_steps": [

        {
            "step_id": "student_personal_information",
            "fields": [
                {"id": "student_full_name", "type": "string", "required": True},
                {"id": "date_of_birth", "type": "date", "required": True},
                {"id": "age", "type": "number", "required": True},
                {
                    "id": "gender",
                    "type": "enum",
                    "options": ["male", "female", "other"],
                    "required": True
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "student_mobile_number", "type": "string", "required": False},
                {"id": "student_email", "type": "string", "required": False}
            ],
        },

        {
            "step_id": "parent_guardian_details",
            "fields": [
                {"id": "father_name", "type": "string", "required": True},
                {"id": "mother_name", "type": "string", "required": False},
                {"id": "guardian_name", "type": "string", "required": False},
                {"id": "guardian_mobile_number", "type": "string", "required": True},
                {"id": "guardian_occupation", "type": "string", "required": False}
            ],
        },

        {
            "step_id": "community_details",
            "fields": [
                {
                    "id": "community_category",
                    "type": "enum",
                    "options": ["oec", "other_equivalent_community"],
                    "required": True
                },
                {"id": "caste_name", "type": "string", "required": True},
                {"id": "caste_certificate_number", "type": "string", "required": True}
            ],
        },

        {
            "step_id": "residence_details",
            "fields": [
                {"id": "state", "type": "enum", "options": ["kerala"], "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "taluk", "type": "string", "required": False},
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "address", "type": "string", "required": True},
                {"id": "pincode", "type": "string", "required": True}
            ],
        },

        {
            "step_id": "school_education_details",
            "fields": [
                {"id": "is_student", "type": "boolean", "required": True},
                {
                    "id": "current_class",
                    "type": "enum",
                    "options": [
                        "class_1","class_2","class_3","class_4",
                        "class_5","class_6","class_7",
                        "class_8","class_9","class_10"
                    ],
                    "required": True
                },
                {
                    "id": "school_type",
                    "type": "enum",
                    "options": [
                        "government",
                        "aided",
                        "recognized_unaided",
                        "cbse",
                        "icse",
                        "kendriya_vidyalaya"
                    ],
                    "required": True
                },
                {"id": "school_name", "type": "string", "required": True},
                {"id": "school_district", "type": "string", "required": True},
                {"id": "admission_status", "type": "enum", "options": ["enrolled"], "required": True}
            ],
        },

        {
            "step_id": "income_details",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": False},
                {"id": "income_certificate_number", "type": "string", "required": False},
                {"id": "bpl_status", "type": "boolean", "required": False}
            ],
        },

        {
            "step_id": "disability_details",
            "fields": [
                {"id": "is_person_with_disability", "type": "boolean", "required": False},
                {"id": "disability_percentage", "type": "number", "required": False},
                {"id": "disability_certificate_number", "type": "string", "required": False}
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
                {"id": "student_identity_proof", "type": "file", "required": True},
                {"id": "aadhaar_card", "type": "file", "required": True},
                {"id": "student_photograph", "type": "file", "required": True},
                {"id": "caste_certificate", "type": "file", "required": True},
                {"id": "income_certificate", "type": "file", "required": False},
                {"id": "residence_proof", "type": "file", "required": True},
                {"id": "disability_certificate", "type": "file", "required": False}
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
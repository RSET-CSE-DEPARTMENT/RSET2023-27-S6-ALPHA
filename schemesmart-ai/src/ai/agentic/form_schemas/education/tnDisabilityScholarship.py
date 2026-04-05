# src/ai/agentic/form_schemas/education/tnDisabilityScholarship.py

tnDisabilityScholarship = {
    "scheme_id": "EDU_SCH_020",
    "scheme_name": "Scholarship for Students with Disabilities (Grades 1–8)",
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
                {"id": "aadhaar_number", "type": "string", "required": False},
                {"id": "student_mobile_number", "type": "string", "required": False}
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
            "step_id": "residence_details",
            "fields": [
                {"id": "state", "type": "enum", "options": ["tamil_nadu"], "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "taluk", "type": "string", "required": False},
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "address", "type": "string", "required": True},
                {"id": "pincode", "type": "string", "required": True}
            ],
        },

        {
            "step_id": "disability_details",
            "fields": [
                {"id": "is_person_with_disability", "type": "boolean", "required": True},
                {
                    "id": "type_of_disability",
                    "type": "enum",
                    "options": [
                        "visual_impairment",
                        "hearing_impairment",
                        "locomotor_disability",
                        "intellectual_disability",
                        "multiple_disability",
                        "other"
                    ],
                    "required": True
                },
                {"id": "disability_percentage", "type": "number", "required": True},
                {"id": "disability_certificate_number", "type": "string", "required": True},
                {"id": "disability_certificate_issuing_authority", "type": "string", "required": False}
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
                        "class_1","class_2","class_3","class_4","class_5",
                        "class_6","class_7","class_8"
                    ],
                    "required": True
                },
                {
                    "id": "school_type",
                    "type": "enum",
                    "options": [
                        "government",
                        "government_aided",
                        "recognized_private"
                    ],
                    "required": True
                },
                {"id": "school_name", "type": "string", "required": True},
                {"id": "school_district", "type": "string", "required": True},
                {"id": "admission_status", "type": "enum", "options": ["enrolled"], "required": True}
            ],
        },

        {
            "step_id": "benefit_declaration",
            "fields": [
                {
                    "id": "receiving_other_similar_scholarship",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "certificate_not_availing_other_assistance",
                    "type": "boolean",
                    "required": True
                }
            ],
        },

        {
            "step_id": "document_uploads",
            "fields": [
                {"id": "non_availing_certificate", "type": "file", "required": True},
                {"id": "disability_certificate", "type": "file", "required": True},
                {"id": "school_certificate", "type": "file", "required": True},
                {"id": "student_photograph", "type": "file", "required": False}
            ],
        },

        {
            "step_id": "declaration",
            "fields": [
                {"id": "applicant_declaration", "type": "boolean", "required": True},
                {"id": "place_of_application", "type": "string", "required": True},
                {"id": "date_of_application", "type": "date", "required": True},
                {"id": "parent_or_guardian_signature", "type": "string", "required": True}
            ],
        }

    ],
}
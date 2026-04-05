homesForIntellectuallyImpaired = {
    "scheme_id": "HOUSING_001",
    "scheme_name": "Homes For Intellectually Impaired Persons",

    "form_steps": [

        {
            "step_id": "child_personal_information",
            "fields": [
                {"id": "child_full_name", "type": "string", "required": True},
                {"id": "date_of_birth", "type": "date", "required": True},
                {"id": "age", "type": "number", "required": True},
                {
                    "id": "gender",
                    "type": "enum",
                    "options": ["male", "female", "other"],
                    "required": True
                },
                {"id": "aadhaar_number", "type": "string", "required": False},
                {
                    "id": "orphan_status",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "child_photo_uploaded",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "guardian_details",
            "fields": [
                {"id": "guardian_name", "type": "string", "required": False},
                {
                    "id": "guardian_relationship",
                    "type": "enum",
                    "options": [
                        "father",
                        "mother",
                        "relative",
                        "legal_guardian",
                        "caretaker",
                        "child_welfare_committee"
                    ],
                    "required": False
                },
                {"id": "guardian_mobile_number", "type": "string", "required": False},
                {"id": "guardian_aadhaar_number", "type": "string", "required": False},
                {"id": "guardian_address", "type": "string", "required": False}
            ]
        },

        {
            "step_id": "disability_details",
            "fields": [
                {
                    "id": "disability_type",
                    "type": "enum",
                    "options": [
                        "intellectual_disability",
                        "mental_retardation",
                        "developmental_disorder"
                    ],
                    "required": True
                },
                {
                    "id": "disability_percentage",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "disability_certificate_issued",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "disability_certificate_number",
                    "type": "string",
                    "required": False
                },
                {
                    "id": "issuing_medical_authority",
                    "type": "string",
                    "required": False
                }
            ]
        },

        {
            "step_id": "residency_details",
            "fields": [
                {
                    "id": "citizenship",
                    "type": "enum",
                    "options": ["indian"],
                    "required": True
                },
                {
                    "id": "state_of_residence",
                    "type": "enum",
                    "options": ["maharashtra"],
                    "required": True
                },
                {"id": "district", "type": "string", "required": True},
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "full_address", "type": "string", "required": True},
                {
                    "id": "maharashtra_domicile_certificate",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "child_welfare_committee_details",
            "fields": [
                {
                    "id": "referred_by_child_welfare_committee",
                    "type": "boolean",
                    "required": True
                },
                {"id": "committee_district", "type": "string", "required": False},
                {"id": "referral_order_number", "type": "string", "required": False},
                {"id": "date_of_referral", "type": "date", "required": False}
            ]
        },

        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_holder_name", "type": "string", "required": True},
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "bank_name", "type": "string", "required": True},
                {"id": "branch_name", "type": "string", "required": False},
                {
                    "id": "aadhaar_linked_to_bank",
                    "type": "boolean",
                    "required": False
                }
            ]
        },

        {
            "step_id": "document_upload_confirmation",
            "fields": [
                {
                    "id": "aadhaar_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "passport_photos_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "age_proof_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "domicile_certificate_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "disability_certificate_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "bank_passbook_uploaded",
                    "type": "boolean",
                    "required": True
                }
            ]
        },

        {
            "step_id": "declaration",
            "fields": [
                {
                    "id": "information_true",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "guardian_signature_name",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "submission_date",
                    "type": "date",
                    "required": True
                }
            ]
        }

    ]
}
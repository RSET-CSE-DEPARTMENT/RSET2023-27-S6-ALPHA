# src/ai/agentic/form_schemas/generic_fallback.py
#
# A generic form schema used for any scheme that does not have
# a custom form schema defined. This is automatically used by the
# /form/start/{scheme_id} and /form/answer/{scheme_id} endpoints
# when SCHEMES.get(scheme_id) returns None.

GENERIC_FORM_SCHEMA = {
    "scheme_id": "__generic__",
    "scheme_name": "Application Form",
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
                {"id": "mobile_number", "type": "string", "required": True},
                {"id": "email", "type": "string", "required": False},
            ],
        },
        {
            "step_id": "address_details",
            "fields": [
                {"id": "address", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "state", "type": "string", "required": True},
                {"id": "pincode", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "income_and_category",
            "fields": [
                {"id": "annual_family_income", "type": "number", "required": True},
                {
                    "id": "category",
                    "type": "enum",
                    "options": ["general", "obc", "sc", "st", "ews"],
                    "required": True,
                },
                {"id": "income_certificate_number", "type": "string", "required": False},
                {"id": "bpl_status", "type": "boolean", "required": False},
            ],
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_name", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "aadhaar_linked", "type": "boolean", "required": True},
            ],
        },
        {
            "step_id": "documents_upload",
            "fields": [
                {"id": "aadhaar_card", "type": "file", "required": True},
                {"id": "passport_photo", "type": "file", "required": True},
                {"id": "income_certificate", "type": "file", "required": True},
                {"id": "residence_proof", "type": "file", "required": True},
            ],
        },
        {
            "step_id": "declaration",
            "fields": [
                {"id": "applicant_declaration", "type": "boolean", "required": True},
                {"id": "date_of_application", "type": "date", "required": True},
                {"id": "applicant_signature", "type": "string", "required": True},
            ],
        },
    ],
}

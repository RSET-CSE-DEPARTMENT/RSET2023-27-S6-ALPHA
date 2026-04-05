loanAdvanceHouseConstructionTripura = {
    "scheme_id": "HOUSING_011",
    "scheme_name": "Scheme For Loan And Advances to the Beneficiary For Construction Of House",
    "form_steps": [
        {
            "step_id": "applicant_personal_information",
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
                {"id": "aadhaar_number", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "worker_registration_details",
            "fields": [
                {
                    "id": "registered_boc_worker",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "boc_registration_years",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "years_before_retirement",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "boc_worker_registration_card_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "economic_and_category_details",
            "fields": [
                {
                    "id": "annual_income",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "ews_category",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "income_affidavit_available",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "ews_certificate_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "house_ownership_details",
            "fields": [
                {
                    "id": "owns_pucca_house_anywhere",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "affidavit_no_pucca_house_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "land_details",
            "fields": [
                {
                    "id": "land_owned",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "land_area_sq_meters",
                    "type": "number",
                    "required": True
                },
                {
                    "id": "property_valuation_certificate_available",
                    "type": "boolean",
                    "required": True
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
                    "options": ["tripura"],
                    "required": True
                },
                {"id": "district", "type": "string", "required": True},
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "full_address", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "bank_details",
            "fields": [
                {"id": "bank_account_holder_name", "type": "string", "required": True},
                {"id": "bank_account_number", "type": "string", "required": True},
                {"id": "bank_ifsc", "type": "string", "required": True},
                {"id": "bank_name", "type": "string", "required": True},
                {"id": "branch_name", "type": "string", "required": False}
            ]
        },
        {
            "step_id": "document_uploads",
            "fields": [
                {
                    "id": "boc_worker_registration_card_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "aadhaar_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "income_affidavit_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "identity_address_proof_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "ews_certificate_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "bank_details_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "property_valuation_certificate_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "affidavit_no_pucca_house_uploaded",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "declaration",
            "fields": [
                {"id": "information_true", "type": "boolean", "required": True},
                {"id": "applicant_signature_name", "type": "string", "required": True},
                {"id": "submission_date", "type": "date", "required": True}
            ]
        }
    ]
}
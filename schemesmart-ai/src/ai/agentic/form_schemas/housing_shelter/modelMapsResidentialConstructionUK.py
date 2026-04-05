modelMapsResidentialConstructionUK = {
    "scheme_id": "HOUSING_018",
    "scheme_name": "Providing Model Maps for Residential Construction",
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
                    "options": ["uttarakhand"],
                    "required": True
                },
                {"id": "district", "type": "string", "required": True},
                {
                    "id": "is_resident_of_haridwar",
                    "type": "boolean",
                    "required": True
                },
                {"id": "village_or_city", "type": "string", "required": True},
                {"id": "full_address", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "land_ownership_details",
            "fields": [
                {
                    "id": "owns_residential_land",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "land_location",
                    "type": "string",
                    "required": True
                },
                {
                    "id": "land_ownership_proof_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "construction_preferences",
            "fields": [
                {
                    "id": "type_of_house_planned",
                    "type": "enum",
                    "options": [
                        "single_floor",
                        "double_floor",
                        "small_house",
                        "independent_house"
                    ],
                    "required": False
                },
                {
                    "id": "selected_model_map",
                    "type": "string",
                    "required": False
                }
            ]
        },
        {
            "step_id": "document_details",
            "fields": [
                {"id": "aadhaar_available", "type": "boolean", "required": True},
                {
                    "id": "land_ownership_document_available",
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
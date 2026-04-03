mapSimplificationProcessUK = {
    "scheme_id": "HOUSING_019",
    "scheme_name": "Map Simplification Process",
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
                    "id": "is_land_in_haridwar_district",
                    "type": "boolean",
                    "required": True
                },
                {"id": "city_or_village", "type": "string", "required": True},
                {"id": "full_address", "type": "string", "required": True}
            ]
        },
        {
            "step_id": "land_ownership_details",
            "fields": [
                {
                    "id": "owns_land",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "land_area_sq_meters",
                    "type": "number",
                    "required": False
                },
                {
                    "id": "land_ownership_document_available",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "construction_map_details",
            "fields": [
                {
                    "id": "map_type",
                    "type": "enum",
                    "options": [
                        "residential",
                        "commercial"
                    ],
                    "required": True
                },
                {
                    "id": "map_prepared_by_architect",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "map_uploaded",
                    "type": "boolean",
                    "required": True
                }
            ]
        },
        {
            "step_id": "document_details",
            "fields": [
                {"id": "aadhaar_available", "type": "boolean", "required": True},
                {
                    "id": "land_document_uploaded",
                    "type": "boolean",
                    "required": True
                },
                {
                    "id": "building_map_uploaded",
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
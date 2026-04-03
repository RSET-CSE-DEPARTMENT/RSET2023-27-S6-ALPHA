iconicMotherAward = {
    "scheme_id": "WOMEN_CHILD_009",
    "scheme_name": "National Award for Senior Citizens – Iconic Mother",
    "form_steps": [
        {
            "step_id": "nominee_personal_information",
            "fields": [
                {"id": "full_name", "type": "string", "required": True},
                {"id": "date_of_birth", "type": "date", "required": True},
                {"id": "age", "type": "number", "required": True},
                {
                    "id": "gender",
                    "type": "enum",
                    "options": ["female"],
                    "required": True,
                },
                {"id": "aadhaar_number", "type": "string", "required": True},
                {"id": "mobile_number", "type": "string", "required": True},
                {"id": "email", "type": "string", "required": False},
            ],
        },
        {
            "step_id": "residency_details",
            "fields": [
                {"id": "state", "type": "string", "required": True},
                {"id": "district", "type": "string", "required": True},
                {"id": "address_line1", "type": "string", "required": True},
                {"id": "address_line2", "type": "string", "required": False},
                {"id": "pincode", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "family_details",
            "fields": [
                {"id": "number_of_children", "type": "number", "required": True},
                {"id": "children_details", "type": "string", "required": False},
                {"id": "family_background", "type": "string", "required": False},
            ],
        },
        {
            "step_id": "achievement_details",
            "fields": [
                {"id": "achievement_description", "type": "string", "required": True},
                {"id": "years_of_contribution", "type": "number", "required": False},
                {"id": "community_recognition", "type": "boolean", "required": False},
            ],
        },
        {
            "step_id": "nominating_agency_details",
            "fields": [
                {"id": "nominating_agency_name", "type": "string", "required": True},
                {"id": "nominator_name", "type": "string", "required": True},
                {"id": "nominator_designation", "type": "string", "required": True},
                {"id": "nominator_contact_number", "type": "string", "required": True},
            ],
        },
        {
            "step_id": "document_details",
            "fields": [
                {"id": "aadhaar_card_uploaded", "type": "boolean", "required": True},
                {"id": "age_proof_uploaded", "type": "boolean", "required": True},
                {"id": "bio_data_uploaded", "type": "boolean", "required": True},
                {"id": "achievement_details_uploaded", "type": "boolean", "required": True},
            ],
        },
    ],
}
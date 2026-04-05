"""
Seed Script: Insert all pre-existing JSON schemes from src/data/schemes/ into Supabase.
Run once from the project root: python backend/seed_supabase.py
"""

import json
import os
import sys

# Add project root to path so we can import backend modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.database import supabase

# Path to JSON scheme files
SCHEMES_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "src", "data", "schemes"
)

def seed():
    inserted = 0
    skipped = 0
    errors = 0

    print(f"\n📂 Reading schemes from: {SCHEMES_PATH}\n")

    for sector_dir in os.listdir(SCHEMES_PATH):
        sector_path = os.path.join(SCHEMES_PATH, sector_dir)
        if not os.path.isdir(sector_path):
            continue

        print(f"  🗂  Sector: {sector_dir}")

        for filename in os.listdir(sector_path):
            if not filename.endswith(".json"):
                continue

            filepath = os.path.join(sector_path, filename)

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if not content:
                        print(f"    ⚠️  Empty file: {filename}")
                        skipped += 1
                        continue

                    scheme = json.loads(content)

                scheme_id = scheme.get("scheme_id")
                if not scheme_id:
                    print(f"    ⚠️  No scheme_id in: {filename}")
                    skipped += 1
                    continue

                # Map JSON fields -> Supabase columns
                # The Supabase 'schemes' table has:
                # id (auto), scheme_id, scheme_name, sector, description,
                # eligibility, benefits, documents_required,
                # application_process, keywords, state, added_at (auto)
                row = {
                    "scheme_id": scheme_id,
                    "scheme_name": scheme.get("scheme_name", ""),
                    "sector": scheme.get("sector", sector_dir),
                    "description": scheme.get("description", ""),
                    "eligibility": scheme.get("eligibility", []),
                    "benefits": scheme.get("benefits", []),
                    "documents_required": scheme.get("documents_required", []),
                    "application_process": scheme.get("application_process", {}),
                    "keywords": scheme.get("keywords", []),
                    "state": scheme.get("state", "All India"),
                }

                # Upsert: delete old + insert fresh (avoids duplicate errors)
                supabase.table("schemes").delete().eq("scheme_id", scheme_id).execute()
                result = supabase.table("schemes").insert(row).execute()

                if result.data:
                    print(f"    ✅  Inserted: {scheme_id} - {scheme.get('scheme_name', '')}")
                    inserted += 1
                else:
                    print(f"    ❌  Failed:   {scheme_id}")
                    errors += 1

            except Exception as e:
                print(f"    ❌  Error in {filename}: {e}")
                errors += 1

    print(f"\n{'='*50}")
    print(f"✅  Inserted : {inserted} schemes")
    print(f"⚠️   Skipped  : {skipped} files")
    print(f"❌  Errors   : {errors} files")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    seed()

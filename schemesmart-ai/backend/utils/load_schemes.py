import os
import json

# Path from project root
BASE_PATH = os.path.join("src", "data", "schemes")

def load_all_schemes():
    all_schemes = []

    for sector_folder in os.listdir(BASE_PATH):
        sector_path = os.path.join(BASE_PATH, sector_folder)

        if os.path.isdir(sector_path):
            for file in os.listdir(sector_path):
                if file.endswith(".json"):
                    file_path = os.path.join(sector_path, file)

                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        all_schemes.append(data)

    return all_schemes
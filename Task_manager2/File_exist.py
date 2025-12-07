import os
import json

def check_file_exist(filename):
    try:
        if os.path.exists(filename):
            # Try to read JSON
            with open(filename, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    # File exists but is empty or invalid JSON
                    data = []
                    with open(filename, 'w') as file:
                        json.dump(data, file)
        else:
            # File doesn't exist, create with empty list
            with open(filename, 'w') as file:
                json.dump([], file)

    except Exception as error:
        print(f"There has been an issue with the file: {error}")
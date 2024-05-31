import json

def serialize_and_save_to_file(data, filename):
    """Serializes the data to JSON format and saves it to a file."""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Data has been serialized and saved to '{filename}'")
    except IOError as e:
        print(f"An error occurred while saving to file: {e}")

def load_and_deserialize(filename):
    """Loads data from a JSON file and deserializes it to a Python object."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except IOError as e:
        print(f"An error occurred while loading from file: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"An error occurred while decoding JSON: {e}")
        return None


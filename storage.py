"""
This module handles saving and loading data to a local JSON file.
It provides data persistence so tasks aren't lost when the application closes.
"""
import json
import os

DEFAULT_FILE = "assignments.json"

def load_data(filename=DEFAULT_FILE):
    """
    Loads tasks from the JSON file. 
    Returns an empty dictionary if the file doesn't exist or is corrupted.
    """
    if not os.path.exists(filename):
        return {}
        
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Warning: Data file corrupted. Starting with a fresh database.")
        return {}
    except Exception as e:
        print(f"Error loading data: {e}")
        return {}

def save_data(data, filename=DEFAULT_FILE):
    """
    Saves the tasks dictionary to the JSON file.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

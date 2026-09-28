"""
This module contains functions to validate user input.
It ensures our program doesn't crash if the user enters the wrong type of data.
"""
from datetime import datetime

def is_valid_date(date_str):
    """
    Checks if a string is a valid date in YYYY-MM-DD format.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True, date_str
    except ValueError:
        return False, "Invalid date format. Please use YYYY-MM-DD."

def is_valid_percentage(val_str):
    """
    Checks if the input is a valid percentage number between 1 and 100.
    """
    try:
        val = float(val_str)
        if 1 <= val <= 100:
            return True, val
        return False, "Percentage must be between 1 and 100."
    except ValueError:
        return False, "Input must be a valid number."

def is_valid_hours(val_str):
    """
    Checks if the estimated hours is a positive number.
    """
    try:
        val = float(val_str)
        if val > 0:
            return True, val
        return False, "Hours must be a positive number."
    except ValueError:
        return False, "Input must be a valid number."

def is_non_empty_string(val_str):
    """
    Ensures the user didn't just press Enter without typing anything.
    """
    clean_str = val_str.strip()
    if clean_str:
        return True, clean_str
    return False, "Input cannot be empty."

import re

# Adding Time logic in 12 Format
def validate_time_12(text):
    "Extracts time in 12 format from the given text."
    pattern = r'(0[0-9]|1[0-2]):[0-5][0-9]'
    description = """Valid time in 12-hour format should:
    - Be from 1 up to 12 hours
    - Contain : between hours and minutes (HH:MM format)
    - Minutes must be below 60 minutes"""

    matches = re.findall(pattern, text)
    return{
        'valid': bool(matches),
        'matches': matches,
        'description': description
    }

# Adding Time logic in 24 Format
def validate_time_24(text):
    "Extracts time in 12 format from the given text."
    pattern = r'(0[0-9]|1[0-9]|2[0-4]):[0-5][0-9]'
    description = """Valid time in 24-hour format should:
    - Be from 1 up to 24 hours
    - Contain : between hours and minutes (HH:MM format)
    - Minutes must be below 60 minutes"""

    matches = re.findall(pattern, text)
    return{
        'valid': bool(matches),
        'matches': matches,
        'description': description
    }

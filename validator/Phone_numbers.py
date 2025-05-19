import re

# Adding Phone number logic
def validate_phone(text):
    pattern = r'[(][+]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{3}?[0-9]{3}[-\s\.]?[0-9]{3}'
    description = """Valid phone numbers have:
    - Optional country code (+250, +255)
    - 3-digit area code in parentheses (In our case)
    - 9-digit number with -, . or space separators after 3 digits
    - Examples are (+123) 456-789-001, (+250) 790 068 175, (+123).456.789.103"""
    
    matches = re.match(pattern, text)
    return {
        'valid': bool(matches),
        'matches': matches,
        'description': description
    }
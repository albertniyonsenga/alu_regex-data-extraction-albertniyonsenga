import re

# Adding Currency logic
def validate_currency(text):
    pattern = r'\$\d{1,3}(?:,\d{3})*\.\d{2}\b'
    description = """Valid USD currency format:
- Starts with $ symbol (We used US Dollars in our case)
- Comma thousands separators
- Requires two decimal places
- Examples are $19.99, $1,234.56 or $10.00"""
    
    matches = re.findall(pattern, text)
    return {
        'valid': bool(matches),
        'matches': matches,
        'description': description
    }
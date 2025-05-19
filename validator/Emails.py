import re

# Adding Email extraction logic 
def validate_email(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    description = """Valid email should contain:
    - Alphanumeric characters and ._%+- symbols before @
    - Alphanumeric and .- characters after @ followed by .
    - Domains with at least 2 letters after dot"""
    
    matches = re.findall(pattern, text)
    return {
        'valid': bool(matches),
        'matches': matches,
        'description': description
    }
import re

# Adding Url extraction logic
def validate_url(text):
    pattern = r'\bhttps?://(?:www\.)?[\w-]+\.[\w.-]+[/\w .-]*\b'
    description = """Valid URL should:
- Start with http:// or https://
- May include www. or not just like Example of https://rubular.com/
- Contain valid domain characters (letters, numbers, dots, hyphens)
- May include path/query parameters"""
    
    matches = re.findall(pattern, text)
    return {
        'valid': bool(matches),
        'matches': matches,
        'description': description
    }
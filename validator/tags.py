import re

"Extracting hashtags from the given text."
def validate_hashtags(text):
    "Extracting hashtags from the given text."
    pattern = r'#\w+\b'
    description = """Valid Hashtag should contain:
    - '#' at the beginning
    - Continued with letter (whether capitalized or not)
    - No apostrophe only underscores"""

    matches = re.findall(pattern, text)
    return{
        'valid': bool(matches),
        'matches': matches,
        'description': description
    }
import re

# Adding Email extraction logic 
def extract_emails(text):
    "Extracts email addresses from the given text."
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(pattern, text)

# Adding Url extraction logic
def extract_urls(text):
    "Extracts URLs from the given text."
    pattern = r'\bhttps?://(?:www\.)?[\w-]+\.[\w.-]+[/\w .-]*\b'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    "Extracts phone numbers from the given text."
    pattern = r'\b(?:\(\d{3}\)[\s-]?|\d{3}[.-]?)\d{3}[.-]?\d{3}\b'
    return re.findall(pattern, text)

def main():
    # For testing while using `re` package
    test_email = "albertniyon@gmail.com or a.niyonseng@alustudent.com"
    test_url = """https://rubular.com/, despite of using only that url let's try https://www.ucll.be/en
      or simply use this url to youtube video of It's complicated by Fave here https://www.youtube.com/watch?v=0Z7RjfeQaNk&pp=0gcJCdgAo7VqN5tD"""
    
    test_phone = "(250) 790 068 175 my number or this (250) 790-068-175 or simply with dot (250) 790.068.175"

    # Extracting 
    emails = extract_emails(test_email)
    urls = extract_urls(test_url)
    phone = extract_phone_numbers(test_phone)

    # Printing the results
    print("Extracted Emails:", emails)
    print("Extracted Urls:", urls)
    print("Extracted Phone number:", phone)

if __name__ == "__main__":
    main()
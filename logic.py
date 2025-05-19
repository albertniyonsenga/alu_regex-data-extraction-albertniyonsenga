import re

# Adding Email extraction logic 
def extract_emails(text):
    "Extracts email addresses from the given text."
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

# Adding Url extraction logic
def extract_urls(text):
    "Extracts URLs from the given text."
    pattern = r'https?://(?:www\.)?[\w-]+\.[\w.-]+[/\w .-]*'
    return re.findall(pattern, text)


def main():
    # For testing while using `re` package
    test_email = "albertniyon@gmail.com or a.niyonseng@alustudent.com"
    test_url = "https://rubular.com/ or https://www.ucll.be/en"

    # Extracting 
    emails = extract_emails(test_email)
    urls = extract_urls(test_url)

    # Printing the results
    print("Extracted Emails:", emails)
    print("Extracted Urls:", urls)
    
if __name__ == "__main__":
    main()
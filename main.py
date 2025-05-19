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

# Adding Phone number logic
def extract_phone_numbers(text):
    "Extracts phone numbers from the given text."
    pattern = r'\b(?:\(\d{3}\)[\s-]?|\d{3}[.-]?)\d{3}[.-]?\d{3}\b'
    return re.findall(pattern, text)

# Adding Currency logic
def extract_currency(text):
    "Extracts currency amounts from the given text."
    pattern = r'\$(?:\d{1,3}(?:,\d{3})*|\d+)\.\d{2}\b'
    return re.findall(pattern, text)

# Adding Time in 12 Format
def extract_time_12(text):
    "Extracts time in 12 format from the given text."
    pattern = r'(0[0-9]|1[0-2]):[0-5][0-9]\b'
    return re.findall(pattern, text)

def main():
    # For testing while using `re` package
    test_email = "albertniyon@gmail.com or a.niyonseng@alustudent.com"
    test_url = """https://rubular.com/, despite of using only that url let's try https://www.ucll.be/en
      or simply use this url to youtube video of It's complicated by Fave here https://www.youtube.com/watch?v=0Z7RjfeQaNk&pp=0gcJCdgAo7VqN5tD"""
    
    test_phone = "(250) 790 068 175 my number or this (250) 790-068-175 or simply with dot (250) 790.068.175"
    test_currency = "This semester i will pay around $333.30 or i can even pay $30.00 until i reach the actual amount"
    test_time_12 = "We are around 12:00 AM i guess or it's 19:02 am wrong"


    # Extracting 
    emails = extract_emails(test_email)
    urls = extract_urls(test_url)
    phone = extract_phone_numbers(test_phone)
    currency = extract_currency(test_currency)
    format12 = extract_time_12(test_time_12)

    # Printing the results
    print("Extracted Emails:", emails)
    print("Extracted Urls:", urls)
    print("Extracted Phone number:", phone)
    print("Extracted Currency amount:", currency)
    print("Extracted Time in 12 format:", format12)


if __name__ == "__main__":
    main()
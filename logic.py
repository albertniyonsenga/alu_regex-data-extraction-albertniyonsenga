import re

def extract_emails(text):
    "Extracts email addresses from the given text."
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)


def main():
    # For testing while using `re` package
    test = "albertniyon@gmail.com or a.niyonseng@alustudent.com"

    # Extracting email
    emails = extract_emails(test)
    print("Extracted Emails:", emails)
if __name__ == "__main__":
    main()
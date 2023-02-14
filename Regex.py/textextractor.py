import re

def extract_info(text):
    # Regular expressions to match phone numbers, email addresses, and URLs
    phone_number_pattern = re.compile(r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}')
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    url_pattern = re.compile(r'https?://[a-zA-Z0-9._/-]+')

    # Extract information from the text
    phone_numbers = re.findall(phone_number_pattern, text)
    email_addresses = re.findall(email_pattern, text)
    urls = re.findall(url_pattern, text)

    return phone_numbers, email_addresses, urls

text = '''
    My phone number is 703-204-3837 and my email is ravi@gmail.com.
    You can also find more information at https://www.ravitejae.com.
'''
phone_numbers, email_addresses, urls = extract_info(text)

print('Phone Numbers:', phone_numbers)
print('Email Addresses:', email_addresses)
print('URLs:', urls)

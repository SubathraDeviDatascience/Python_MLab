import re
def extract_email(text):
    Email_pattern=r'[a-zA-Z0-9._/+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}'
    return re.findall(Email_pattern,text)
sample_text="Please contact us sample @ exampl.com or sales@example.org"
Emails=extract_email(sample_text)
print("Extract Email:",Emails)
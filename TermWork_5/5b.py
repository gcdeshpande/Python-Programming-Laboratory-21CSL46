import re

def find_phone_numbers_and_emails(filename):
    with open(filename, 'r') as file:
        content = file.read()

        phone_pattern = r'\+\d{10,12}'
        phone_numbers = re.findall(phone_pattern, content)

        email_pattern = r'\S+@\S+'
        email_addresses = re.findall(email_pattern, content)

    return phone_numbers, email_addresses

# Replace 'your_file.txt' with the actual file path
file_path = 'your_file.txt'
phone_numbers, email_addresses = find_phone_numbers_and_emails(file_path)

print("Phone Numbers:")
for number in phone_numbers:
    print(number)

print("\nEmail Addresses:")
for email in email_addresses:
    print(email)

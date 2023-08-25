def test_find_phone_numbers_and_emails():
    test_cases = [
        ("TestCases/testcase1.txt", ["+1234567890"], ["test@example.com"]),
        ("TestCases/testcase2.txt", ["+919900889977", "+918877665544"], ["info@example.com", "support@sample.org"]),
        ("TestCases/testcase3.txt", [], []),
        ("TestCases/testcase4.txt", [], []),
        ("TestCases/testcase5.txt", [], ["user.name123@gmail.com", "support@subdomain.example.org"]),
    ]

    for filename, expected_phones, expected_emails in test_cases:
        phone_numbers, email_addresses = find_phone_numbers_and_emails(filename)
        print(f"File: {filename}")
        print(f"Expected Phone Numbers: {expected_phones}")
        print(f"Actual Phone Numbers: {phone_numbers}")
        print(f"Expected Email Addresses: {expected_emails}")
        print(f"Actual Email Addresses: {email_addresses}")
        print("=" * 30)

if __name__ == "__main__":
    test_find_phone_numbers_and_emails()

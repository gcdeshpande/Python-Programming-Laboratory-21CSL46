def test_isphonenumber_functions():
    test_cases = [
        ("415-555-4242", True),
        ("123-456-7890", True),
        ("987-654-3210", True),
        ("123-456-789", False),  # Incomplete phone number
        ("415-5555-4242", False),  # Incomplete phone number
        ("415-555-42424", False),  # Extra digit
        ("415a555-4242", False),  # Non-numeric character
        ("415-555-42a2", False),  # Non-numeric character
        ("1234567890", False),  # No hyphens
    ]

    for phone_number, expected_result in test_cases:
        result_non_regex = isphonenumber(phone_number)
        result_regex = isphonenumber_regex(phone_number)

        print(f"Phone Number: {phone_number}")
        print(f"Expected Result (Non-Regex): {expected_result}")
        print(f"Actual Result (Non-Regex): {result_non_regex}")
        print(f"Expected Result (Regex): {expected_result}")
        print(f"Actual Result (Regex): {result_regex}")
        print("=" * 30)

if __name__ == "__main__":
    test_isphonenumber_functions()

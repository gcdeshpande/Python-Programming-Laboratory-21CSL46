def test_palindrome():
    test_cases = [
        (121, True),
        (7, True),
        (123456789987654321, True),
        (12345, False),
        (-121, False)
    ]
    
    for number, expected in test_cases:
        result = is_palindrome(number)
        if result == expected:
            print(f"Palindrome Test Passed: {number} is {'a' if expected else 'not a'} palindrome.")
        else:
            print(f"Palindrome Test Failed: {number} is {'a' if expected else 'not a'} palindrome, but got {result}.")

def test_digit_occurrences():
    test_cases = [
        (121, [0, 2, 1, 0, 0, 0, 0, 0, 0, 0]),
        (12345, [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]),
        (121, [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]),
        (7, [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]),
        (123456789987654321, [2, 4, 2, 2, 2, 2, 2, 2, 2, 2])
    ]
    
    for number, expected in test_cases:
        result = count_digit_occurrences(number)
        if result == expected:
            print(f"Digit Occurrences Test Passed: Occurrences for {number} are correct.")
        else:
            print(f"Digit Occurrences Test Failed: Expected {expected} for {number}, but got {result}.")

if __name__ == '__main__':
    test_palindrome()
    test_digit_occurrences()

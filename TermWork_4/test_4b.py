def test_roman_to_int():
    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("XLII", 42),
        ("XC", 90),
        ("CXXIII", 123),
        ("MMMCMXCIX", 3999),
    ]

    for roman_numeral, expected_integer in test_cases:
        result = roman_to_int(roman_numeral)
        print(f"Roman Numeral: {roman_numeral}")
        print(f"Expected Integer: {expected_integer}")
        print(f"Actual Integer: {result}")
        print("=" * 30)

if __name__ == "__main__":
    test_roman_to_int()

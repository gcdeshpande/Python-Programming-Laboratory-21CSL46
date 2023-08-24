def roman_to_int(roman_numeral):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in roman_numeral[::-1]:
        value = roman_dict[char]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value

    return total

# Example usage
roman_numeral=input("Enter a Roman Number: ")

integer_value = roman_to_int(roman_numeral)
print(f"The integer value of {roman_numeral} is {integer_value}")

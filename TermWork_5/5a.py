import re

def isphonenumber(input_str):
    if len(input_str) != 12:
        return False
    for i in range(0, 3):
        if not input_str[i].isdecimal():
            return False
    if input_str[3] != '-':
        return False
    for i in range(4, 7):
        if not input_str[i].isdecimal():
            return False
    if input_str[7] != '-':
        return False
    for i in range(8, 12):
        if not input_str[i].isdecimal():
            return False
    return True

# Test the function
print("Testing valid phone number without RegEx")
phone_number =input("Enter a Phone Number: ")
#phone_number = "415-555-4242"
if isphonenumber(phone_number):
    print(f"{phone_number} is a valid phone number.")
else:
    print(f"{phone_number} is not a valid phone number.")

def isphonenumber_regex(input_str):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    if re.match(pattern, input_str):
        return True
    else:
        return False

# Test the function
print("\n\nTesting valid phone number with RegEx")
phone_number =input("Enter a Phone Number: ")
#phone_number = "415-555-4242"
if isphonenumber_regex(phone_number):
    print(f"{phone_number} is a valid phone number.")
else:
    print(f"{phone_number} is not a valid phone number.")

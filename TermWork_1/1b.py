def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

def count_digit_occurrences(number):
    num_str = str(number)
    occurrences = [0] * 10  # Initialize a list to store digit occurrences
    
    for digit in num_str:
        occurrences[int(digit)] += 1
        
    return occurrences

def main():
    try:
        num = int(input("Enter a number: "))
        
        if is_palindrome(num):
            print(f"{num} is a palindrome.")
        else:
            print(f"{num} is not a palindrome.")
        
        occurrences = count_digit_occurrences(num)
        for digit, count in enumerate(occurrences):
            if count!=0:
                print(f"Digit {digit} occurs {count} time(s) in the number.")
            
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

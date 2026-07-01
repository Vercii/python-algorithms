number = int(input("Please enter an integer: "))
reverse = 0

# duplicates the original input
orig_number = number

# same algorithm as reversing the int
while number != 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

# compares the original and the reverse
if reverse == orig_number:
    print("Palindrome.")
else:
    print("NOT a Palindrome.")
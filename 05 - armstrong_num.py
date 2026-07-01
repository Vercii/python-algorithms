number = int(input("Enter a number: "))
number_temp = number
orig_number = number # stores the original input

# loop for counting digits, which will be used as an exponent later
digit_count = 0
while number_temp != 0:
    number_temp //= 10
    digit_count += 1

# loop for getting each digit, which will be used to multiply to the exponent individually then added to each other
total = 0
while number != 0:
    digit = number % 10
    total += digit**digit_count
    number //= 10

# if statement to check if the number is an armstrong number
if orig_number == total:
    print("Armstrong!")
else:
    print("Not Armstrong.")


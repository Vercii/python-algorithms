number = int(input("Enter a number: "))

total = 0

# loop won't stop until number hits 0
while number != 0: 
    digit = number % 10 # gets the last digit by taking the remainder
    total += digit # add the extracted digit to the running total
    number //= 10 # divides the original number by 10 until 0
    
print(total)
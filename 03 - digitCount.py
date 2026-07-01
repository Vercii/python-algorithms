# this code is for counting the digits

number = int(input("Enter a number: "))

# original digit count
count = 0 

# if the number is purely 0, automatically equate count to 1
if number == 0:
    count = 1

# increment per loop which serves as the digit count, deducts a digit by removing the remainder per loop
while number != 0:
    number //= 10
    count += 1

print("Digit Count: ", count)
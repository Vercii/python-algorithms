number = int(input("Please enter an integer: "))
reverse = 0

while number != 0: # as long as number isn't 0, the loop continues
    digit = number % 10 # gets the last digit by dividing it by 10 and getting the remainder
    reverse = reverse * 10 + digit # multiplies by 10 in order to have an extra "space" for the number that would be added which is digit
    number //= 10 # divides number per iteration until it reaches 0

print(reverse)

import math
number = int(input("Enter a number: ")) # user enters a number here

checker = 0

# for loop, takes the range of the inserted number + 1
for divisor in range(2, int(math.sqrt(number)) + 1):
    digit = number % (divisor)
    if digit == 0: 
        checker += 1
        break # immediately exits once checker becomes 1

# if checker is greater than or equal to 1 it will be considered NOT prime, vice versa
if checker == 1:
    print("This is NOT a Prime Number.")
# special cases for 0 and 1 since the algorithm contradicts them
elif number == 0 or number == 1:
    print("This is NOT a Prime Number")
else:
    print("This is a Prime Number!")



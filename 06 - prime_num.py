number = int(input("Enter a number: "))

cnt = number - 1 # automatically subtracts 1 from the start to avoid dividing it by itself
checker = 0

while cnt != 0:
    digit = number % cnt # this gets the remainder of number divided by cnt
    cnt -= 1 # subtracts 1 per iteration
    if digit == 0:
        checker += 1 # adds 1 to checker everytime the remainder is 0

# it will eventually hit 1 because it will be divided by 1 on the previous formula above
if checker > 1:
    print("This is NOT a Prime Number.")
else:
    print("This is a Prime Number!")



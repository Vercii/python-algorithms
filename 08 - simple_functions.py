def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def show_menu():
    print("1 - add")
    print("2 - subtract")
    print("3 - multiply")
    print("4 - divide")

# ---

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

show_menu()

operation = int(input("What operation would you like to do? "))


if operation == 1:
    print(add(num1, num2))
elif operation == 2:
    print(subtract(num1, num2))
elif operation == 3:
    print(multiply(num1, num2))
elif operation == 4:
    print(divide(num1, num2))
else:
    print("Invalid Choice")
#TASK 2 :- CALCULATOR

"""Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result."""


def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input('\n'"Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print('\n',"Addition of",num1, "+", num2, "=", add(num1, num2),'\n')

        elif choice == '2':
            print('\n',"Subtract of",num1, "-", num2, "=", subtract(num1, num2),'\n')

        elif choice == '3':
            print('\n',"Multiply of",num1, "*", num2, "=", multiply(num1, num2),'\n')

        elif choice == '4':
            print('\n',"Divide of",num1, "/", num2, "=", divide(num1, num2),'\n')

        next_calculation = input("Let's do next calculation? (Y/N): ")
        if next_calculation.lower() == "n" or next_calculation.lower() == "N":
            break
    else:
        print("Invalid Input")

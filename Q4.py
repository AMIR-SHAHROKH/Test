import random

def calculator():
    try:
        print("Calculator Menu:")
        print("1. Random")
        print("2. Manual")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':  # Random
            key = input("Enter a key to generate random numbers: ")
            random.seed(key)  # Setting seed based on the key

            num1 = random.uniform(0, 100)  # Generate random float between 0 and 100
            num2 = random.uniform(0, 100)  # Generate random float between 0 and 100

            operator = input("Enter the operator (+, -, *, /, %, ^): ")

        elif choice == '2':  # Manual
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /, %, ^): ")

        else:
            print("Invalid choice. Please enter 1 or 2.")
            return

        result = None

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            else:
                result = num1 / num2
        elif operator == '%':
            result = num1 % num2
        elif operator == '^':
            result = num1 ** num2
        else:
            print("Error: Invalid operator entered.")
            return

        print(f"The result of {num1} {operator} {num2} is {result}")

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()


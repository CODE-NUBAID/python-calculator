import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error! Division by zero."
def power(x, y): return x ** y
def sqrt(x): return math.sqrt(x) if x >= 0 else "Error! Negative root."
def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))
def tan(x): return math.tan(math.radians(x))

def show_menu():
    print("\n--- Python Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("0. Exit")

while True:
    show_menu()
    choice = input("Enter choice (0-9): ")

    if choice == '0':
        print("Goodbye!")
        break

    if choice in ['1', '2', '3', '4', '5']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input!")
            continue

        operations = {
            '1': add,
            '2': subtract,
            '3': multiply,
            '4': divide,
            '5': power
        }

        result = operations[choice](num1, num2)
        print("Result:", result)

    elif choice in ['6', '7', '8', '9']:
        try:
            num = float(input("Enter number: "))
        except ValueError:
            print("Invalid input!")
            continue

        operations = {
            '6': sqrt,
            '7': sin,
            '8': cos,
            '9': tan
        }

        result = operations[choice](num)
        print("Result:", result)

    else:
        print("Invalid choice!")
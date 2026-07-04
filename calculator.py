import math
from typing import Callable


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def power(a: float, b: float) -> float:
    return a ** b


def square_root(a: float) -> float:
    if a < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    return math.sqrt(a)


def sin_deg(a: float) -> float:
    return math.sin(math.radians(a))


def cos_deg(a: float) -> float:
    return math.cos(math.radians(a))


def tan_deg(a: float) -> float:
    return math.tan(math.radians(a))


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def show_menu() -> None:
    print("\n" + "=" * 30)
    print("      Python Calculator")
    print("=" * 30)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Sin (degrees)")
    print("8. Cos (degrees)")
    print("9. Tan (degrees)")
    print("0. Exit")


BINARY_OPERATIONS: dict[str, tuple[str, Callable[[float, float], float]]] = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
    "5": ("Power", power),
}

UNARY_OPERATIONS: dict[str, tuple[str, Callable[[float], float]]] = {
    "6": ("Square Root", square_root),
    "7": ("Sin", sin_deg),
    "8": ("Cos", cos_deg),
    "9": ("Tan", tan_deg),
}


def main() -> None:
    print("Welcome to the Python Calculator!")

    while True:
        show_menu()
        choice = input("Choose an option (0-9): ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        try:
            if choice in BINARY_OPERATIONS:
                name, func = BINARY_OPERATIONS[choice]
                first = get_number("Enter first number: ")
                second = get_number("Enter second number: ")
                result = func(first, second)
                print(f"{name} result: {result}")

            elif choice in UNARY_OPERATIONS:
                name, func = UNARY_OPERATIONS[choice]
                number = get_number("Enter number: ")
                result = func(number)
                print(f"{name} result: {result}")

            else:
                print("Invalid choice. Please select a number from 0 to 9.")

        except (ZeroDivisionError, ValueError) as error:
            print(f"Error: {error}")
        except Exception:
            print("Something went wrong. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCalculator closed.")

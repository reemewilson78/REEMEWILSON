"""Module for adding two numbers."""


def add(a: float | int, b: float | int) -> float | int:
    """Returns the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            result = add(num1, num2)
            # Format integer output cleanly if it's an integer
            if result.is_integer():
                result = int(result)
            print(f"The sum of {sys.argv[1]} and {sys.argv[2]} is {result}")
        except ValueError:
            print("Error: Please provide valid numbers as arguments.")
    else:
        print("Usage: python add_numbers.py <number1> <number2>")

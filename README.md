# Number Addition Tool

## Overview
Number Addition Tool is a Python command-line utility designed to calculate the sum of two numbers (integers or floating-point numbers). It provides a clean terminal interface for performing basic arithmetic addition and includes error handling for invalid input types and argument counts.

## Features
- **Addition Calculation:** Adds positive, negative, integer, and floating-point numbers.
- **Command-Line Interface (CLI):** Accepts two numerical inputs directly via command-line arguments.
- **Input Validation:** Handles invalid non-numeric inputs gracefully with descriptive error messages.
- **Clean Output Formatting:** Automatically formats whole numbers as integers (e.g., `5` instead of `5.0`) in the output presentation.
- **Automated Test Suite:** Comprehensive unit test coverage using `pytest`.

## Technologies Used
- **Programming Language:** Python 3 (3.12+)
- **Standard Libraries:** `sys`
- **Testing Framework:** `pytest`

## Project Structure
```text
.
├── .gitignore             # Specifies intentionally untracked files to ignore
├── add_numbers.py         # Main script containing addition logic and CLI interface
└── test_add_numbers.py    # Unit test suite for verifying addition functionality
```

- `add_numbers.py`: Contains the `add(a, b)` function to sum two numbers and CLI execution logic to parse arguments and display the result.
- `test_add_numbers.py`: Contains test cases using `pytest` to test positive integers, negative integers, mixed signs, zero, and floating-point arithmetic.
- `.gitignore`: Configured to exclude `__pycache__/` directory and compiled bytecode (`*.pyc`).

## Requirements
- **Python:** Python 3.10 or higher (tested with Python 3.12)
- **Dependencies:** `pytest` (required for running unit tests)

## Installation
1. **Clone or Download the Repository:**
   Ensure all repository files (`add_numbers.py`, `test_add_numbers.py`, `.gitignore`) are located in your working directory.

2. **Verify Python Installation:**
   Check that Python 3 is installed on your system:
   ```bash
   python3 --version
   ```

3. **Install Dependencies (Optional for testing):**
   Install `pytest` to run the test suite:
   ```bash
   pip install pytest
   ```

## Configuration
No environment variables or custom configuration files are required to run this project.

## How to Run
Run the application using Python 3 from your command line:

```bash
python3 add_numbers.py <number1> <number2>
```

### Examples
- Add two integers:
  ```bash
  python3 add_numbers.py 5 10
  ```
  *Output:* `The sum of 5 and 10 is 15`

- Add two floating-point numbers:
  ```bash
  python3 add_numbers.py 2.5 3.1
  ```
  *Output:* `The sum of 2.5 and 3.1 is 5.6`

- Add positive and negative numbers:
  ```bash
  python3 add_numbers.py -4 9
  ```
  *Output:* `The sum of -4 and 9 is 5`

## How It Works
1. **Core Function (`add`):**
   The `add(a, b)` function in `add_numbers.py` takes two numerical arguments (`float` or `int`) and returns their sum (`a + b`).

2. **CLI Parsing:**
   When `add_numbers.py` is executed directly:
   - It checks `sys.argv` to ensure exactly two command-line arguments are passed.
   - It converts the arguments to floating-point numbers (`float`).
   - It passes the parsed numbers to `add()`.
   - If the resulting float represents a whole integer (using `result.is_integer()`), it formats the output as an integer (`int`).
   - The result is printed to stdout in the format: `The sum of <num1> and <num2> is <result>`.

3. **Testing:**
   `test_add_numbers.py` imports `add` from `add_numbers.py` and runs multiple test scenarios using `pytest` assertions (including `pytest.approx` for floating-point precision checks).

## Usage
Execute the script from the terminal by providing two numbers as positional arguments.

To run the automated test suite:
```bash
pytest
```

## Error Handling / Troubleshooting
- **Incorrect Number of Arguments:**
  - *Symptom:* `Usage: python add_numbers.py <number1> <number2>`
  - *Cause:* Running the script without providing exactly 2 arguments.
  - *Solution:* Provide two numbers as command-line arguments (e.g., `python3 add_numbers.py 10 20`).

- **Invalid Input Types:**
  - *Symptom:* `Error: Please provide valid numbers as arguments.`
  - *Cause:* Passing non-numeric characters (e.g., letters or symbols) as arguments.
  - *Solution:* Ensure both command-line arguments are valid integers or decimal numbers.

- **`pytest` Command Not Found:**
  - *Symptom:* `command not found: pytest`
  - *Cause:* `pytest` package is not installed in your Python environment.
  - *Solution:* Install pytest using `pip install pytest`.

## Future Enhancements
Potential improvements for future development include:
- Interactive CLI prompt mode when command-line arguments are not passed.
- Support for adding more than two numbers at once.
- Support for additional arithmetic operations (subtraction, multiplication, division).
- Packaging as a standalone CLI application or library.

## Contributing
Contributions are welcome. To contribute:
1. Fork or clone the repository.
2. Create a new branch for your feature or bug fix.
3. Add tests in `test_add_numbers.py` for any new functionality.
4. Run `pytest` to ensure all tests pass.
5. Submit a pull request detailing your changes.

## License
No explicit license file is provided in this repository.

## Author
Author information is not explicitly provided in the repository files.

## Acknowledgements
- [Python Standard Library](https://docs.python.org/3/) for built-in modules (`sys`).
- [pytest](https://docs.pytest.org/) for the testing framework.

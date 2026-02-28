from typing import IO


def garden_operations() -> None:
    """
    Demonstrate handling of different built-in Python exceptions.

    This function intentionally triggers several common error types
    that may occur in a garden management program:

        - ValueError (invalid data conversion)
        - ZeroDivisionError (division by zero)
        - FileNotFoundError (missing file)
        - KeyError (missing dictionary key)

    Each error is caught using try/except blocks to show how
    the program can handle failures gracefully and continue running.

    It also demonstrates how to catch multiple exception types
    within a single except block.
    """
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
        print("")

    try:
        print("Testing ZeroDivisionError...")
        print(50 / 0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
        print("")

    try:
        print("Testing FileNotFoundError...")
        f: IO = open("missing.txt")
        f.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
        print("")

    try:
        print("Testing KeyError...")
        dic: dict[str, int] = {"pizza": 3}
        print(dic["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
        print("")

    try:
        print("Testing multiple errors together...")
        int("abc")
    except (ValueError, KeyError):
        print("Caught an error, but program continues!")
        print("")


def test_error_types() -> None:
    """
    Run and display tests for different exception handling cases.

    This function:
        - Prints a header message
        - Calls garden_operations() to trigger and catch errors
        - Confirms that all error tests completed successfully

    It demonstrates that the program continues execution
    even after multiple errors occur.
    """
    print("=== Garden Error Types Demo ===")
    print("")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

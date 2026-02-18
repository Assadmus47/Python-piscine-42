from typing import IO


def garden_operations() -> None:
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
        f: IO = open("fichier_inexesitant.txt")
        f.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
        print("")

    try:
        print("Testing KeyError...")
        dic: dict[str, int] = {"pizza": 3}
        print(dic["suchi"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
        print("")

    try:
        print("Testing multiple errors together...")
        int("abc")
    except (ValueError, KeyError):
        print("Caught an error, but program continues!")
        print("")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

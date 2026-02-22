import sys


def ft_command_quest() -> None:
    """
    Display command-line argument information.

    This function reads arguments passed through sys.argv and prints:
    - the program name
    - the number of arguments received
    - each argument with its index

    If no arguments are provided, it notifies the user accordingly.
    """
    print("=== Command Quest ===")
    argc: int = len(sys.argv)

    if argc < 2:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {argc - 1}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    ft_command_quest()

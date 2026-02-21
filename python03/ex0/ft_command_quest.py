import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    argc: int = len(sys.argv)

    if argc < 2:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {argc - 1}")
        for i in range(1, argc):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    ft_command_quest()

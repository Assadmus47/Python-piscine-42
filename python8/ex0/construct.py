
import os

import sys

import site


def is_in_venv() -> bool:
    return os.environ.get("VIRTUAL_ENV") is not None


def display_env_info() -> None:
    print("Current Python:", sys.executable)

    if is_in_venv():
        print(
            "Virtual Environment:",
            os.path.basename(os.environ.get("VIRTUAL_ENV"))
        )
        print("Environment Path:", os.environ.get("VIRTUAL_ENV"))

    else:
        print("Virtual Environment: None detected")


def main() -> None:

    if is_in_venv():
        print("MATRIX STATUS: Welcome to the construct")
    else:
        print("MATRIX STATUS: You're still plugged in")
    print()

    print()
    display_env_info()
    print()

    if is_in_venv():
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print(site.getsitepackages()[0])

    else:
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print()

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate    # On Windows")

        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()

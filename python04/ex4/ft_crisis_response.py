
def crisis_handler(filename: str) -> None:
    """
    Handle archive access with full crisis management.

    The function attempts to open and read the specified archive file
    using a context manager. It prints a success message if the access
    succeeds, or displays appropriate crisis responses for missing
    files, permission issues, or unexpected system anomalies.
    """
    try:
        if filename == "standard_archive.txt":
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        with open(filename, "r") as f:
            data: str = f.read()
            print(f"SUCCESS: Archive recovered - ``{data}''")
            print("STATUS: Normal operations resumed")
            return

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
        print()

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
        print()

    except Exception:
        print("RESPONSE: Unexpected system anomaly")
        print("STATUS: Crisis handled, system stable")
        print()


def main() -> None:
    """
    Execute the Cyber Archives crisis response workflow.

    The function initializes the crisis response system and tests
    multiple archive access scenarios by invoking the crisis handler
    on predefined archive files.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()

    crisis_handler("lost_archive.txt")

    crisis_handler("classified_vault.txt")

    crisis_handler("standard_archive.txt")

    print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()

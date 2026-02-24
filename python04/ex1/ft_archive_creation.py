
def main() -> None:
    """
    Create a new archive file and write preservation entries.

    The function initializes the archive system, creates the file
    'new_discovery.txt' in write mode, records three predefined
    entries, and displays status messages in the terminal.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    print("Initializing new storage unit: new_discovery.txt")
    try:
        f = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")

        print("Inscribing preservation data...")
        print("[ENTRY 001] New quantum algorithm discovered")
        f.write("[ENTRY 001] New quantum algorithm discovered\n")

        print("[ENTRY 002] Efficiency increased by 347%")
        f.write("[ENTRY 002] Efficiency increased by 347%\n")

        print("[ENTRY 003] Archived by Data Archivist trainee\n")
        f.write("[ENTRY 003] Archived by Data Archivist trainee\n")

        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
        f.close()

    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

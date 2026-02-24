
def main() -> None:
    """
    Recover and display data from ancient_fragment.txt.

    Opens the storage vault, reads its contents,
    and prints the recovered data. Handles the case
    where the file is missing.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        with open("ancient_fragment.txt", "r") as f:
            print("Connection established...", end="\n\n")
            print("RECOVERED DATA:")
            data: str = f.read()
            print(data, end="\n\n")
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()

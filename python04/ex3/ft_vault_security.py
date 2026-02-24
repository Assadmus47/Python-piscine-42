
def main() -> None:
    try:
        print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
        print()
        print("Initiating secure vault access...")

        with open("classified_data.txt", "r") as f:
            print("Vault connection established with failsafe protocols\n")
            data: str = f.read()
            print("SECURE EXTRACTION:")
            print(data)

        print()

        with open("security_protocols.txt", "w") as f:
            print("SECURE PRESERVATION:")
            f.write("[CLASSIFIED] New security protocols archived\n")
            print("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion")
        print()
        print("All vault operations completed with maximum security.")

    except Exception as e:
        print("ERROR: Vault operation failed")
        print(f"DETAILS: {e}")


if __name__ == "__main__":
    main()

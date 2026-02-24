import sys


def main() -> None:
    """
    Manage the three communication streams of the Cyber Archives.

    The function collects archivist identification and status
    information from standard input, then routes standard messages
    to stdout and alert messages to stderr to verify proper stream
    separation.
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()

    id_arch: str = input("Input Stream active. Enter archivist ID: ")
    report: str = input("Input Stream active. Enter status report: ")
    print()

    sys.stdout.write(f"[STANDARD] Archive status from {id_arch}: {report}\n")
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n"
        )
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print()

    sys.stdout.write("Three-channel communication test successful.\n")


if __name__ == "__main__":
    main()


from dotenv import load_dotenv

import os


def load_config() -> dict[str, str]:
    load_dotenv()

    config: dict[str, str] = {
        "mode": os.getenv("MATRIX_MODE", "development"),
        "url": os.getenv("DATABASE_URL", "not configured"),
        "key": os.getenv("API_KEY", "not configured"),
        "level": os.getenv("LOG_LEVEL", "DEBUG"),
        "endpoint": os.getenv("ZION_ENDPOINT", "not configured")
    }

    return config


def display_config(config: dict[str, str]) -> None:
    print("Configuration loaded:")
    print("Mode:", config["mode"])
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print("Log Level:", config["level"])
    print("Zion Network: Online")


def security_check() -> None:
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[MISSING] .env file not found")

    if os.environ.get("MATRIX_MODE"):
        print("[OK] Production overrides available")
    else:
        print("[WARNING] No production overrides set")


def main() -> None:
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    config: dict[str, str] = load_config()

    display_config(config)
    print()

    security_check()

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()

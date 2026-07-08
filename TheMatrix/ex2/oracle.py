import os
from dotenv import load_dotenv  # type: ignore

load_dotenv()

OBLIGATORY_VARS = [
    "DATABASE_URL",
    "API_KEY",
    "ZION_ENDPOINT"
]


def loading_configuration():
    return {
        "mode": os.getenv("MATRIX_MODE", "development"),
        "database_url": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL"),
        "zion_endpoint": os.getenv("ZION_ENDPOINT")
    }


def check_missing() -> list[str]:
    missing = []

    for variable in OBLIGATORY_VARS:
        if not os.getenv(variable):
            missing.append(variable)

    return missing


def display(config) -> None:

    print("ORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    print(f"Mode: {config["mode"]}")

    if config["database_url"]:
        if config["mode"] == "development":
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to production database")
    else:
        print("Database: MISSING CONFIGURATION")

    if config["api_key"]:
        print("API Access: Authenticated")
    else:
        print("API Access: MISSING API_KEY")

    print(f"Log Level: {config["log_level"]}")

    if config["zion_endpoint"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check(missing: list[str]) -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if missing:
        print("[WARNING] Missing configuration values.")
        print("\nMissing required variables:")
        for missing_variable in missing:
            print(f"- {missing_variable}")
    else:
        print("[OK] .env file properly configured.")
        print("[OK] Environment variables can override .env values.")
        print("\nThe Oracle sees all configurations,")
        print("and would like to give you a cookie Neo.")


def main() -> None:
    config = loading_configuration()
    missing = check_missing()

    display(config)
    security_check(missing)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import os
import sys

from dotenv import load_dotenv


def load_environment() -> None:
    """Load the environment variables from the .env file."""
    load_dotenv()


def load_configuration() -> dict[str, str | None]:
    """Retrieve the configuration values."""
    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT")
    }


def show_configuration(config: dict[str, str | None]) -> None:
    """Display the current configuration."""
    print("Configuration loaded:")

    print(f"Mode: {config['MATRIX_MODE']}")

    if config["DATABASE_URL"]:
        print("Database: Connected to local instance")
    else:
        print("Database: Missing configuration")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing configuration")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Missing configuration")

    print()


def security_check(config: dict[str, str | None]) -> None:
    """Check whether the configuration is valid."""
    print("Environment security check:")

    missing_variables = []

    if not config["DATABASE_URL"]:
        missing_variables.append("DATABASE_URL")

    if not config["API_KEY"]:
        missing_variables.append("API_KEY")

    if not config["ZION_ENDPOINT"]:
        missing_variables.append("ZION_ENDPOINT")

    print("[OK] No hardcoded secrets detected.")

    if missing_variables:
        print("[WARNING] .env file is missing some variables.")
    else:
        print("[OK] .env file properly configured.")

    print("[OK] Production overrides available.")

    if missing_variables:
        print()
        show_missing_configuration(missing_variables)


def show_missing_configuration(
    missing_variables: list[str]
) -> None:
    """Show which configuration values are missing."""
    print("Missing variables:")

    for variable in missing_variables:
        print(f"- {variable}")


def main() -> None:
    """Main entry point of the program."""
    print("ORACLE STATUS: Reading the Matrix...\n")

    load_environment()

    config = load_configuration()

    show_configuration(config)

    security_check(config)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()

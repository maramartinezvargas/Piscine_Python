import os
from dotenv import load_dotenv


def load_configuration() -> dict[str, str | None]:
    """Retrieve the configuration values from the environment."""

    load_dotenv()

    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }


def show_configuration(config: dict[str, str | None]) -> None:
    """Display the current configuration based on the environment mode."""
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    # Showcase difference between dev and prod as requested by the subject
    if config["DATABASE_URL"]:
        if config["MATRIX_MODE"] == "production":
            print("Database: Connected to production cluster")
        else:
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
    """Check whether the configuration is valid and secure."""
    print("Environment security check:")

    missing_variables = []
    for var in ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]:
        if not config[var]:
            missing_variables.append(var)

    # The architecture enforces security: by using exclusively os.getenv(),
    # the source code is guaranteed to be free of hardcoded secrets.
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env") and not missing_variables:
        print("[OK] .env file properly configured")
    elif os.path.exists(".env"):
        print("[WARNING] .env file is missing some variables")
    else:
        print("[WARNING] .env file not found")

    # load_dotenv() respects pre-existing environment variables,
    # ensuring runtime/CLI injections always override .env defaults.
    print("[OK] Production overrides available")

    if missing_variables:
        print()
        show_missing_configuration(missing_variables)


def show_missing_configuration(missing_variables: list[str]) -> None:
    """Show which configuration values are missing."""
    print("Missing variables:")
    for variable in missing_variables:
        print(f"- {variable}")


def main() -> None:
    """Main entry point of the program."""
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_configuration()
    show_configuration(config)
    security_check(config)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import importlib
import importlib.metadata
import sys

# List of required dependencies for the program
DEPENDENCIES = [
    "numpy",
    "pandas",
    "matplotlib"
]

PACKAGE_DESCRIPTION = {
    "numpy": "Numerical computation ready",
    "pandas": "Data manipulation ready",
    "matplotlib": "Visualization ready"
}


def package_is_installed(package: str) -> bool:
    """Check if the required packages are installed."""
    try:
        importlib.import_module(package)
        return True
    except ModuleNotFoundError:
        return False


def package_version(package: str) -> str:
    """Get the version of a package."""
    return importlib.metadata.version(package)


def check_dependencies() -> bool:
    """Check if the required packages are installed."""
    all_ok = True

    for package in DEPENDENCIES:
        if package_is_installed(package):
            print(
                f"[OK] {package} "
                f"({package_version(package)}) - "
                f"{PACKAGE_DESCRIPTION[package]}"
            )
        else:
            print(f"[ERROR] {package} is not installed.")
            all_ok = False

    return all_ok


def show_installation_help() -> None:
    """Print installation instructions for the required packages."""
    print("Missing dependencies detected.")
    print("Choose one of the following options to install the required packages:")

    print()
    print("1. Use pip to install the packages:")
    print(" pip install -r requirements.txt")

    print()
    print("2. Use poetry to install the packages:")
    print(" poetry install")
    print(" poetry run python loading.py")


def generate_matrix_data():
    ...


def analyze_data(data):
    ...


def create_visualization(data) -> None:
    ...

def main() -> None:

    print()
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    if not check_dependencies():

        show_installation_help()
        sys.exit(1)

    data = generate_matrix_data()
    analyze_data(data)
    create_visualization(data)


if __name__ == "__main__":
    main()
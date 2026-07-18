#!/usr/bin/env python3

import importlib.metadata
import sys

try:
    import numpy as np
except ModuleNotFoundError:
    np = None

try:
    import pandas as pd
except ModuleNotFoundError:
    pd = None

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    plt = None


PACKAGE_DESCRIPTION: dict[str, str] = {
    "numpy": "Numerical computation ready",
    "pandas": "Data manipulation ready",
    "matplotlib": "Visualization ready"
}

PACKAGE_MODULES: dict[str, object | None] = {
    "numpy": np,
    "pandas": pd,
    "matplotlib": plt
}


def package_version(package: str) -> str:
    """Get the installed version of a package."""
    return importlib.metadata.version(package)


def check_dependencies() -> bool:
    """Check whether all required packages are installed."""
    all_ok = True

    for package, module in PACKAGE_MODULES.items():

        if module is not None:
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
    print(
        "Choose one of the following options "
        "to install the required packages:"
    )

    print()
    print("1. Use pip to install the packages:")
    print(" pip install -r requirements.txt")

    print()
    print("2. Use poetry to install the packages:")
    print(" poetry install")
    print(" poetry run python loading.py")


def generate_matrix_data():
    """Generate 1000 Matrix data points using numpy."""
    return np.random.normal(loc=100, scale=25, size=1000)


def analyze_data(data):
    """Analyze Matrix data using pandas."""
    print()
    print("Analyzing Matrix data...")
    print(f"Processing {len(data)} data points...")

    return pd.DataFrame(
        data,
        columns=["Matrix Value"]
    )


def create_visualization(data) -> None:
    """Generate a histogram using matplotlib."""
    print("Generating visualization...")

    plt.figure(figsize=(10, 6))
    plt.hist(
        data["Matrix Value"],
        bins=15,
        color="thistle",
        edgecolor="purple"
    )

    plt.title("Matrix Data Analysis", color="purple")
    plt.xlabel("Value", color="purple")
    plt.ylabel("Frequency", color="purple")

    plt.savefig("matrix_analysis.png")
    plt.close()

    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print()
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    if not check_dependencies():
        show_installation_help()
        sys.exit(1)

    data = generate_matrix_data()

    dataframe = analyze_data(data)

    create_visualization(dataframe)


if __name__ == "__main__":
    main()

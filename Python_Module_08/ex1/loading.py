#!/usr/bin/env python3

from typing import Any
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
    import requests as rq
except ModuleNotFoundError:
    rq = None

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    plt = None


PACKAGE_DESCRIPTION: dict[str, str] = {
    "numpy": "Numerical computation ready",
    "pandas": "Data manipulation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready"
}

PACKAGE_MODULES: dict[str, object] = {
    "numpy": np,
    "pandas": pd,
    "requests": rq,
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
            status_tag = f"[OK] {package} ({package_version(package)})"
            print(f"{status_tag:<30} {PACKAGE_DESCRIPTION[package]}")
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


def generate_matrix_data() -> Any:
    """Generate 1000 Matrix data points using numpy."""
    return np.random.normal(loc=100, scale=25, size=1000)


def analyze_data(data: Any) -> Any:
    """Analyze Matrix data using pandas."""
    print()
    print("Analyzing Matrix data...")
    print(f"Processing {len(data)} data points...")

    return pd.DataFrame(
        data,
        columns=["Matrix Value"]
    )


def create_visualization(data: Any) -> None:
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

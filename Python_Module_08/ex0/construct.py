#!/usr/bin/env python3

import os
import sys
import site


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def detect_virtual_env() -> None:
    current_path = sys.executable

    if not is_virtual_env():
        print("MATRIX STATUS: You're still plugged in")

        print()
        print(f"Current Python: {current_path}")
        print("Virtual Environment: None detected")

        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")

        print()
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")

        print()
        print(f"Current Python: {current_path}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")

        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        print()
        print("Package installation path:")
        print(site.getsitepackages()[0])


if __name__ == "__main__":
    detect_virtual_env()

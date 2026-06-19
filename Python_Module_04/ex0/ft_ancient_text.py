#!/usr/bin/env python3

import sys


def ft_ancient_text() -> None:
    """Reads and prints the content of a specified file."""
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    filename: str = sys.argv[1]
    print(f"Accessing file '{filename}'")
    file = None
    try:
        file = open(filename, "r")
        print("---\n")
        print(file.read(), end="")
        print("\n---")
        file.close()
        print(f"File '{filename}' closed.")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    ft_ancient_text()

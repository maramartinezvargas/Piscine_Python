#!/usr/bin/env python3

import sys


def ft_ancient_text() -> None:
    """Reads and prints the content of a specified file."""
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        filename: str = sys.argv[1]
        print(f"Accessing file '{filename}'")
        file = None
        try:
            file = open(filename, "r")
            print("---")
            print(file.read(), end="")
            print("\n---")
            print(f"File '{filename}' closed.")
            file.close()
        except OSError as e:
            print(f"Error opening file '{filename}': {e}")
        finally:
            if file is not None:
                file.close()


if __name__ == "__main__":
    ft_ancient_text()

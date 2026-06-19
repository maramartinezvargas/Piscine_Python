#!/usr/bin/env python3

import sys


def ft_ancient_text() -> None:
    """Reads and prints the content of a specified file,
    transforms the content by replacing newlines with '#',
    and optionally saves the transformed content to a new file."""
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    filename: str = sys.argv[1]
    print(f"Accessing file '{filename}'")
    try:
        file = open(filename, "r")
        print("---")
        content = file.read()
        print(content, end="")
        file.close()
        print(f"File '{filename}' closed.")
        print("\n---")

        print("Transform data:")
        print("---")
        transformed_content: str = content.replace("\n", "#\n")
        print(transformed_content, end="")

        print("\n---")
        save_in = input("Enter new file name (or empty): ")
        if save_in == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{save_in}'")
            new_file = open(save_in, 'w')
            new_file.write(transformed_content)
            print(f"Data saved in file '{save_in}'.")
            new_file.close()
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    ft_ancient_text()

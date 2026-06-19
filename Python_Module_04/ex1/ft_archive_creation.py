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
    new_file = None
    try:
        file = open(filename, "r")
        print("---")
        content = file.read()
        print(content, end="")
        print("\n---")
        print(f"File '{filename}' closed.")
        file.close()

        print("Transform data:")
        print("---")
        transformed_content: str = ""
        file = open(filename, 'r')
        for line in file:
            transformed_content += line.replace("\n", "#\n")
        file.close()
        transformed_content = transformed_content + "#"
        print(transformed_content, end="")

        print("\n---")
        save_in = input("Enter new file name (or empty): ")
        if save_in == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{save_in}'")
            new_file = open(save_in, 'w')
            new_file.write(transformed_content)
            print(f"Data saved in file '{save_in}'")
            new_file.close()
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file is not None:
            file.close()
        if new_file is not None:
            new_file.close()


if __name__ == "__main__":
    ft_ancient_text()

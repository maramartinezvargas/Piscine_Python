#!/usr/bin/env python3

import sys


def ft_stream_management() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    filename: str = sys.argv[1]
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, "r")
        print("---")
        content = file.read()
        print(content, end="")
        print("---")
        file.close()
        print(f"File '{filename}' closed.")

    except OSError as e:
        print(f"[STDERR] Error opening file '{filename}': {e}",
              file=sys.stderr)
        return

    print("Transform data:")
    print("---")
    transformed_content: str = content.replace("\n", "#\n")
    print(transformed_content, end="")
    print("\n---")

    print("Enter new file name (or empty):")
    save_in = sys.stdin.readline().rstrip("\n")
    if save_in == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{save_in}'")

    try:
        new_file = open(save_in, "w")
        new_file.write(transformed_content)
        new_file.close()

        print(f"Data saved in file '{save_in}'.")

    except OSError as e:
        print(f"[STDERR] Error opening file '{save_in}': {e}",
              file=sys.stderr)
        print("Data not saved.")


if __name__ == "__main__":
    ft_stream_management()

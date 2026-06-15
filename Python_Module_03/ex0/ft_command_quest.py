#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    len: int = len(sys.argv)
    i: int = 0

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv.pop(0)}")

    if len > 1:
        print(f"Arguments received: {len - 1}")
    else:
        print("No arguments provided!")

    for arg in (sys.argv):
        i += 1
        print(f"Argument {i}: {arg}")

    print(f"Total arguments: {len}")

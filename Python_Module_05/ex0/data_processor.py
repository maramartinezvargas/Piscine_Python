#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise ValueError("No data available")
        return self._data.pop(0)


class NumericProcessor(DataProcessor):

    def _is_valid_number(self, data: Any) -> bool:
        return isinstance(data, (int, float)) and not isinstance(data, bool)

    def validate(self, data: Any) -> bool:
        if self._is_valid_number(data):
            return True

        if isinstance(data, list):
            return all(self._is_valid_number(item) for item in data)

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._data.append((self._count, str(item)))
                self._count += 1
        else:
            self._data.append((self._count, str(data)))
            self._count += 1


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._data.append((self._count, item))
                self._count += 1
        else:
            self._data.append((self._count, data))
            self._count += 1


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )

        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in item.items()
                )
                for item in data
            )

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for item in data:
                log = (
                    f"{item.get('log_level', 'UNKNOWN')}: "
                    f"{item.get('log_message', '')}"
                )
                self._data.append((self._count, log))
                self._count += 1
        else:
            log = (
                f"{data.get('log_level', 'UNKNOWN')}: "
                f"{data.get('log_message', '')}"
            )
            self._data.append((self._count, log))
            self._count += 1


def code_nexus() -> None:
    print("=== Code Nexus - Data Processor ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    # Testing NumericProcessor
    print("\nTesting Numeric Processor...")
    print("Trying to validate input '42':", numeric.validate(42))
    print("Trying to validate input 'Hello':", numeric.validate("Hello"))

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        # error intentional: passing invalid type to test runtime exception
        # mypy will flag this as an error, but we want to test runtime behavior
        numeric.ingest("foo")
    except ValueError as e:
        print("Got exception:", e)

    numbers: list[int | float] = [1, 2, 3, 4, 5]
    print("Processing data:", numbers)
    numeric.ingest(numbers)

    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")

    # Testing TextProcessor
    print("\nTesting Text Processor...")
    print("Trying to validate input '42':", text.validate(42))

    words: list[str] = ["Hello", "Nexus", "World"]
    print("Processing data:", words)
    text.ingest(words)

    print("Extracting 1 value...")
    rank, value = text.output()
    print(f"Text value {rank}: {value}")

    # Testing LogProcessor
    print("\nTesting Log Processor...")
    print("Trying to validate input 'Hello':", log.validate("Hello"))

    logs: list[dict[str, str]] = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server"
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!"
        }
    ]

    print("Processing data:", logs)
    log.ingest(logs)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    code_nexus()

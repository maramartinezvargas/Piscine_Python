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

    def total_processed(self) -> int:
        return self._count

    def remaining(self) -> int:
        return len(self._data)


class NumericProcessor(DataProcessor):

    def _is_valid_number(self, data: Any) -> bool:
        return isinstance(data, (int, float)) and \
            not isinstance(data, bool)

    def validate(self, data: Any) -> bool:
        if self._is_valid_number(data):
            return True

        if isinstance(data, list):
            return all(
                self._is_valid_number(item)
                for item in data
            )

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
            return all(
                isinstance(item, str)
                for item in data
            )

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
                isinstance(key, str)
                and isinstance(value, str)
                for key, value in data.items()
            )

        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(key, str)
                    and isinstance(value, str)
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


class DataStream:

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:

        for element in stream:
            processed = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break

            if not processed:
                print(
                    "DataStream error - "
                    "Can't process element in stream:",
                    element
                )

    def print_processors_stats(self) -> None:

        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:

            name = proc.__class__.__name__.replace(
                "Processor",
                " Processor"
            )

            print(
                f"{name}: total "
                f"{proc.total_processed()} "
                f"items processed, "
                f"remaining "
                f"{proc.remaining()} "
                f"on processor"
            )


def code_nexus() -> None:

    print("=== Code Nexus - Data Stream ===")

    stream = DataStream()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    data: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message":
                "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message":
                "User wil is connected"
            }
        ],
        42,
        ["Hi", "five"]
    ]

    print("\nInitialize Data Stream...")
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    stream.register_processor(numeric)

    print("Send first batch of data on stream:", data)

    stream.process_stream(data)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    stream.register_processor(text)
    stream.register_processor(log)

    print("Send the same batch again")
    stream.process_stream(data)
    stream.print_processors_stats()

    print(
        "\nConsume some elements from "
        "the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        numeric.output()

    for _ in range(2):
        text.output()

    for _ in range(1):
        log.output()

    stream.print_processors_stats()

    print()
    print(
        "Polymorphism allows DataStream "
        "to interact with all processors "
        "through the common DataProcessor "
        "interface without knowing their "
        "concrete implementations."
    )

    print(
        "Benefits: extensibility, low "
        "coupling, code reuse and easier "
        "maintenance."
    )


if __name__ == "__main__":
    code_nexus()

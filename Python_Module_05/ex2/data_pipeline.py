#!/usr/bin/env python3

from typing import Any, Protocol
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

        if self._is_valid_log(data):
            return True

        if isinstance(data, list):
            return all(self._is_valid_log(item) for item in data)

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

    def _is_valid_log(self, data: Any) -> bool:

        return (
            isinstance(data, dict)
            and "log_level" in data
            and "log_message" in data
            and isinstance(data["log_level"], str)
            and isinstance(data["log_message"], str)
        )


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:

        values = [value for _, value in data]

        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:

        items: list[str] = []

        for index, value in data:
            escaped = (value.replace("\\", "\\\\").replace('"', '\\"'))
            items.append(f'"item_{index}": "{escaped}"')

        print("JSON Output:")
        print("{" + ", ".join(items) + "}")


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

        print("\n== DataStream statistics ==")

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:

        if nb <= 0:
            raise ValueError(
                "Number of elements must be positive"
            )

        for proc in self._processors:

            output_data: list[tuple[int, str]] = []

            for _ in range(nb):

                if proc.remaining() == 0:
                    break

                output_data.append(proc.output())

            if output_data:
                plugin.process_output(output_data)


def code_nexus() -> None:

    print("=== Code Nexus - Data Pipeline ===")

    stream = DataStream()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    csv_plugin = CSVExportPlugin()
    json_plugin = JSONExportPlugin()

    data = [
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

    print("\nRegistering Processors")

    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    print("\nSend first batch of data on stream:", data)

    stream.process_stream(data)
    stream.print_processors_stats()

    print(
        "\nSend 3 processed data "
        "from each processor to a CSV plugin:"
    )

    stream.output_pipeline(3, csv_plugin)

    stream.print_processors_stats()

    second_batch = [
        21,
        [
            "I love AI",
            "LLMs are wonderful",
            "Stay healthy"
        ],
        [
            {
                "log_level": "ERROR",
                "log_message":
                "500 server crash"
            },
            {
                "log_level": "NOTICE",
                "log_message":
                "Certificate expires in 10 days"
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    print("\nSend another batch of data:", second_batch)

    stream.process_stream(second_batch)
    stream.print_processors_stats()

    print(
        "\nSend 5 processed data "
        "from each processor to a JSON plugin:"
    )

    stream.output_pipeline(5, json_plugin)

    stream.print_processors_stats()


if __name__ == "__main__":
    code_nexus()

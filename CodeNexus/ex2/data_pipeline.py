#!/usr/bin/python3

from abc import ABC, abstractmethod
import typing
from typing import Any
from typing import Protocol

data_list = [
            "Hello world", [3.14, -1, 2.71],
            [{"log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"},
                {"log_level": "INFO",
                    "log_message": "User wil is connected"}],
            42, ["Hi", "five"]]

data_list2 = [
    21, ["I love AI", "LLMs are wonderful", "Stay healthy"],
    [{"log_level": "ERROR", "log_message": "500 server crash"},
     {"log_level": "NOTICE", "log_message": "Certificate expires in 10 days"}],
    [32, 42, 64, 84, 128, 168], "World hello"
    ]


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.storage: list[str] = []
        self.rank = 0
        self.item_processed = 0

    def output(self) -> tuple[int, str]:

        if (len(self.storage) == 0):
            raise ValueError("Cannot pop from an empty storage !")

        value = self.storage.pop(0)

        current_rank = self.rank

        self.rank += 1

        return (current_rank, value)

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def asingest(self, data: Any) -> None:
        pass


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if (isinstance(data, (int, float))):
            return True

        elif (isinstance(data, list)):
            for i in data:
                if not isinstance(i, (int, float)):
                    return False
            return True

        else:
            return False

    def asingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Cannot ingest data that is not numeric !")

        elif (isinstance(data, list)):
            for item in data:
                self.item_processed += 1
                self.storage.append(str(item))

        else:
            self.item_processed += 1
            self.storage.append(str(data))


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if (isinstance(data, str)):
            return True

        elif (isinstance(data, list)):
            for i in data:
                if not isinstance(i, (str)):
                    return False
            return True
        else:
            return False

    def asingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Cannot ingest data that is not text !")

        elif (isinstance(data, list)):
            for item in data:
                self.item_processed += 1
                self.storage.append(item)
        else:
            self.item_processed += 1
            self.storage.append(data)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if (isinstance(data, dict)):
            return self._is_valid(data)

        elif (isinstance(data, list)):
            for log in data:
                if not self._is_valid(log):
                    return False
            return True

        else:
            return False

    def _is_valid(self, log: Any):
        if not isinstance(log, dict):
            return False

        if "log_level" not in log:
            return False

        if "log_message" not in log:
            return False

        if not isinstance(log["log_level"], str):
            return False

        if not isinstance(log["log_message"], str):
            return False

        return True

    def asingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Cannot ingest data that is not in log type !")

        if isinstance(data, list):
            for log in data:
                self.item_processed += 1
                self.storage.append(f"{log["log_level"]}: "
                                    f"{log["log_message"]}")
        else:
            self.item_processed += 1
            self.storage.append(f"{data["log_level"]}: {data["log_message"]}")


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        self.error_activate = False

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:

        if len(self.processors) == 0:
            print("No processor found, no data")
            return

        for data in stream:
            processed = False

            for proc in self.processors:
                if (proc.validate(data)):

                    proc.asingest(data)

                    processed = True

                    break

            if not processed and self.error_activate:
                print("DataStream error - Can’t process "
                      f"element in stream: {data}\n")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:

        for proc in self.processors:
            output_data = []

            for _ in range(nb):
                try:
                    output_data.append(proc.output())
                except ValueError:
                    break

            if len(output_data) > 0:
                plugin.process_output(output_data)


class CSVExportPlugin():

    def process_output(self, data: list[tuple[int, str]]) -> None:

        values = []

        for _, value in data:
            values.append(value)

        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin():

    def process_output(self, data: list[tuple[int, str]]) -> None:

        values = []

        for rank, value in data:
            values.append(f'"item_{rank}": "{value}"')

        print("JSON Output:")
        print("{" + ",".join(values) + "}")


def main() -> None:

    stream = DataStream()

    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    print("== DataStream statistics ==")
    # using the function without any processor to print the error code
    stream.process_stream(data_list)
    print("\nRegistering Processors...\n")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    csv_plugin = CSVExportPlugin()
    json_plugin = JSONExportPlugin()

    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    print(f"Send first batch of data on stream: {data_list}\n")
    stream.process_stream(data_list)

    print("== DataStream statistics ==")
    print(f"Numeric Processor: total {numeric.item_processed} items processed,"
          f" remaining {len(numeric.storage)} on processor\n")

    print(f"Text Processor: total {text.item_processed} items processed, "
          f"remaining {len(text.storage)} on processor\n")

    print(f"Log Processor: total {log.item_processed} items processed, "
          f"remaining {len(log.storage)} on processor\n")

    print("Send 3 processed data from each processor to a CSV plugin:")

    stream.output_pipeline(3, csv_plugin)

    print("\n== DataStream statistics ==")
    print(f"Numeric Processor: total {numeric.item_processed} items processed,"
          f" remaining {len(numeric.storage)} on processor\n")

    print(f"Text Processor: total {text.item_processed} items processed, "
          f"remaining {len(text.storage)} on processor\n")

    print(f"Log Processor: total {log.item_processed} items processed, "
          f"remaining {len(log.storage)} on processor\n")

    # data list 2

    stream.process_stream(data_list2)
    print(f"Send second batch of data on stream: {data_list2}\n")
    print("== DataStream statistics ==")
    print(f"Numeric Processor: total {numeric.item_processed} items processed"
          f", remaining {len(numeric.storage)} on processor\n")

    print(f"Text Processor: total {text.item_processed} items processed, "
          f"remaining {len(text.storage)} on processor\n")

    print(f"Log Processor: total {log.item_processed} items processed, "
          f"remaining {len(log.storage)} on processor\n")

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, json_plugin)

    print("\n== DataStream statistics ==")
    print(f"Numeric Processor: total {numeric.item_processed} items processed"
          f", remaining {len(numeric.storage)} on processor\n")

    print(f"Text Processor: total {text.item_processed} items processed, "
          f"remaining {len(text.storage)} on processor\n")

    print(f"Log Processor: total {log.item_processed} items processed, "
          f"remaining {len(log.storage)} on processor\n")

    print("=== End ===")


if __name__ == "__main__":
    main()

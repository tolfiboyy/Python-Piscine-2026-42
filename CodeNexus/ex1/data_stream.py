#!/usr/bin/python3

from abc import ABC, abstractmethod
import typing
from typing import Any


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


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        self.error_activate = False

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
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


def main() -> None:

    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    print("== DataStream statistics ==")
    print("No processor found, no data\n")
    print("Registering Numeric Processor\n")

    stream = DataStream()
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    data_list = [
            "Hello world", [3.14, -1, 2.71],
            [{"log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"},
                {"log_level": "INFO",
                    "log_message": "User wil is connected"}],
            42, ["Hi", "five"]]

    stream.register_processor(numeric)

    print(f"Send first batch of data on stream: {data_list}\n")
    # activate the error printing or not as you wish :)
    stream.error_activate = True
    stream.process_stream(data_list)

    print("== DataStream statistics ==")
    print(f"Numeric Processor: total {numeric.item_processed} items processed,"
          f" remaining {len(numeric.storage)} on processor\n")

    print("Register other data processors\nSend the same batch again\n")
    print("== DataStream statistics ==\n")

    stream.error_activate = False
    stream.register_processor(log)
    stream.register_processor(text)
    stream.process_stream(data_list)

    print(f"Numeric Processor: total {numeric.item_processed} items processed,"
          f" remaining {len(numeric.storage)} on processor\n")

    print(f"Text Processor: total {text.item_processed} items processed, "
          f"remaining {len(text.storage)} on processor\n")

    print(f"Log Processor: total {log.item_processed} items processed, "
          f"remaining {len(log.storage)} on processor\n")

    # la on output des elements du storage ta capte

    numeric_output = 3
    text_output = 2
    log_output = 1

    for _ in range(numeric_output):
        numeric.output()

    for _ in range(text_output):
        text.output()

    for _ in range(log_output):
        log.output()

    print("Consumed elements from the data processors: "
          f"Numeric {numeric_output}, "
          f"Text {text_output}, "
          f"Log {log_output}\n")

    print("== DataStream statistics ==\n")

    print(f"Numeric Processor: total {numeric.item_processed} items processed,"
          f" remaining {len(numeric.storage)} on processor\n")

    print(f"Text Processor: total {text.item_processed} items processed, "
          f"remaining {len(text.storage)} on processor\n")

    print(f"Log Processor: total {log.item_processed} items processed, "
          f"remaining {len(log.storage)} on processor\n")

    print("=== End ===")


if __name__ == "__main__":
    main()

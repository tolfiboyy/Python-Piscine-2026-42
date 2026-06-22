#!/usr/bin/python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.storage: list[str] = []
        self.rank = 0

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
                self.storage.append(str(item))

        else:
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
                self.storage.append(item)
        else:
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
                self.storage.append(f"{log["log_level"]}: "
                                    f"{log["log_message"]}")
        else:
            self.storage.append(f"{data["log_level"]}: {data["log_message"]}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    # Numeric Processing

    numericvalue = NumericProcessor()
    print("=== Testing numeric processor...\n")
    print("Trying to validate input '42': ", numericvalue.validate(42))
    print("Trying to validate input 'Hello': ", numericvalue.validate("Hello"))

    print("Test invalid ingestion of string ’foo’ without prior validation:")
    try:
        numericvalue.asingest("hello")
    except ValueError as error:
        print(error)

    data_list = [1, 2, 3, 4, 5]
    print("\nProcessing data: ", data_list)
    numericvalue.asingest(data_list)

    print("Extracting 3 values ...")
    for i in range(3):
        rank, value = numericvalue.output()
        print(f"Numeric value {rank}: {value}")

    # Text Processing
    print()

    textvalue = TextProcessor()
    print("=== Testing text processor...\n")
    print("Trying to validate input '42': ", textvalue.validate(42))

    print("Test invalid ingestion of float '42.2' without prior validation:")
    try:
        textvalue.asingest(42.2)
    except ValueError as error:
        print(error)

    txt_list = ["Hello", "Nexus", "World"]
    textvalue.asingest(txt_list)
    print("\nProcessing data: ", txt_list)

    print("Extracting 1 value...")
    for i in range(1):
        rank, value = textvalue.output()
        print(f"Text value {rank}: {value}")

    # Log Processing
    print()

    log = LogProcessor()
    print("=== Testing log processor...\n")
    print("Trying to validate input ’Hello’: ", log.validate("Hello"))

    print("Trying to validate input ’foolish_error’"
          " without prior validation: ")
    try:
        log.asingest({"log_level": "error"})
    except ValueError as error:
        print(error)

    log_data = [

        {"log_level": "NOTICE",
         "log_message": "Connection to server"},

        {"log_level": "ERROR",
         "log_message": "Unauthorized access!!"}

        ]
    log.asingest(log_data)
    print("\nProcessing data: ", log_data)

    print("Extracting 2 values...")
    for i in range(2):
        rank, value = log.output()
        print(f"{rank}: {value}")

    print("\n=== END ===")


if __name__ == "__main__":
    main()

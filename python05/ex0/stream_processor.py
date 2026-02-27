

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    Abstract base class defining the interface for all data processors.

    Each processor must implement validation and processing logic while
    optionally using the shared output formatting behavior.
    """
    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate the input data for the specific processor.

        Args:
            data (Any): The input data to validate.

        Returns:
            bool: True if the data is valid, False otherwise.
        """
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the input data after validation.

        Args:
            data (Any): The input data to process.

        Returns:
            str: The formatted processing result.
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Format the final output string for processors.

        Args:
            result (str): The raw result string.

        Returns:
            str: The formatted output prefixed with 'Output:'.
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    Processor specialized in handling numeric list data.

    Validates that the input is a non-empty list of numbers and
    computes basic statistics (count, sum, average).
    """
    def validate(self, data: Any) -> bool:
        """
        Validate that the input is a non-empty list of int or float.

        Args:
            data (Any): The input data to validate.

        Returns:
            bool: True if the data is a valid numeric list.
        """
        if type(data) is not list:
            return False

        count: int = 0
        for x in data:
            count += 1
            if type(x) is bool:
                return False
            if type(x) is not int and type(x) is not float:
                return False

        return count > 0

    def process(self, data: Any) -> str:
        """
        Process numeric data and compute statistics.

        Args:
            data (Any): The numeric list to process.

        Returns:
            str: Formatted statistics or error output.
        """
        try:
            print(f"Processing data: {data}")

            if not self.validate(data):
                raise ValueError("Invalid Data")

            print("Validation: Numeric data verified")
            info: dict[str, int | float] = self.info(data)
            result: str = f'Processed {info["len"]} numeric '
            f'values, sum={info["sum"]}, avg={info["avg"]:.1f}'
            return self.format_output(result)
        except ValueError as e:
            print(e)
            return self.format_output("ERROR")

    def info(self, data: Any) -> dict[str, int | float]:
        """
        Compute numeric statistics from the data.

        Args:
            data (Any): Validated numeric list.

        Returns:
            dict[str, int | float]: Dictionary containing length,
            sum, and average of the numbers.
        """
        length: int = 0
        somme: float = 0

        for i in data:
            length += 1
            somme = somme + i

        average: float = somme / length
        return {"len": length, "sum": somme, "avg": average}


class TextProcessor(DataProcessor):
    """
    Processor specialized in handling textual data.

    Validates string input and computes character and word counts.
    """
    def validate(self, data: Any) -> bool:
        """
        Validate that the input is a non-empty string.

        Args:
            data (Any): The input data to validate.

        Returns:
            bool: True if the data is a valid string.
        """
        if type(data) is not str:
            return False
        if data == "":
            return False
        return True

    def process(self, data: Any) -> str:
        """
        Process text data and compute character and word counts.

        Args:
            data (Any): The text to process.

        Returns:
            str: Formatted text statistics or error output.
        """
        try:
            print(f"Processing data: \"{data}\"")
            if not self.validate(data):
                raise ValueError("Invalid Data")
            print("Validation: Text data verified")
            char, words = self.count_chars_words(data)
            result: str = f'Processed text: {char} characters, {words} words'
            return self.format_output(result)
        except ValueError as e:
            print(e)
            return self.format_output("ERROR")

    def count_chars_words(self, data: str) -> tuple[int, int]:
        """
        Count characters and words in a string.

        Args:
            data (str): The input text.

        Returns:
            tuple[int, int]: Number of characters and words.
        """
        char_count: int = 0
        word_count: int = 0
        in_word: bool = False

        for c in data:
            char_count += 1

            if c != " " and not in_word:
                word_count += 1
                in_word = True
            elif c == " ":
                in_word = False

        return char_count, word_count


class LogProcessor(DataProcessor):
    """
    Processor specialized in handling structured log messages.

    Validates log level prefixes and extracts level and message
    for formatted alert reporting.
    """
    def validate(self, data: Any) -> bool:
        """
        Validate that the input is a properly formatted log string.

        Accepted prefixes: ERROR:, WARN:, INFO:

        Args:
            data (Any): The log entry to validate.

        Returns:
            bool: True if the log format is valid.
        """
        if type(data) is not str:
            return False
        if data == "":
            return False

        if data[:6] == "ERROR:":
            return True
        if data[:5] == "WARN:":
            return True
        if data[:5] == "INFO:":
            return True

        return False

    def process(self, data: Any) -> str:
        """
        Process a log entry and extract level and message.

        Args:
            data (Any): The log string to process.

        Returns:
            str: Formatted alert message or error output.
        """
        try:
            print(f"Processing data: {data}")
            if not self.validate(data):
                raise ValueError("Invalid Data")

            print("Validation: Log data verified")

            i: int = 0
            for c in data:
                if c == ":":
                    break
                i += 1

            level: str = data[:i]
            message: str = data[i + 1:]

            if message != "" and message[0] == " ":
                message = message[1:]

            result: str = f"[{level}] {level} level detected: {message}"
            return self.format_output(result)

        except ValueError as e:
            print(e)
            return self.format_output("ERROR")


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("")

    print("Initializing Numeric Processor...")
    num_proc: NumericProcessor = NumericProcessor()
    data_1: list[int] = [1, 2, 3, 4, 5]
    print(num_proc.process(data_1))

    print()
    print("Initializing Text Processor...")
    text_proc: TextProcessor = TextProcessor()
    data_2: str = "Hello Nexus World"
    print(text_proc.process(data_2))

    print()
    print("Initializing Log Processor...")
    log_proc: LogProcessor = LogProcessor()
    data_3: str = "ERROR: Connection timeout"
    print(log_proc.process(data_3))

    print()
    print("=== Polymorphic Processing Demo ===")
    print()

    print("Processing multiple data types through same interface...")

    processors: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    data_samples: list[list[int] | str] = [
        [1, 2, 3],
        "Hello world!",
        "INFO: System ready",
    ]
    i: int = 0
    while i < 3:
        processor: DataProcessor = processors[i]
        data: Any = data_samples[i]
        result = processor.process(data)
        print(f"Result {i + 1}: {result}")
        i += 1

    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()

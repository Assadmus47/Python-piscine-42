from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """
    Abstract base class defining the interface for all data streams.

    Each stream must implement batch processing logic while
    optionally using the shared filtering and statistics behavior.
    """
    def __init__(self, stream_id: str):
        """
        Initialize the DataStream with a stream identifier.

        Args:
            stream_id (str): Unique identifier for the stream.
        """
        self.stream_id: str = stream_id
        self.total_processed: int = 0
        self.batches_processed: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of data specific to the stream type.

        Args:
            data_batch (List[Any]): The batch of data to process.

        Returns:
            str: The formatted processing result.
        """
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """
        Filter data based on an optional criteria string.

        Args:
            data_batch (List[Any]): The batch of data to filter.
            criteria (Optional[str]): The string criteria to filter by.

        Returns:
            List[Any]: Filtered list of data elements.
        """
        if criteria is None:
            return data_batch
        return [element for element in data_batch if criteria in element]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Return stream statistics.

        Returns:
            Dict[str, Union[str, int, float]]: Dictionary containing
            stream_id, total_processed, and batches_processed.
        """
        return {
            "stream_id": self.stream_id,
            "total_processed": self.total_processed,
            "batches_processed": self.batches_processed
            }


class SensorStream(DataStream):
    """
    Stream specialized in handling environmental sensor data.

    Validates sensor readings and computes average temperature
    from batch data containing temp, humidity, and pressure values.
    """
    def __init__(self, stream_id: str):
        """
        Initialize the SensorStream with a stream identifier.

        Args:
            stream_id (str): Unique identifier for the sensor stream.
        """
        super().__init__(stream_id)
        self.stream_type: str = "Environmental Data"
        self.temp: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of sensor readings and compute average temperature.

        Args:
            data_batch (List[Any]): List of sensor readings (e.g. 'temp:22.5').

        Returns:
            str: Formatted sensor analysis result.
        """
        temps: List[float] = []
        for elem in data_batch:
            if "temp" in elem:
                temps.append(float(elem[5:]))
        if temps:
            self.temp = sum(temps) / len(temps)

        self.total_processed += len(data_batch)
        self.batches_processed += 1

        return (
            f"Sensor analysis: {self.total_processed} readings processed, "
            f"avg temp: {self.temp:.1f}°C"
        )


class TransactionStream(DataStream):
    """
    Stream specialized in handling financial transaction data.

    Processes buy and sell operations and computes the net flow
    from batch data containing transaction values.
    """
    def __init__(self, stream_id: str):
        """
        Initialize the TransactionStream with a stream identifier.

        Args:
            stream_id (str): Unique identifier for the transaction stream.
        """
        super().__init__(stream_id)
        self.stream_type: str = "Financial Data"
        self.net_flow: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of transactions and compute net flow.

        Args:
            data_batch (List[Any]): List of transactions
            (e.g. 'buy:100', 'sell:150').

        Returns:
            str: Formatted transaction analysis result.
        """
        buys: int = 0
        for elem in data_batch:
            if "buy" in elem:
                buys += int(elem[4:])
        sells: int = 0
        for elem in data_batch:
            if "sell" in elem:
                sells += int(elem[5:])
        net: int = buys - sells
        sign: str = "+" if net >= 0 else ""

        self.total_processed += len(data_batch)
        self.batches_processed += 1
        self.net_flow += net
        return (
            f"Transaction analysis: {self.total_processed} "
            f"operations, net flow: {sign}{net} units"
        )


class EventStream(DataStream):
    """
    Stream specialized in handling system event data.

    Processes system events and counts errors from batch data
    containing event types like login, logout, and error.
    """
    def __init__(self, stream_id: str):
        """
        Initialize the EventStream with a stream identifier.

        Args:
            stream_id (str): Unique identifier for the event stream.
        """
        super().__init__(stream_id)
        self.stream_type: str = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of system events and count errors.

        Args:
            data_batch (List[Any]):
            List of system events (e.g. 'login', 'error').

        Returns:
            str: Formatted event analysis result.
        """
        errors: int = 0
        for elem in data_batch:
            if "error" in elem:
                errors += 1

        self.total_processed += len(data_batch)
        self.batches_processed += 1

        return (
            f"Event analysis: {self.total_processed} "
            f"events, {errors} error detected"
        )


class StreamProcessor():
    """
    Manages and processes multiple data streams polymorphically.

    Handles any DataStream subtype through a unified interface
    without knowing specific implementation details.
    """
    def __init__(self):
        """
        Initialize the StreamProcessor with an empty stream list.
        """
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream):
        """
        Add a data stream to the processor.

        Args:
            stream (DataStream): The stream to add.
        """
        self.streams.append(stream)

    def process_all(self, data_batch: List[Any]):
        """
        Process all streams with their respective data batches.

        Args:
            data_batch (List[Any]): List of batches, one per stream.
        """
        i: int = 0
        print("Batch 1 Results:")
        for stream in self.streams:
            stream.process_batch(data_batch[i])

            if isinstance(stream, SensorStream):
                print(
                    f"- Sensor data: {stream.total_processed} "
                    "readings processed"
                    )
            elif isinstance(stream, TransactionStream):
                print(
                    f"- Transaction data: {stream.total_processed} "
                    "operations processed"
                    )
            elif isinstance(stream, EventStream):
                print(
                    f"- Event data: {stream.total_processed} events processed"
                    )
            i += 1


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    print("Initializing Sensor Stream...")
    sensor: SensorStream = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    temp_data: List[str] = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {temp_data}")
    result: str = sensor.process_batch(temp_data)
    print(result)

    print()

    print("Initializing Transaction Stream...")
    transaction: TransactionStream = TransactionStream("TRANS_001")
    print(
        f"Stream ID: {transaction.stream_id}, Type: {transaction.stream_type}"
        )
    transaction_data: List[str] = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {transaction_data}")
    result = transaction.process_batch(transaction_data)
    print(result)

    print()

    print("Initializing Event Stream...")
    event: EventStream = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_data: List[str] = ["login", "error", "logout"]
    print(f"Processing event batch: {event_data}")
    result = event.process_batch(event_data)
    print(result)

    print()
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()
    stream_proc: StreamProcessor = StreamProcessor()
    stream_proc.add_stream(SensorStream("SENSOR_001"))
    stream_proc.add_stream(TransactionStream("TRANS_001"))
    stream_proc.add_stream(EventStream("EVENT_001"))
    batchs: List[List[str]] = [
        ["temp:19.0", "temp:21.0"],
        ["buy:100", "sell:50", "buy:200", "sell:100"],
        ["login", "error", "logout"]
    ]
    stream_proc.process_all(batchs)
    print()

    print("Stream filtering active: High-priority data only")
    filter_temp: int = len(sensor.filter_data(temp_data, "temp"))
    filter_buy: int = len(transaction.filter_data(transaction_data, "buy"))
    print(
        f"Filtered results: {filter_temp} "
        f"critical sensor alerts, {filter_buy} large transaction"
    )

    print("")
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()

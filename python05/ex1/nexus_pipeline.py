
from abc import ABC, abstractmethod
from typing import Any


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass
    @abstractmethod
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass
    @abstractmethod
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)


class StreamProcessor():
    pass
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    def __init__(self):
        pass

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        pass

    @classmethod
    def parse(cls, path: str) -> list:
        pass

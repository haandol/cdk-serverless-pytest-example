from abc import ABC, abstractmethod
from typing import Protocol, Callable


class FetchTable(Protocol):
    get_item: Callable


class FetchAdapter(ABC):
    @abstractmethod
    def fetch(self, path: str):
        """return hitCount for the given path"""
from abc import ABC, abstractmethod
from typing import Protocol, Callable


class UpdateTable(Protocol):
    update_item: Callable


class UpdateAdapter(ABC):
    @abstractmethod
    def update(self, path: str):
        """return hitCount for the given path"""
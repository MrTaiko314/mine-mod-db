from abc import ABC, abstractmethod


class Screen(ABC):
    """Interface base para todas as telas."""

    @abstractmethod
    def show(self) -> None:
        raise NotImplementedError

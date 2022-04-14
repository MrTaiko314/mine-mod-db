from typing import Generic, TypeVar


T = TypeVar('T')


class Database(Generic[T]):
    def __init__(self) -> None:
        self._index: int = 0
        self._entries: dict[int, T] = {}

    def _index_increment(self) -> None:
        self._index += 1

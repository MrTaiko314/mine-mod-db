from abc import abstractmethod
from typing import Any

from minemoddb.dao.dao import Dao, T
from minemoddb.dao.pysondb.pysondb_json_database_wrapper import \
    PysonDBJsonDatabaseWrapper


class PysonDBDao(Dao[T]):
    """Classe abstrata, base para implementações de DAOs para PysonDB."""

    def get(self, id: int) -> T:
        entry = self._object_table.get(id)
        return self._object_from_entry(entry)

    def get_all(self) -> list[T]:
        return list(map(self._object_from_entry, self._object_table.get_all()))

    def get_by_query(self, query: dict[str, Any]) -> list[T]:
        return list(map(
            self._object_from_entry, self._object_table.get_by_query(query)))

    def save(self, obj: T) -> int:
        entry = self._object_to_entry(obj)
        obj_id = self._object_table.save(entry)
        obj.id = obj_id
        return obj_id

    def update(self, obj: T) -> None:
        entry = self._object_to_entry(obj)
        self._object_table.update(obj.id, entry)

    def delete(self, obj: T) -> bool:
        return self._object_table.delete(obj.id)

    def delete_all(self) -> None:
        self._object_table.delete_all()

    @property
    @abstractmethod
    def _object_table(self) -> PysonDBJsonDatabaseWrapper:
        raise NotImplementedError

    @abstractmethod
    def _object_from_entry(self, entry: dict[str, Any]) -> T:
        raise NotImplementedError

    @abstractmethod
    def _object_to_entry(self, obj: T) -> dict[str, Any]:
        raise NotImplementedError

    @property
    def _entry_id_key_name(self) -> str:
        return self._object_table.id_key_name

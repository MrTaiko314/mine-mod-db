from typing import Any

from pysondb import db


class PysonDBJsonDatabaseWrapper:
    def __init__(self, pyson_db: db.JsonDatabase):
        self._pyson_db = pyson_db

    @property
    def id_key_name(self) -> str:
        return self._pyson_db.id_fieldname

    def get(self, id: int) -> dict[str, Any]:
        return self._pyson_db.getById(id)

    def get_all(self) -> list[dict[str, Any]]:
        return self._pyson_db.getAll()

    def get_by_query(self, query: dict[str, Any]) -> list[dict[str, Any]]:
        return self._pyson_db.getByQuery(query)

    def save(self, entry: dict[str, Any]) -> int:
        return self._pyson_db.add(entry)

    def update(self, id: int, new_entry: dict[str, Any]) -> None:
        self._pyson_db.updateById(id, new_entry)

    def delete(self, id: int) -> bool:
        return self._pyson_db.deleteById(id)

    def delete_all(self) -> None:
        self._pyson_db.deleteAll()

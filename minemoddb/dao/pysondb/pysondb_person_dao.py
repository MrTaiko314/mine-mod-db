from typing import Any

from minemoddb.dao.person_dao import PersonDao
from minemoddb.dao.pysondb.pysondb_dao import PysonDBDao
from minemoddb.dao.pysondb.pysondb_json_database_wrapper import \
    PysonDBJsonDatabaseWrapper
from minemoddb.models.person import Person


class PysonDBPersonDao(PysonDBDao[Person], PersonDao):
    """Implementação de PersonDao para PysonDB."""

    def __init__(self, person_db: PysonDBJsonDatabaseWrapper) -> None:
        self._person_db = person_db

    def get_by_name(self, name: str) -> list[Person]:
        return self.get_by_query({'name': name})

    @property
    def _object_table(self) -> PysonDBJsonDatabaseWrapper:
        return self._person_db

    def _object_from_entry(self, entry: dict[str, Any]) -> Person:
        return Person(
            name=entry['name'],
            id=entry[self._entry_id_key_name]
        )

    def _object_to_entry(self, person: Person) -> dict[str, Any]:
        return {'name': person.name}

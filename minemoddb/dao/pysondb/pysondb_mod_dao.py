from typing import Any

from minemoddb.dao.mod_dao import ModDao
from minemoddb.dao.pysondb.pysondb_dao import PysonDBDao
from minemoddb.dao.pysondb.pysondb_json_database_wrapper import \
    PysonDBJsonDatabaseWrapper
from minemoddb.dao.pysondb.pysondb_person_dao import PysonDBPersonDao
from minemoddb.models.mod import Mod


class PysonDBModDao(PysonDBDao[Mod], ModDao):
    """Implementação de ModDao para PysonDB."""

    def __init__(
            self, person_db: PysonDBJsonDatabaseWrapper,
            mod_db: PysonDBJsonDatabaseWrapper) -> None:
        self._person_db = person_db
        self._mod_db = mod_db

    def get_by_name(self, name: str) -> list[Mod]:
        return self.get_by_query({'name': name})

    def get_by_owner_name(self, owner_name: str) -> list[Mod]:
        return [mod for mod in self.get_all() if mod.owner.name == owner_name]

    @property
    def _person_dao(self) -> PysonDBPersonDao:
        return PysonDBPersonDao(self._person_db)

    @property
    def _object_table(self) -> PysonDBJsonDatabaseWrapper:
        return self._mod_db

    def _object_from_entry(self, entry: dict[str, Any]) -> Mod:
        return Mod(
            name=entry['name'],
            owner=self._person_dao.get(entry['owner']),
            id=entry[self._entry_id_key_name]
        )

    def _object_to_entry(self, mod: Mod) -> dict[str, Any]:
        return {
            'name': mod.name,
            'owner': mod.owner.id
        }

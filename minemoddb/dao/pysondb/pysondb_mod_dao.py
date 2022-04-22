from typing import Any

from minemoddb.dao.mod_dao import ModDao
from minemoddb.dao.pysondb.pysondb_json_database_wrapper import \
    PysonDBJsonDatabaseWrapper
from minemoddb.dao.pysondb.pysondb_person_dao import PysonDBPersonDao
from minemoddb.models.mod import Mod


class PysonDBModDao(ModDao):
    def __init__(
            self, person_db: PysonDBJsonDatabaseWrapper,
            mod_db: PysonDBJsonDatabaseWrapper) -> None:
        self._person_db = person_db
        self._mod_db = mod_db

    def get(self, id: int) -> Mod:
        entry = self._mod_db.get(id)
        return self._mod_from_entry(entry)

    def get_all(self) -> list[Mod]:
        entries = self._mod_db.get_all()
        return list(map(self._mod_from_entry, entries))

    def get_by_name(self, name: str) -> list[Mod]:
        query = {'name': name}
        entries = self._mod_db.get_by_query(query)
        return list(map(self._mod_from_entry, entries))

    def get_by_owner_name(self, owner_name: str) -> list[Mod]:
        return [mod for mod in self.get_all() if mod.owner.name == owner_name]

    def save(self, mod: Mod) -> int:
        entry = self._mod_to_entry(mod)
        mod_id = self._mod_db.save(entry)
        mod.id = mod_id
        return mod_id

    def update(self, mod: Mod) -> None:
        entry = self._mod_to_entry(mod)
        self._mod_db.update(mod.id, entry)

    def delete(self, mod: Mod) -> bool:
        return self._mod_db.delete(mod.id)

    def delete_all(self) -> None:
        self._mod_db.delete_all()

    @property
    def _person_dao(self) -> PysonDBPersonDao:
        return PysonDBPersonDao(self._person_db)

    @property
    def _entry_id_key_name(self) -> str:
        return self._mod_db.id_key_name

    def _mod_from_entry(self, entry: dict[str, Any]) -> Mod:
        return Mod(
            name=entry['name'],
            owner=self._person_dao.get(entry['owner']),
            id=entry[self._entry_id_key_name]
        )

    def _mod_to_entry(self, mod: Mod) -> dict[str, Any]:
        return {
            'name': mod.name,
            'owner': mod.owner.id
        }

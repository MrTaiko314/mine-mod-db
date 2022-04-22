from typing import Any

from minemoddb.dao.modpack_dao import ModpackDao
from minemoddb.dao.pysondb.pysondb_json_database_wrapper import \
    PysonDBJsonDatabaseWrapper
from minemoddb.dao.pysondb.pysondb_mod_dao import PysonDBModDao
from minemoddb.dao.pysondb.pysondb_person_dao import PysonDBPersonDao
from minemoddb.models.modpack import Modpack


class PysonDBModpackDao(ModpackDao):
    def __init__(
            self, person_db: PysonDBJsonDatabaseWrapper,
            mod_db: PysonDBJsonDatabaseWrapper,
            modpack_db: PysonDBJsonDatabaseWrapper) -> None:
        self._person_db = person_db
        self._mod_db = mod_db
        self._modpack_db = modpack_db

    def get(self, id: int) -> Modpack:
        entry = self._modpack_db.get(id)
        return self._modpack_from_entry(entry)

    def get_all(self) -> list[Modpack]:
        entries = self._modpack_db.get_all()
        return list(map(self._modpack_from_entry, entries))

    def get_by_name(self, name: str) -> list[Modpack]:
        query = {'name': name}
        entries = self._modpack_db.get_by_query(query)
        return list(map(self._modpack_from_entry, entries))

    def get_by_owner_name(self, owner_name: str) -> list[Modpack]:
        return [
            modpack
            for modpack in self.get_all()
            if modpack.owner.name == owner_name
        ]

    def get_by_contained_mod_name(self, mod_name: str) -> list[Modpack]:
        return [
            modpack
            for modpack in self.get_all()
            if any(mod.name == mod_name for mod in modpack.mods)
        ]

    def save(self, modpack: Modpack) -> int:
        entry = self._modpack_to_entry(modpack)
        modpack_id = self._modpack_db.save(entry)
        modpack.id = modpack_id
        return modpack_id

    def update(self, modpack: Modpack) -> None:
        entry = self._modpack_to_entry(modpack)
        self._modpack_db.update(modpack.id, entry)

    def delete(self, modpack: Modpack) -> bool:
        return self._modpack_db.delete(modpack.id)

    def delete_all(self) -> None:
        self._modpack_db.delete_all()

    @property
    def _person_dao(self) -> PysonDBPersonDao:
        return PysonDBPersonDao(self._person_db)

    @property
    def _mod_dao(self) -> PysonDBModDao:
        return PysonDBModDao(self._person_db, self._mod_db)

    @property
    def _entry_id_key_name(self) -> str:
        return self._modpack_db.id_key_name

    def _modpack_from_entry(self, entry: dict[str, Any]) -> Modpack:
        return Modpack(
            name=entry['name'],
            owner=self._person_dao.get(entry['owner']),
            mods=[self._mod_dao.get(mod_id) for mod_id in entry['mods']],
            id=entry[self._entry_id_key_name]
        )

    def _modpack_to_entry(self, modpack: Modpack) -> dict[str, Any]:
        return {
            'name': modpack.name,
            'owner': modpack.owner.id,
            'mods': [mod.id for mod in modpack.mods]
        }

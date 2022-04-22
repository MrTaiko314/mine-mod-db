from typing import Any

from minemoddb.dao.person_dao import PersonDao
from minemoddb.dao.pysondb.pysondb_json_database_wrapper import \
    PysonDBJsonDatabaseWrapper
from minemoddb.models.person import Person


class PysonDBPersonDao(PersonDao):
    def __init__(self, person_db: PysonDBJsonDatabaseWrapper) -> None:
        self._person_db = person_db

    def get(self, id: int) -> Person:
        entry = self._person_db.get(id)
        return self._person_from_entry(entry)

    def get_all(self) -> list[Person]:
        entries = self._person_db.get_all()
        return list(map(self._person_from_entry, entries))

    def get_by_name(self, name: str) -> list[Person]:
        query = {'name': name}
        entries = self._person_db.get_by_query(query)
        return list(map(self._person_from_entry, entries))

    def save(self, person: Person) -> int:
        entry = self._person_to_entry(person)
        person_id = self._person_db.save(entry)
        person.id = person_id
        return person_id

    def update(self, person: Person) -> None:
        entry = self._person_to_entry(person)
        self._person_db.update(person.id, entry)

    def delete(self, person: Person) -> bool:
        return self._person_db.delete(person.id)

    def delete_all(self) -> None:
        self._person_db.delete_all()

    @property
    def _entry_id_key_name(self) -> str:
        return self._person_db.id_key_name

    def _person_from_entry(self, entry: dict[str, Any]) -> Person:
        return Person(
            name=entry['name'],
            id=entry[self._entry_id_key_name]
        )

    def _person_to_entry(self, person: Person) -> dict[str, Any]:
        return {'name': person.name}

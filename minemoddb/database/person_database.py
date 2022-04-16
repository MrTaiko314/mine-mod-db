import copy
from minemoddb.database.database import Database
from minemoddb.models.person import Person


class PersonDatabase(Database[Person]):
    def add_person(self, person: Person) -> int:
        self._entries[self._index] = copy.copy(person)
        self._index_increment()
        return self._index-1

    def get_person_id(self, person: Person) -> int:
        for key, value in self._entries.items():
            if value == person:
                return key
        return -1

    def get_person(self, person_id: int) -> Person:
        return copy.copy(self._entries[person_id])

    def remove_person(self, person: Person) -> None:
        for key, value in self._entries.items():
            if value == person:
                del self._entries[key]
                break

    def modify_person(self, person_id: int, person: Person) -> None:
        """Modifica registro do banco de dados a partir de dicionário de
        modificações.

        :param person_id: Id do registro da pessoa a ser modificada.
        :param person: Pessoa modificada.
        """
        self._entries[person_id] = copy.copy(person)

    def retrieve_entries(self) -> dict[int, Person]:
        return self._entries

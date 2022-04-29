from minemoddb.models.database_object import DatabaseObject
from minemoddb.models.person import Person


class Mod(DatabaseObject):
    def __init__(self, name: str, owner: Person, id: int = -1) -> None:
        super().__init__(id)
        self.name = name
        self.owner = owner

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.owner == other.owner

    def __str__(self) -> str:
        return f'Mod(name={self.name}, owner={self.owner})'

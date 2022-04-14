from minemoddb.models.person import Person


class Mod:
    def __init__(self, name: str, owner: Person) -> None:
        self.name = name
        self.owner = owner

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.owner == other.owner

    def __str__(self) -> str:
        return f'Mod(name={self.name}, owner={self.owner})'

from minemoddb.models.database_object import DatabaseObject


class Person(DatabaseObject):
    """Representa uma pessoa.

    name: Nomes são únicos no sistema.
    """

    def __init__(self, name: str, id: int = -1) -> None:
        super().__init__(id)
        self.name = name

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __str__(self) -> str:
        return f'Person(name={self.name})'

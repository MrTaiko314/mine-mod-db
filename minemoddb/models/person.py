from __future__ import annotations


class Person:
    """Representa uma pessoa.

    name: Nomes são únicos no sistema.
    """

    def __init__(self, name: str, id: int = -1) -> None:
        self.name = name
        self.id = id

    def __eq__(self, other: Person) -> bool:
        return self.name == other.name

    def __str__(self) -> str:
        return f'Person(name={self.name})'

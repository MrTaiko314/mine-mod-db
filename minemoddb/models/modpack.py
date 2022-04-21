from __future__ import annotations

from minemoddb.models.mod import Mod
from minemoddb.models.person import Person


class Modpack:
    def __init__(
            self, name: str, owner: Person, mods: list[Mod],
            id: int = -1) -> None:
        self.name = name
        self.owner = owner
        self.mods = mods
        self.id = id

    def __eq__(self, other: Modpack) -> bool:
        return (
            len(self.mods) == len(other.mods)
            and self.name == other.name
            and self.owner == other.owner
            and all(mod in other.mods for mod in self.mods))

    def __str__(self) -> str:
        mod_text = '\n- '.join(map(str, self.mods))
        return (
            f'Modpack(name={self.name}, owner={self.owner},'
            f' \nmods=[\n- {mod_text}])')

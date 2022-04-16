import copy

from minemoddb.database.database import Database
from minemoddb.models.mod import Mod
from minemoddb.models.modpack import Modpack


class ModpackDatabase(Database[Modpack]):
    def add_modpack(self, modpack: Modpack) -> int:
        self._entries[self._index] = copy.copy(modpack)
        self._index_increment()
        return self._index - 1

    def remove_modpack(self, modpack: Modpack) -> None:
        for key, value in self._entries.items():
            if value == modpack:
                del self._entries[key]
                break

    def get_modpack(self, modpack_id: int) -> Modpack:
        return copy.copy(self._entries[modpack_id])

    def get_modpack_id(self, modpack: Modpack) -> int:
        for key, value in self._entries.items():
            if value == modpack:
                return key
        return -1

    def modify_modpack(self, modpack_id: int, modpack: Mod) -> None:
        self._entries[modpack_id] = copy.copy(modpack)

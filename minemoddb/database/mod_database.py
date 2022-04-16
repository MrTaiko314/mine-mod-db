import copy

from minemoddb.models.mod import Mod
from minemoddb.database.database import Database


class ModDatabase(Database[Mod]):
    def add_mod(self, mod: Mod) -> int:
        self._entries[self._index] = copy.copy(mod)
        self._index_increment()
        return self._index - 1

    def get_mod_id(self, mod: Mod) -> int:
        for key, value in self._entries.items():
            if value == mod:
                return key
        return -1

    def get_mod(self, mod_id: int) -> Mod:
        return copy.copy(self._entries[mod_id])

    def modify_mod(self, mod_id: int, mod: Mod) -> None:
        self._entries[mod_id] = copy.copy(mod)

    def remove_mod(self, mod: Mod) -> None:
        for key, value in self._entries.items():
            if value == mod:
                del self._entries[key]
                break

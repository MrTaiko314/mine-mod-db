from abc import abstractmethod

from minemoddb.dao.dao import Dao
from minemoddb.models.mod import Mod


class ModDao(Dao[Mod]):
    """Interface base para todos os DAOs de Mod."""

    @abstractmethod
    def get_by_name(self, name: str) -> list[Mod]:
        """Retorna uma lista com todos os mods com o nome passado."""
        raise NotImplementedError

    @abstractmethod
    def get_by_owner_name(self, owner_name: str) -> list[Mod]:
        """Retorna uma lista com todos os mods cujo dono tem o nome passado."""
        raise NotImplementedError

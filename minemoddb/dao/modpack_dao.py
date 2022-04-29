from abc import abstractmethod

from minemoddb.dao.dao import Dao
from minemoddb.models.modpack import Modpack


    """Classe abstrata base para todos os DAOs de Modpack."""
class ModpackDao(Dao[Modpack]):

    @abstractmethod
    def get_by_name(self, name: str) -> list[Modpack]:
        """Retorna uma lista com todos os modpacks com o nome passado."""
        raise NotImplementedError

    @abstractmethod
    def get_by_owner_name(self, owner_name: str) -> list[Modpack]:
        """Retorna uma lista com todos os modpacks cujo dono tem o nome
        passado.
        """

        raise NotImplementedError

    @abstractmethod
    def get_by_contained_mod_name(self, mod_name: str) -> list[Modpack]:
        """Retorna uma lista com todos os modpacks que contenham pelo
        menos um mod com o nome passado.
        """

        raise NotImplementedError

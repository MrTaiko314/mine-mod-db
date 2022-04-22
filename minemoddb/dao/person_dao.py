from abc import abstractmethod

from minemoddb.dao.dao import Dao
from minemoddb.models.person import Person


class PersonDao(Dao[Person]):
    """Classe abstrata base para todos os DAOs de Person."""

    @abstractmethod
    def get_by_name(self, name: str) -> list[Person]:
        """Retorna uma lista com todas as pessoas com o nome passado."""
        raise NotImplementedError

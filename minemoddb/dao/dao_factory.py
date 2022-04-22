from abc import ABC, abstractmethod

from minemoddb.dao.mod_dao import ModDao
from minemoddb.dao.modpack_dao import ModpackDao
from minemoddb.dao.person_dao import PersonDao


class DaoFactory(ABC):

    @abstractmethod
    def create_person_dao(self) -> PersonDao:
        raise NotImplementedError

    @abstractmethod
    def create_mod_dao(self) -> ModDao:
        raise NotImplementedError

    @abstractmethod
    def create_modpack_dao(self) -> ModpackDao:
        raise NotImplementedError

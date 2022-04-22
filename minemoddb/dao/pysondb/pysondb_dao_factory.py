from minemoddb.dao.dao_factory import DaoFactory
from minemoddb.dao.mod_dao import ModDao
from minemoddb.dao.modpack_dao import ModpackDao
from minemoddb.dao.person_dao import PersonDao
from minemoddb.dao.pysondb.pysondb_json_database_wrapper import \
    PysonDBJsonDatabaseWrapper
from minemoddb.dao.pysondb.pysondb_mod_dao import PysonDBModDao
from minemoddb.dao.pysondb.pysondb_modpack_dao import PysonDBModpackDao
from minemoddb.dao.pysondb.pysondb_person_dao import PysonDBPersonDao


class PysonDBDaoFactory(DaoFactory):
    def __init__(
            self, person_db: PysonDBJsonDatabaseWrapper,
            mod_db: PysonDBJsonDatabaseWrapper,
            modpack_db: PysonDBJsonDatabaseWrapper) -> None:
        self._person_db = person_db
        self._mod_db = mod_db
        self._modpack_db = modpack_db

    def create_person_dao(self) -> PersonDao:
        return PysonDBPersonDao(person_db=self._person_db)

    def create_mod_dao(self) -> ModDao:
        return PysonDBModDao(
            person_db=self._person_db,
            mod_db=self._mod_db
        )

    def create_modpack_dao(self) -> ModpackDao:
        return PysonDBModpackDao(
            person_db=self._person_db,
            mod_db=self._mod_db,
            modpack_db=self._modpack_db
        )

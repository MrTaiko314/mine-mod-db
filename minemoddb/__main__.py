from pysondb import db

from minemoddb.dao.pysondb.pysondb_dao_factory import PysonDBDaoFactory
from minemoddb.dao.pysondb.pysondb_json_database_wrapper import \
    PysonDBJsonDatabaseWrapper
from minemoddb.program import Program
from minemoddb.cli.main_menu_screen import MainMenuScreen


def main() -> None:
    person_db = PysonDBJsonDatabaseWrapper(
        db.JsonDatabase('data/person_table.json'))
    mod_db = PysonDBJsonDatabaseWrapper(
        db.JsonDatabase('data/mod_table.json'))
    modpack_db = PysonDBJsonDatabaseWrapper(
        db.JsonDatabase('data/modpack_table.json'))
    dao_factory = PysonDBDaoFactory(
        person_db=person_db, mod_db=mod_db, modpack_db=modpack_db)
    program = Program(dao_factory=dao_factory)
    program.set_screen(MainMenuScreen(program))
    program.run()


if __name__ == '__main__':
    main()

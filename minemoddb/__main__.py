from minemoddb.database.person_database import PersonDatabase
from minemoddb.database.mod_database import ModDatabase
from minemoddb.database.modpack_database import ModpackDatabase
from minemoddb.program import Program
from minemoddb.cli.main_menu_screen import MainMenuScreen


def main() -> None:
    person_database = PersonDatabase()
    mod_database = ModDatabase()
    modpack_database = ModpackDatabase()
    program = Program(person_database, mod_database, modpack_database)
    program.set_screen(MainMenuScreen(program))
    program.run()


if __name__ == '__main__':
    main()

from minemoddb.database.person_database import PersonDatabase
from minemoddb.database.mod_database import ModDatabase
from minemoddb.database.modpack_database import ModpackDatabase
import minemoddb.cli.screen as screen
from minemoddb.utils import clear_screen


class Program:
    def __init__(
            self, person_database: PersonDatabase, mod_database: ModDatabase,
            modpack_database: ModpackDatabase) -> None:
        self._previous_screen: screen.Screen | None = None
        self._current_screen: screen.Screen | None = None
        self._person_database = person_database
        self._mod_database = mod_database
        self._modpack_database = modpack_database

    def set_screen(self, screen: screen.Screen) -> None:
        self._previous_screen = self._current_screen
        self._current_screen = screen

    def run(self) -> None:
        if self._current_screen is None:
            return

        while True:
            clear_screen()
            self._current_screen.show()
            if self._previous_screen is None:
                break
            else:
                self._previous_screen = None

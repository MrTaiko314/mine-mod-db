from minemoddb.database.person_database import PersonDatabase
from minemoddb.database.mod_database import ModDatabase
from minemoddb.database.modpack_database import ModpackDatabase
import minemoddb.cli.screen as screen
from minemoddb.models.person import Person
from minemoddb.models.mod import Mod
from minemoddb.models.modpack import Modpack
from minemoddb.utils import clear_screen, get_number, get_numbers


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

    def get_person(self, prompt: str) -> Person:
        entries = self._person_database.entries
        if len(entries) == 0:
            raise RuntimeError('Person database is empty')
        print(f"Pessoas ({len(entries)}):")
        sorted_person_list = sorted(entries.values(), key=lambda x: x.name)
        for i, person in enumerate(sorted_person_list, 1):
            print(f"{i:3}. {person.name}")
        selected_number = get_number(
            prompt=prompt, min_value=1, max_value=len(entries))
        return sorted_person_list[selected_number - 1]

    def get_mod(self, prompt: str) -> Mod:
        entries = self._mod_database.entries
        if len(entries) == 0:
            raise RuntimeError('Mod database is empty')
        print(f"Mods ({len(entries)}):")
        sorted_mod_list = sorted(entries.values(), key=lambda x: x.name)
        for i, mod in enumerate(sorted_mod_list, 1):
            print(f"{i:3}. {mod.name} de {mod.owner.name}")
        selected_number = get_number(
            prompt=prompt, min_value=1, max_value=len(entries))
        return sorted_mod_list[selected_number - 1]

    def get_mods(self, prompt: str) -> list[Mod]:
        entries = self._mod_database.entries
        if len(entries) == 0:
            raise RuntimeError('Mod database is empty')
        print(f"Mods ({len(entries)}):")
        sorted_mod_list = sorted(entries.values(), key=lambda x: x.name)
        for i, mod in enumerate(sorted_mod_list, 1):
            print(f"{i:3}. {mod.name} de {mod.owner.name}")
        selected_numbers = get_numbers(
            prompt=prompt, min_value=1, max_value=len(entries), separator=',')
        mods = [sorted_mod_list[number-1] for number in selected_numbers]
        return mods

    def get_modpack(self, prompt: str) -> Modpack:
        entries = self._modpack_database.entries
        if len(entries) == 0:
            raise RuntimeError('Modpack database is empty')
        print(f"Modpacks ({len(entries)}):")
        sorted_modpack_list = sorted(entries.values(), key=lambda x: x.name)
        for i, modpack in enumerate(sorted_modpack_list, 1):
            print(f"{i:3}. {modpack.name} de {modpack.owner.name}")
        selected_number = get_number(
            prompt=prompt, min_value=1, max_value=len(entries))
        return sorted_modpack_list[selected_number - 1]

from minemoddb.dao.dao_factory import DaoFactory
from minemoddb.dao.mod_dao import ModDao
from minemoddb.dao.modpack_dao import ModpackDao
from minemoddb.dao.person_dao import PersonDao
import minemoddb.cli.screen as screen
from minemoddb.models.person import Person
from minemoddb.models.mod import Mod
from minemoddb.models.modpack import Modpack
from minemoddb.utils import clear_screen, get_number, get_numbers


class Program:
    def __init__(self, dao_factory: DaoFactory) -> None:
        self._previous_screen: screen.Screen | None = None
        self._current_screen: screen.Screen | None = None
        self._dao_factory = dao_factory

    @property
    def person_dao(self) -> PersonDao:
        return self._dao_factory.create_person_dao()

    @property
    def mod_dao(self) -> ModDao:
        return self._dao_factory.create_mod_dao()

    @property
    def modpack_dao(self) -> ModpackDao:
        return self._dao_factory.create_modpack_dao()

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

    def get_person(self, prompt: str, person_list: list[Person]) -> Person:
        if len(person_list) == 0:
            raise RuntimeError('Person list is empty')
        print(f"Pessoas ({len(person_list)}):")
        sorted_person_list = sorted(person_list, key=lambda x: x.name)
        for i, person in enumerate(sorted_person_list, 1):
            print(f"{i:3}. {person.name}")
        selected_number = get_number(
            prompt=prompt, min_value=1, max_value=len(person_list))
        return sorted_person_list[selected_number - 1]

    def get_mod(self, prompt: str, mod_list: list[Mod]) -> Mod:
        if len(mod_list) == 0:
            raise RuntimeError('Mod list is empty')
        print(f"Mods ({len(mod_list)}):")
        sorted_mod_list = sorted(mod_list, key=lambda x: x.name)
        for i, mod in enumerate(sorted_mod_list, 1):
            print(f"{i:3}. {mod.name} de {mod.owner.name}")
        selected_number = get_number(
            prompt=prompt, min_value=1, max_value=len(mod_list))
        return sorted_mod_list[selected_number - 1]

    def get_mods(self, prompt: str, mod_list: list[Mod]) -> list[Mod]:
        if len(mod_list) == 0:
            raise RuntimeError('Mod list is empty')
        print(f"Mods ({len(mod_list)}):")
        sorted_mod_list = sorted(mod_list, key=lambda x: x.name)
        for i, mod in enumerate(sorted_mod_list, 1):
            print(f"{i:3}. {mod.name} de {mod.owner.name}")
        selected_numbers = get_numbers(
            prompt=prompt, min_value=1, max_value=len(mod_list), separator=',')
        mods = [sorted_mod_list[number-1] for number in selected_numbers]
        return mods

    def get_modpack(self, prompt: str, modpack_list: list[Modpack]) -> Modpack:
        if len(modpack_list) == 0:
            raise RuntimeError('Modpack list is empty')
        print(f"Modpacks ({len(modpack_list)}):")
        sorted_modpack_list = sorted(modpack_list, key=lambda x: x.name)
        for i, modpack in enumerate(sorted_modpack_list, 1):
            print(f"{i:3}. {modpack.name} de {modpack.owner.name}")
        selected_number = get_number(
            prompt=prompt, min_value=1, max_value=len(modpack_list))
        return sorted_modpack_list[selected_number - 1]

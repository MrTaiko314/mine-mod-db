from minemoddb.models.modpack import Modpack
from minemoddb.program import Program
from minemoddb.cli.screen import Screen
import minemoddb.cli.modpack_table_menu_screen as modpack_table_menu_screen
from minemoddb.utils import get_option


class ModpackInfoScreen(Screen):
    def __init__(self, program: Program, modpack: Modpack) -> None:
        self._program = program
        self._modpack = modpack

    def show(self) -> None:
        print('Modpack'.upper())
        print('')

        print(f"Nome: {self._modpack.name}")
        print(f"Dono: {self._modpack.owner.name}")
        print('Mods:')
        sorted_mods = sorted(self._modpack.mods, key=lambda mod: mod.name)
        for mod in sorted_mods:
            print(f"- {mod.name} de {mod.owner.name}")
        print('')

        options = ['Voltar']
        option = get_option(options)
        if option == 'Voltar':
            self._program.set_screen(
                modpack_table_menu_screen
                .ModpackTableMenuScreen(self._program))

from minemoddb.models.mod import Mod
from minemoddb.program import Program
from minemoddb.cli.screen import Screen
# from minemoddb.ui.edit_mod_screen import EditPersonScreen
import minemoddb.cli.mod_table_menu_screen as mod_table_menu_screen
from minemoddb.utils import get_option


class ModInfoScreen(Screen):
    def __init__(self, program: Program, mod: Mod) -> None:
        self._program = program
        self._mod = mod

    def show(self) -> None:
        print('Mod'.upper())

        print(f"Nome: {self._mod.name}")
        print(f"Dono: {self._mod.owner.name}")
        options = ['Voltar']
        option = get_option(options)
        if option == 'Voltar':
            self._program.set_screen(
                mod_table_menu_screen.ModTableMenuScreen(self._program))

from minemoddb.program import Program
import minemoddb.cli.main_menu_screen as main_menu_screen
import minemoddb.cli.person_table_menu_screen as person_table_menu_screen
import minemoddb.cli.mod_table_menu_screen as mod_table_menu_screen
import minemoddb.cli.modpack_table_menu_screen as modpack_table_menu_screen
from minemoddb.cli.screen import Screen
from minemoddb.utils import get_option


class TablesMenuScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Tabelas'.upper())

        options = ['Pessoas', 'Mods', 'Modpacks', 'Voltar']
        option = get_option(options)
        if option == 'Pessoas':
            self._program.set_screen(
                person_table_menu_screen.PersonTableMenuScreen(self._program))
        elif option == 'Mods':
            self._program.set_screen(
                mod_table_menu_screen.ModTableMenuScreen(self._program))
        elif option == 'Modpacks':
            self._program.set_screen(
                modpack_table_menu_screen
                .ModpackTableMenuScreen(self._program))
        elif option == 'Voltar':
            self._program.set_screen(
                main_menu_screen.MainMenuScreen(self._program))

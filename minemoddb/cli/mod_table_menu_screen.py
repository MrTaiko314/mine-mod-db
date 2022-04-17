from minemoddb.program import Program
from minemoddb.cli.screen import Screen
from minemoddb.cli.create_mod_screen import CreateModScreen
from minemoddb.cli.select_mod_screen import SelectModScreen
import minemoddb.cli.tables_menu_screen as tables_menu_screen
from minemoddb.utils import get_option


class ModTableMenuScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Mods'.upper())

        options = [
            'Ver/atualizar mod', 'Cadastrar mod', 'Voltar'
        ]
        option = get_option(options)
        if option == 'Ver/atualizar mod':
            self._program.set_screen(SelectModScreen(self._program))
        elif option == 'Cadastrar mod':
            self._program.set_screen(CreateModScreen(self._program))
        elif option == 'Voltar':
            self._program.set_screen(
                tables_menu_screen.TablesMenuScreen(self._program))

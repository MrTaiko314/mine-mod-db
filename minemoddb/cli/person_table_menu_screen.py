from minemoddb.program import Program
from minemoddb.cli.screen import Screen
import minemoddb.cli.tables_menu_screen as tables_menu_screen
from minemoddb.cli.create_person_screen import CreatePersonScreen
from minemoddb.cli.select_person_screen import SelectPersonScreen
from minemoddb.utils import get_option


class PersonTableMenuScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Pessoas'.upper())

        options = [
            'Ver/atualizar pessoa', 'Cadastrar pessoa', 'Voltar'
        ]
        option = get_option(options)
        if option == 'Ver/atualizar pessoa':
            self._program.set_screen(SelectPersonScreen(self._program))
        elif option == 'Cadastrar pessoa':
            self._program.set_screen(CreatePersonScreen(self._program))
        elif option == 'Voltar':
            self._program.set_screen(
                tables_menu_screen.TablesMenuScreen(self._program))

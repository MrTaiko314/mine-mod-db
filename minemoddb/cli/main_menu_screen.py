from minemoddb.program import Program
from minemoddb.cli.screen import Screen
from minemoddb.cli.tables_menu_screen import TablesMenuScreen
from minemoddb.utils import get_option


class MainMenuScreen(Screen):
    def __init__(self, program: Program) -> None:
        super().__init__()
        self._program = program

    def show(self) -> None:
        print('Menu principal\n'.upper())

        options = ['Tabelas', 'Sair']
        option = get_option(options)
        if option == 'Tabelas':
            self._program.set_screen(TablesMenuScreen(self._program))
        elif option == 'Sair':
            print('Tchau.')

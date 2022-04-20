from minemoddb.program import Program
from minemoddb.cli.screen import Screen
import minemoddb.cli.tables_menu_screen as tables_menu_screen
from minemoddb.cli.create_modpack_screen import CreateModpackScreen
from minemoddb.cli.select_modpack_screen import SelectModpackScreen
from minemoddb.utils import get_option


class ModpackTableMenuScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Modpacks\n'.upper())

        options = [
            'Ver/atualizar modpacks', 'Cadastrar modpack', 'Voltar'
        ]
        option = get_option(options)
        if option == 'Ver/atualizar modpacks':
            self._program.set_screen(SelectModpackScreen(self._program))
        elif option == 'Cadastrar modpack':
            self._program.set_screen(CreateModpackScreen(self._program))
        elif option == 'Voltar':
            self._program.set_screen(
                tables_menu_screen.TablesMenuScreen(self._program))

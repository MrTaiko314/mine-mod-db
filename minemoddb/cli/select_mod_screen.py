from minemoddb.program import Program
import minemoddb.cli.mod_table_menu_screen as mod_table_menu_screen
from minemoddb.cli.screen import Screen
from minemoddb.cli.mod_info_screen import ModInfoScreen


class SelectModScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Seleção de mod\n'.upper())

        entries = self._program._mod_database.entries
        if len(entries) == 0:
            print('Nenhum mod encontrado.')

            input('\nPressione enter para voltar...')
            self._program.set_screen(
                mod_table_menu_screen.ModTableMenuScreen(self._program))
            return

        mod = self._program.get_mod('Mod> ')
        self._program.set_screen(ModInfoScreen(self._program, mod))

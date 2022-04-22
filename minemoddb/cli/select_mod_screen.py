from minemoddb.program import Program
import minemoddb.cli.mod_table_menu_screen as mod_table_menu_screen
from minemoddb.cli.screen import Screen
from minemoddb.cli.mod_info_screen import ModInfoScreen


class SelectModScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Seleção de mod\n'.upper())

        mod_list = self._program._mod_database.get_all()
        if len(mod_list) == 0:
            print('Nenhum mod encontrado.')

            input('\nPressione enter para voltar...')
            self._program.set_screen(
                mod_table_menu_screen.ModTableMenuScreen(self._program))
            return

        mod = self._program.get_mod(prompt='Mod> ', mod_list=mod_list)
        self._program.set_screen(ModInfoScreen(self._program, mod))

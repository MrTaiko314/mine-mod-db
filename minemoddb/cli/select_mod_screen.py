from minemoddb.program import Program
import minemoddb.cli.mod_table_menu_screen as mod_table_menu_screen
from minemoddb.cli.screen import Screen
from minemoddb.cli.mod_info_screen import ModInfoScreen
from minemoddb.utils import get_number


class SelectModScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Seleção de mod'.upper())

        entries = self._program._mod_database.entries
        if len(entries) == 0:
            print('Nenhum mod encontrado.')
            input('Pressione enter para voltar...')
            self._program.set_screen(
                mod_table_menu_screen.ModTableMenuScreen(self._program))
            return

        print(f"Mods {len(entries)}:")
        sorted_mod_list = sorted(entries.values(), key=lambda x: x.name)
        for i, mod in enumerate(sorted_mod_list, 1):
            print(f"{i:3}. {mod.name} de {mod.owner.name}")

        selected_number = get_number('Seleção> ', 1, len(entries))
        mod = sorted_mod_list[selected_number - 1]
        self._program.set_screen(ModInfoScreen(self._program, mod))

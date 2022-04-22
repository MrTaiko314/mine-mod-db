from minemoddb.program import Program
import minemoddb.cli.modpack_table_menu_screen as modpack_table_menu_screen
from minemoddb.cli.screen import Screen
from minemoddb.cli.modpack_info_screen import ModpackInfoScreen


class SelectModpackScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Seleção de modpack\n'.upper())

        modpack_list = self._program.modpack_dao.get_all()
        if len(modpack_list) == 0:
            print('Nenhum modpack encontrado.')

            input('\nPressione para voltar...')
            self._program.set_screen(
                modpack_table_menu_screen
                .ModpackTableMenuScreen(self._program))
            return

        modpack = self._program.get_modpack(
            prompt='Modpack> ', modpack_list=modpack_list)
        self._program.set_screen(ModpackInfoScreen(self._program, modpack))

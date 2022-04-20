from minemoddb.program import Program
from minemoddb.models.modpack import Modpack
from minemoddb.cli.screen import Screen
import minemoddb.cli.modpack_table_menu_screen as modpack_table_menu_screen


class CreateModpackScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Cadastro de modpack'.upper())

        if len(self._program._person_database.entries) == 0:
            print('Não existe nenhum usuário cadastrado!')
            self._return_to_previous_screen()
            return

        if len(self._program._mod_database.entries) == 0:
            print('Não existe nenhum mod cadastrado!')
            self._return_to_previous_screen()
            return

        modpack_name = input('Nome do modpack> ')
        modpack_owner = self._program.get_person('Dono do modpack> ')
        mods = self._program.get_mods('Mods> ')
        modpack = Modpack(modpack_name, modpack_owner, mods)
        self._program._modpack_database.add_modpack(modpack)
        print('Modpack cadastrado com sucesso.')
        self._return_to_previous_screen()

    def _return_to_previous_screen(self) -> None:
        input('Pressione enter para voltar...')
        self._program.set_screen(
            modpack_table_menu_screen.ModpackTableMenuScreen(self._program))

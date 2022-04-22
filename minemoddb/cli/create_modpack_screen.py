from minemoddb.program import Program
from minemoddb.models.modpack import Modpack
from minemoddb.cli.screen import Screen
import minemoddb.cli.modpack_table_menu_screen as modpack_table_menu_screen


class CreateModpackScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Cadastro de modpack\n'.upper())

        person_list = self._program.person_dao.get_all()
        if len(person_list) == 0:
            print('Não existe nenhum usuário cadastrado!')
            self._return_to_previous_screen()
            return

        mod_list = self._program.mod_dao.get_all()
        if len(mod_list) == 0:
            print('Não existe nenhum mod cadastrado!')
            self._return_to_previous_screen()
            return

        modpack_name = input('Nome do modpack> ')
        modpack_owner = self._program.get_person(
            prompt='Dono do modpack> ', person_list=person_list)
        mods = self._program.get_mods(prompt='Mods> ', mod_list=mod_list)
        modpack = Modpack(modpack_name, modpack_owner, mods)
        self._program.modpack_dao.save(modpack)

        print('\nModpack cadastrado com sucesso.')

        self._return_to_previous_screen()

    def _return_to_previous_screen(self) -> None:
        input('\nPressione enter para voltar...')
        self._program.set_screen(
            modpack_table_menu_screen.ModpackTableMenuScreen(self._program))

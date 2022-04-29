from minemoddb.program import Program
from minemoddb.models.mod import Mod
from minemoddb.cli.screen import Screen
import minemoddb.cli.mod.mod_table_menu_screen as mod_table_menu_screen


class CreateModScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Cadastro de mod\n'.upper())

        person_list = self._program.person_dao.get_all()
        if len(person_list) == 0:
            print('Não existe nenhum usuário cadastrado!')
            self._return_to_previous_screen()
            return

        mod_name = input('Nome do mod> ')
        mod_owner = self._program.get_person(
            prompt='Dono do mod> ', person_list=person_list)
        mod = Mod(mod_name, mod_owner)
        self._program.mod_dao.save(mod)

        print('\nMod cadastrado com sucesso.')

        self._return_to_previous_screen()

    def _return_to_previous_screen(self) -> None:
        input('\nPressione enter para voltar...')
        self._program.set_screen(
            mod_table_menu_screen.ModTableMenuScreen(self._program))

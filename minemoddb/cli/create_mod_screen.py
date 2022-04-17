from minemoddb.program import Program
from minemoddb.models.person import Person
from minemoddb.models.mod import Mod
from minemoddb.cli.screen import Screen
import minemoddb.cli.mod_table_menu_screen as mod_table_menu_screen


class CreateModScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Cadastro de mod'.upper())

        mod_name = input('Nome> ')
        # TODO: fazer a seleção do dono através da tabela de pessoas.
        mod_owner_name = input('Dono> ')
        mod_owner = Person(mod_owner_name)
        mod = Mod(mod_name, mod_owner)
        self._program._mod_database.add_mod(mod)
        print('Mod cadastrado com sucesso.')
        input('Pressione enter para voltar...')
        self._program.set_screen(
            mod_table_menu_screen.ModTableMenuScreen(self._program))

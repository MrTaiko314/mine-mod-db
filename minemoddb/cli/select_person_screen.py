from minemoddb.program import Program
import minemoddb.cli.person_table_menu_screen as person_table_menu_screen
from minemoddb.cli.screen import Screen
from minemoddb.cli.person_info_screen import PersonInfoScreen


class SelectPersonScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Seleção de pessoa'.upper())

        entries = self._program._person_database.entries
        if len(entries) == 0:
            print('Nenhuma pessoa encontrada.')
            input('Pressione enter para voltar...')
            self._program.set_screen(
                person_table_menu_screen.PersonTableMenuScreen(self._program))
            return

        person = self._program.get_person('Pessoa> ')
        self._program.set_screen(PersonInfoScreen(self._program, person))

from minemoddb.program import Program
import minemoddb.cli.person_table_menu_screen as person_table_menu_screen
from minemoddb.cli.screen import Screen
from minemoddb.cli.person_info_screen import PersonInfoScreen


class SelectPersonScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Seleção de pessoa\n'.upper())

        person_list = self._program._person_database.get_all()
        if len(person_list) == 0:
            print('Nenhuma pessoa encontrada.')

            input('\nPressione enter para voltar...')
            self._program.set_screen(
                person_table_menu_screen.PersonTableMenuScreen(self._program))
            return

        person = self._program.get_person(
            prompt='Pessoa> ', person_list=person_list)
        self._program.set_screen(PersonInfoScreen(self._program, person))

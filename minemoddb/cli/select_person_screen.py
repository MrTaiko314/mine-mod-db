from minemoddb.program import Program
import minemoddb.cli.person_table_menu_screen as person_table_menu_screen
from minemoddb.cli.screen import Screen
from minemoddb.cli.person_info_screen import PersonInfoScreen
from minemoddb.utils import get_number


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

        print(f"Pessoas ({len(entries)}):")
        sorted_person_list = sorted(entries.values(), key=lambda x: x.name)
        for i, person in enumerate(sorted_person_list, 1):
            print(f"{i:3}. {person.name}")

        selected_number = get_number('Seleção> ', 1, len(entries))
        person = sorted_person_list[selected_number - 1]
        self._program.set_screen(PersonInfoScreen(self._program, person))

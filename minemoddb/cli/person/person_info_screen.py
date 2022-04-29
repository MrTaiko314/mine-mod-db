from minemoddb.models.person import Person
from minemoddb.program import Program
from minemoddb.cli.screen import Screen
from minemoddb.cli.person.edit_person_screen import EditPersonScreen
import minemoddb.cli.person.person_table_menu_screen as \
    person_table_menu_screen
from minemoddb.utils import get_option


class PersonInfoScreen(Screen):
    def __init__(self, program: Program, person: Person) -> None:
        self._program = program
        self._person = person

    def show(self) -> None:
        print('Pessoa\n'.upper())

        print(f"Nome: {self._person.name}")

        print('')
        options = ['Editar', 'Voltar']
        option = get_option(options)
        if option == 'Editar':
            self._program.set_screen(
                EditPersonScreen(self._program, self._person))
        elif option == 'Voltar':
            self._program.set_screen(
                person_table_menu_screen.PersonTableMenuScreen(self._program))

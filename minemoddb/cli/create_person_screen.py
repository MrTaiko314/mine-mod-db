from minemoddb.program import Program
from minemoddb.models.person import Person
from minemoddb.cli.screen import Screen
import minemoddb.cli.person_table_menu_screen as person_table_menu_screen


class CreatePersonScreen(Screen):
    def __init__(self, program: Program) -> None:
        self._program = program

    def show(self) -> None:
        print('Cadastro de pessoa'.upper())

        person_name = input('Nome> ')
        person = Person(person_name)
        self._program._person_database.add_person(person)
        print('Pessoa cadastrada com sucesso.')
        input('Pressione enter para voltar...')
        self._program.set_screen(
            person_table_menu_screen.PersonTableMenuScreen(self._program))

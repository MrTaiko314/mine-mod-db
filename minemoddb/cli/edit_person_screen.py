from minemoddb.models.person import Person
from minemoddb.program import Program
from minemoddb.cli.screen import Screen
import minemoddb.cli.person_info_screen as person_info_screen


class EditPersonScreen(Screen):
    def __init__(self, program: Program, person: Person) -> None:
        self._program = program
        self._person = person

    def show(self) -> None:
        print('Editar pessoa\n'.upper())

        edited_name = self._get_edited_name()
        edited_person = Person(edited_name)
        person_id = self._program._person_database.get_person_id(self._person)
        self._program._person_database.modify_person(person_id, edited_person)

        print('\nPessoa editada com sucesso.')

        input('\nPressione enter para voltar...')
        self._program.set_screen(
            person_info_screen.PersonInfoScreen(self._program, edited_person))

    def _get_edited_name(self) -> str:
        edited_name = input(f"Novo nome [{self._person.name}]> ")
        return self._person.name if edited_name == '' else edited_name

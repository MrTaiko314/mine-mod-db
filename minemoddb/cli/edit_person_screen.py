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

        self._person.name = self._get_edited_name()
        self._program.person_dao.update(self._person)

        print('\nPessoa editada com sucesso.')

        input('\nPressione enter para voltar...')
        self._program.set_screen(
            person_info_screen.PersonInfoScreen(self._program, self._person))

    def _get_edited_name(self) -> str:
        edited_name = input(f"Novo nome [{self._person.name}]> ")
        return self._person.name if edited_name == '' else edited_name

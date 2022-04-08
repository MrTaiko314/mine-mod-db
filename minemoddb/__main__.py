from enum import Enum
from typing import Callable


MINE_MOD_DB = 'Mine Mod DB'

menu_stack = []


class MenuOptions(Enum):
    def __init__(self, description: str, handler: Callable[[], None]) -> None:
        self.description = description
        self.handler = handler

    @classmethod
    def option_handler_dict(cls) -> dict[str, Callable[[], None]]:
        return {e.description: e.handler for e in cls}


def get_option(options: list[str]) -> str:
    while True:
        for option_number, option in enumerate(options, 1):
            print(f"{option_number:3}: {option}")
        try:
            selection = int(input('Seleção> '))
        except ValueError:
            pass
        else:
            if selection in range(1, len(options) + 1):
                return options[selection - 1]


def main_menu() -> None:
    print(f"{MINE_MOD_DB}")
    options = [
        MainMenuOptions.TABLE_MENU.description,
        MainMenuOptions.TOOLS_MENU.description,
        MainMenuOptions.END_PROGRAM.description
    ]
    option = get_option(options)
    next_menu = MainMenuOptions.option_handler_dict().get(option, main_menu)
    menu_stack.append(next_menu)


def tables_menu() -> None:
    print(f"{MINE_MOD_DB} > Tabelas")
    options = [
        TablesMenuOptions.PEOPLE_MENU.description,
        TablesMenuOptions.MODS_MENU.description,
        TablesMenuOptions.MODPACKS_MENU.description,
        TablesMenuOptions.RETURN_TO_PREVIOUS_MENU.description
    ]
    option = get_option(options)
    next_menu = TablesMenuOptions.option_handler_dict().get(
        option, tables_menu)
    menu_stack.append(next_menu)


def people_menu() -> None:
    print(f"{MINE_MOD_DB} > Tabelas > Pessoas")
    options = [
        PeopleMenuOptions.CREATE_PERSON.description,
        PeopleMenuOptions.MODIFY_PERSON.description,
        PeopleMenuOptions.REMOVE_PERSON.description,
        PeopleMenuOptions.RETURN_TO_PREVIOUS_MENU.description
    ]
    option = get_option(options)
    next_menu = PeopleMenuOptions.option_handler_dict().get(
        option, people_menu)
    menu_stack.append(next_menu)


def create_person_page() -> None:
    print('Cadastrar nova pessoa')
    # TODO: implementar


def modify_person_page() -> None:
    print('Modificar pessoa existente')
    # TODO: implementar


def remove_person_page() -> None:
    print('Remover pessoa existente')
    # TODO: implementar


def mods_menu() -> None:
    print(f"{MINE_MOD_DB} > Tabelas > Mods")
    options = [
        ModsMenuOptions.CREATE_MOD.description,
        ModsMenuOptions.MODIFY_MOD.description,
        ModsMenuOptions.REMOVE_MOD.description,
        ModsMenuOptions.RETURN_TO_PREVIOUS_MENU.description
    ]
    option = get_option(options)
    next_menu = ModsMenuOptions.option_handler_dict().get(option, people_menu)
    menu_stack.append(next_menu)


def create_mod_page() -> None:
    print('Cadastrar novo mod')
    # TODO: implementar


def modify_mod_page() -> None:
    print('Modificar mod existente')
    # TODO: implementar


def remove_mod_page() -> None:
    print('Remover mod existente')
    # TODO: implementar


def modpacks_menu() -> None:
    print(f"{MINE_MOD_DB} > Tabelas > Modpacks")
    options = [
        ModpacksMenuOptions.CREATE_MODPACK.description,
        ModpacksMenuOptions.MODIFY_MODPACK.description,
        ModpacksMenuOptions.REMOVE_MODPACK.description,
        ModpacksMenuOptions.RETURN_TO_PREVIOUS_MENU.description
    ]
    option = get_option(options)
    next_menu = ModpacksMenuOptions.option_handler_dict().get(
        option, people_menu)
    menu_stack.append(next_menu)


def create_modpack_page() -> None:
    print('Cadastrar novo modpack')
    # TODO: implementar


def modify_modpack_page() -> None:
    print('Modificar modpack existente')
    # TODO: implementar


def remove_modpack_page() -> None:
    print('Remover modpack existente')
    # TODO: implementar


def tools_menu() -> None:
    print(f"{MINE_MOD_DB} > Ferramentas")
    options = [
        ToolsMenuOptions.FILTER_MOD_AND_MODPACK_BY_AUTHOR.description,
        ToolsMenuOptions.LIST_MODPACK_MODS.description,
        ToolsMenuOptions.FILTER_MODPACKS_BY_CONTAINED_MOD.description,
        ToolsMenuOptions.RETURN_TO_PREVIOUS_MENU.description
    ]
    option = get_option(options)
    next_menu = ToolsMenuOptions.option_handler_dict().get(option, tools_menu)
    menu_stack.append(next_menu)


def filter_mod_modpack_by_author_page() -> None:
    print('Filtrar mods e modpacks por autor')


def list_modpack_mods_page() -> None:
    print('Listar mods de um modpack')


def filter_modpacks_by_mod_page() -> None:
    print('Filtrar modpacks por mods contidos')


def end_program_page() -> None:
    print('Tchau.')


class MainMenuOptions(MenuOptions):
    TABLE_MENU = ('Tabelas', tables_menu)
    TOOLS_MENU = ('Ferramentas', tools_menu)
    END_PROGRAM = ('Sair', end_program_page)


class ToolsMenuOptions(MenuOptions):
    FILTER_MOD_AND_MODPACK_BY_AUTHOR = (
        'Filtrar mods e modpacks por autor', filter_mod_modpack_by_author_page)
    LIST_MODPACK_MODS = ('Listar mods de um modpack', list_modpack_mods_page)
    FILTER_MODPACKS_BY_CONTAINED_MOD = (
        'Filtrar modpacks por mods contidos', filter_modpacks_by_mod_page)
    RETURN_TO_PREVIOUS_MENU = ('Voltar', main_menu)


class TablesMenuOptions(MenuOptions):
    PEOPLE_MENU = ('Pessoas', people_menu)
    MODS_MENU = ('Mods', mods_menu)
    MODPACKS_MENU = ('Modpacks', modpacks_menu)
    RETURN_TO_PREVIOUS_MENU = ('Voltar', main_menu)


class PeopleMenuOptions(MenuOptions):
    CREATE_PERSON = ('Cadastrar nova pessoa', create_person_page)
    MODIFY_PERSON = ('Modificar pessoa existente', modify_person_page)
    REMOVE_PERSON = ('Remover pessoa existente', remove_person_page)
    RETURN_TO_PREVIOUS_MENU = ('Voltar', tables_menu)


class ModsMenuOptions(MenuOptions):
    CREATE_MOD = ('Cadastrar novo mod', create_mod_page)
    MODIFY_MOD = ('Modificar mod existente', modify_mod_page)
    REMOVE_MOD = ('Remover mod existente', remove_mod_page)
    RETURN_TO_PREVIOUS_MENU = ('Voltar', tables_menu)


class ModpacksMenuOptions(MenuOptions):
    CREATE_MODPACK = ('Cadastrar novo modpack', create_modpack_page)
    MODIFY_MODPACK = ('Modificar modpack existente', modify_modpack_page)
    REMOVE_MODPACK = ('Remover modpack existente', remove_modpack_page)
    RETURN_TO_PREVIOUS_MENU = ('Voltar', tables_menu)


def main() -> None:
    menu_stack.append(main_menu)
    while menu_stack:
        menu_stack.pop()()


if __name__ == '__main__':
    main()

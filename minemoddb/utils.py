def get_option(options: list[str]) -> str:
    while True:
        print('Opções:')
        for option_number, option in enumerate(options, 1):
            print(f"{option_number:3}: {option}")
        try:
            selection = int(input('Seleção> '))
        except ValueError:
            pass
        else:
            if selection in range(1, len(options) + 1):
                return options[selection - 1]


def get_number(
        prompt: str, min_value: int | None = None,
        max_value: int | None = None) -> int:
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print('Digite um número.')
        else:
            if min_value is not None and number < min_value:
                print(f"O número deve ser maior ou igual que {min_value}.")
                continue

            if max_value is not None and number > max_value:
                print(f"O número deve ser menor ou igual que {max_value}.")
                continue

            return number


def clear_screen() -> None:
    print('\x1b[1;1H\x1b[0J', end='')

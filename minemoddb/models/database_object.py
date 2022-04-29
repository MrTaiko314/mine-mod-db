class DatabaseObject:
    """Classe base para todos os objetos que precisam de persistência."""

    def __init__(self, id: int) -> None:
        self.id = id

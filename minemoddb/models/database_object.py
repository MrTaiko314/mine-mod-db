class DatabaseObject:
    """Classe base para todos os objetos que precisam de persistĂȘncia."""

    def __init__(self, id: int) -> None:
        self.id = id

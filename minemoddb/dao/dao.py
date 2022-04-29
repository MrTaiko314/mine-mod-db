from abc import ABC, abstractmethod
from typing import Generic, TypeVar


T = TypeVar('T')


class Dao(ABC, Generic[T]):
    """Interface genérica base para todos os DAOs.

    Um DAO (Objeto de Acesso aos Dados) é um objeto ou uma interface
    que fornece acesso a um banco de dados ou qualquer outro
    armazenamento persistente.
    """

    @abstractmethod
    def get(self, id: int) -> T:
        """Retorna o primeiro objeto armazenado com o ID passado."""
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[T]:
        """Retorna todos os objetos armazenados."""
        raise NotImplementedError

    @abstractmethod
    def save(self, obj: T) -> int:
        """Armazena o objeto passado e retorna o ID criado para ele."""
        raise NotImplementedError

    @abstractmethod
    def update(self, obj: T) -> None:
        """Atualiza o objeto correspondente armazenado."""
        raise NotImplementedError

    @abstractmethod
    def delete(self, obj: T) -> bool:
        """Deleta o objeto correspondente armazenado."""
        raise NotImplementedError

    @abstractmethod
    def delete_all(self) -> None:
        """Deleta todos os objetos armazenados."""
        raise NotImplementedError

from abc import ABC, abstractmethod

DAMAGE_TYPES = 'PHY', 'MAG', 'EX'

class Ser_Vivo(ABC):
    def __init__(self, hp: int, forca: int, velocidade: int, inteligencia: int, rank: str) -> None:
        self._hp = hp
        self._forca = forca
        self._velocidade = velocidade
        self._inteligencia = inteligencia
        self.rank = rank

    @abstractmethod   
    def atacar(self, alvo) -> float:
        pass

    @abstractmethod
    def receber_dano(self, dano: int) -> None:
        pass

    @abstractmethod
    def morrer(self) -> None:
        pass

class Dano:
    def __init__(self, value: float, type: str) -> None:
        self.value = value
        self.type = type

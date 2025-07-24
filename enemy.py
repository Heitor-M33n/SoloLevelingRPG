from player import *
from classe import *

class Enemy(Ser_Vivo):
    def __init__(self, nome: str, hp: int, forca: int, velocidade: int, inteligencia: int, defesa: int, rank: str, exp_drop: int, type_weakness: dict[str, float] = {'PHY': 1.0, 'MAG': 1.0}) -> None:
        super.__init__(hp, forca, velocidade, inteligencia, rank)
        self.defesa = defesa
        self.nome = nome
        self.exp_drop = exp_drop
        self.type_weakness = type_weakness

    @property
    def hp(self) -> int:
        return self._hp
    
    @property
    def forca(self) -> int:
        return self._forca
    
    @property
    def velocidade(self) -> int:
        return self._velocidade

    @property
    def inteligencia(self) -> int:
        return self._inteligencia

    def atacar(self, alvo, type: str, mult: float = 1.0):
        if not isinstance(alvo, Ser_Vivo):
            return

        if type.upper() == "PHY":
            dano = round((self.forca + self.velocidade / 3) * mult, 2)
        if type.upper() == "MAG":
            dano = round((self.inteligencia + self.velocidade / 5) * mult, 2)

        alvo.receber_dano(dano)
    
    def receber_dano(self):
        pass

    def morrer(self, player: Player) -> None:
        if not isinstance(player, Player):
            return
        

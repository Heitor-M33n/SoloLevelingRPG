EXP_MULT = 1.1
RANK_UP_INCREMENT = 5

RANKS = ['E', 'D', 'C', 'B', 'A', 'S', 'Nacional', 'Monarca']

CLASSES = {'Assasino': {'hp': 0.8, 'forca': 1.0, 'velocidade': 1.6, 'inteligencia': 1.0},
  'Lutador': {'hp': 1.0, 'forca': 1.6, 'velocidade': 1.0, 'inteligencia': 0.8},
  'Tanque': {'hp': 1.8, 'forca': 1.2, 'velocidade': 0.8, 'inteligencia': 0.6},
  'Mago': {'hp': 0.6, 'forca': 0.8, 'velocidade': 1.0, 'inteligencia': 2.0}
}

class Player:
  def __init__(self, classe: str = 'Assasino') -> None:
    class_mult = CLASSES[classe]
    self._hp = 100
    self._forca = 5
    self._velocidade = 5
    self._inteligencia = 5
    self._classe = classe
    self._rank = 'E'
    self._level = 1
    self._rank_up_level = RANK_UP_INCREMENT
    self._exp_dados = {'acumulado': 0, 'necessario': 100}

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
  
  @property
  def classe(self) -> int:
    return self._classe

  @property
  def rank(self) -> str:
    return self._rank

  @property
  def level(self) -> int:
    return self._level

  @property
  def rank_up_level(self) -> int:
    return self._rank_up_level

  @property
  def exp_dados(self) -> dict[str, int]:
    return self._exp_dados

  def rank_up(self) -> None:
    self._rank = RANKS[RANKS.index(self._rank) + 1]
    if self.rank in RANKS[:4]: # Todos abaixo de A
      self._rank_up_level += RANK_UP_INCREMENT
    elif self.rank == 'A':
      self._rank_up_level += RANK_UP_INCREMENT * 2
    elif self.rank == 'S':
      self._rank_up_level += RANK_UP_INCREMENT * 4
    elif self.rank == 'Nacional':
      self._rank_up_level += RANK_UP_INCREMENT * 8
    else:
      self._rank_up_level = None

  def level_up(self, vezes: int = 1) -> None:
    for i in range(vezes):
      self._exp_dados['acumulado'] = 0
      self._exp_dados['necessario'] = int(self.exp_dados['necessario'] * EXP_MULT)
      self._level += 1
      
      if self.level == self.rank_up_level:
        self.rank_up()
  
  def ganhar_exp(self, exp: int, mult: float = 1.0) -> None:
    exp = int(exp * mult)
    while exp >= self.exp_dados['necessario'] - self.exp_dados['acumulado']: #enquanto conseguir upar de nível:
      exp -= self.exp_dados['necessario'] - self.exp_dados['acumulado']
      self.level_up()

    self._exp_dados['acumulado'] += exp

if __name__ == '__main__': #Testando o sistema de exp de Player
  player = Player()

  player.ganhar_exp(69)
  print(f"Level: {player.level}, Exp: {player.exp_dados['acumulado']}/{player.exp_dados['necessario']}, Rank: {player.rank}\n")
  player.ganhar_exp(650)
  print(f"Level: {player.level}, Exp: {player.exp_dados['acumulado']}/{player.exp_dados['necessario']}, Rank: {player.rank}\n")
  player.ganhar_exp(1800)
  print(f"Level: {player.level}, Exp: {player.exp_dados['acumulado']}/{player.exp_dados['necessario']}, Rank: {player.rank}\n")
  player.ganhar_exp(4500)
  print(f"Level: {player.level}, Exp: {player.exp_dados['acumulado']}/{player.exp_dados['necessario']}, Rank: {player.rank}\n")
  player.ganhar_exp(8500)
  print(f"Level: {player.level}, Exp: {player.exp_dados['acumulado']}/{player.exp_dados['necessario']}, Rank: {player.rank}\n")
  player.ganhar_exp(30000)
  print(f"Level: {player.level}, Exp: {player.exp_dados['acumulado']}/{player.exp_dados['necessario']}, Rank: {player.rank}\n")
  player.ganhar_exp(70000)
  print(f"Level: {player.level}, Exp: {player.exp_dados['acumulado']}/{player.exp_dados['necessario']}, Rank: {player.rank}\n")
  player.ganhar_exp(3500000)
  print(f"Level: {player.level}, Exp: {player.exp_dados['acumulado']}/{player.exp_dados['necessario']}, Rank: {player.rank}\n")
  player.ganhar_exp(500000)
  print(f"Level: {player.level}, Exp: {player.exp_dados['acumulado']}/{player.exp_dados['necessario']}, Rank: {player.rank}\n")
  player.ganhar_exp(5000000000)
  print(f"Level: {player.level}, Exp: {player.exp_dados['acumulado']}/{player.exp_dados['necessario']}, Rank: {player.rank}\n")
  player.ganhar_exp(1000000000)
  print(f"Level: {player.level}, Exp: {player.exp_dados['acumulado']}/{player.exp_dados['necessario']}, Rank: {player.rank}\n")
  player.ganhar_exp(10000000000000000000)
  print(f"Level: {player.level}, Exp: {player.exp_dados['acumulado']}/{player.exp_dados['necessario']}, Rank: {player.rank}\n")
  #Os números começam a ficar grandes, mas o sistema de exp funciona bem, balancear depois a questão dos multiplicadores de exp.
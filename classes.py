EXP_MULT = 1.1
RANK_UP_MULT = 5

RANKS = ['E', 'D', 'C', 'B', 'A', 'S', 'Nacional', 'Monarca']

CLASSES = {
  'Assasino': {'hp': 0.8, 'forca' = 1.0, 'velocidade' = 1.6, 'inteligencia' = 1.0},
  'Lutador': {'hp': 1.0, 'forca' = 1.6, 'velocidade' = 1.0, 'inteligencia' = 0.8},
  'Tanque': {'hp': 1.8, 'forca' = 1.2, 'velocidade' = 0.8, 'inteligencia' = 0.6},
  'Mago': {'hp': 0.6, 'forca' = 0.8, 'velocidade' = 1.0, 'inteligencia' = 2.0}
}

class Player:
  def __init__(self, classe: dict{str: float}) -> None:
    self._hp = 100
    self._forca = 5
    self._velocidade = 5
    self._inteligencia = 5
    self._rank = 'E'
    self._level = 1
    self._exp_dados = {'acumulado': 0, 'necessario': 100, 'total': 0}

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
  def level(self) -> int:
    return self._level

  @property
  def _exp_dados(self) -> int:
    return self._exp_dados

  def rank_up(self) -> None:
    pass

  def level_up(self) -> None:
    self._exp_dados['acumulado'] = 0
    self._exp_dados['necessario'] *= EXP_MULT
    self._level += 1
    if self._level == RANK_UP_LEVEL:
      self.rank_up()
  
  def ganhar_exp(self, exp: int) -> None:
    self._exp_dados['total'] += exp
    while exp >= self._exp_dados['necessario'] - self._exp_dados['acumulado']: #enquanto conseguir upar de nível:
      exp -= self._exp_dados['necessario'] - self._exp_dados['acumulado']
      self.level_up()
      
    self._exp_dados['acumulado'] += exp

STATUS_MULT = 1.1 #Multiplicador padrão de status do jogador, usado para aumentar os atributos de combate ao subir de nível.
EXP_MULT = 1.1 #Multiplicador de experiência necessário para o próximo nível. A cada nível, a experiência necessária aumenta baseada nesse multiplicador.
RANK_UP_INCREMENT = 5 #Incremento inicial para o rank up, que aumenta conforme o rank do jogador. Para ranks mais altos, o incremento é maior.
#Um EXP_MULT mais alto significa que o jogador precisa de mais experiência para subir de nível, necessitando de um RANK_UP_INCREMENT menor para balancear.

RANKS = ['E', 'D', 'C', 'B', 'A', 'S', 'Nacional', 'Monarca'] #Ranks disponíveis para o jogador, do mais baixo (E) ao mais alto (Monarca).

CLASSES = {'Assasino': {'hp': 0.8, 'forca': 1.2, 'velocidade': 1.4, 'inteligencia': 1.0},
  'Lutador': {'hp': 1.0, 'forca': 1.6, 'velocidade': 1.0, 'inteligencia': 0.8},
  'Tanque': {'hp': 2.0, 'forca': 1.0, 'velocidade': 0.8, 'inteligencia': 0.6},
  'Mago': {'hp': 0.6, 'forca': 0.8, 'velocidade': 1.0, 'inteligencia': 2.0}
} #Dicionário de classes disponíveis, com multiplicadores fixos para cada atributo de combate.

class Player:
  """Classe que representa um jogador no jogo, com atributos e métodos para gerenciar experiência, nível e rank.

    Attributes:
      hp (float): Pontos de vida do jogador, multiplicados pela classe (ele morre se chegar a 0 :O ).
      forca (float): Força de ataque do jogador, multiplicada pela classe. Responsável por determinar o dano de ataques físicos e outras ações.
      velocidade (float): Velocidade de movimento do jogador, multiplicada pela classe. Responsável por determinar quem ataca primeiro e outras ações.
      inteligencia (float): Inteligência do jogador, multiplicada pela classe. Responsável por determinar o dano de magia e outras coisas.
      classe (str): Classe do jogador, que afeta os multiplicadores dos atributos de combate.
      rank (str): Rank do jogador, que determina sua força e dungeons disponíveis.
      level (int): Nível atual do jogador.
      rank_up_level (int): Nível necessário para o próximo rank up.
      exp_dados (dict): Dados de experiência acumulada e necessária para o próximo nível.
  """
  def __init__(self, classe: str = 'Assasino') -> None:
    """Inicializa um novo jogador com atributos padrão e a classe especificada.

    Args:
      classe (str): Classe do jogador, deve ser uma das chaves em CLASSES. Padrão é 'Assasino'.
    """
    self._hp = 100.0
    self._forca = 5.0
    self._velocidade = 5.0
    self._inteligencia = 5.0
    self.classe = classe
    self.rank = 'E'
    self.level = 1
    self.rank_up_level = RANK_UP_INCREMENT
    self._exp_dados = {'acumulado': 0, 'necessario': 100}

  @property
  def hp(self) -> int:
    """Retorna os pontos de vida do jogador, multiplicados pelo multiplicador da classe.

    returns:
      int: Pontos de vida do jogador, arredondados para o inteiro mais próximo.
    """
    return round(self._hp * CLASSES[self.classe]['hp'])

  @property
  def forca(self) -> int:
    """Retorna a força do jogador, multiplicada pelo multiplicador da classe.

    returns:
      int: Força do jogador, arredondada para o inteiro mais próximo.
    """
    return round(self._forca * CLASSES[self.classe]['forca'], 1)

  @property
  def velocidade(self) -> int:
    """Retorna a velocidade do jogador, multiplicada pelo multiplicador da classe.

    returns:
      int: Velocidade do jogador, arredondada para o inteiro mais próximo.
    """
    return round(self._velocidade * CLASSES[self.classe]['velocidade'], 1)
  
  @property
  def inteligencia(self) -> int:
    """Retorna a inteligência do jogador, multiplicada pelo multiplicador da classe.

    returns:
      int: Inteligência do jogador, arredondada para o inteiro mais próximo.
    """
    return round(self._inteligencia * CLASSES[self.classe]['inteligencia'], 1)

  @property
  def exp_dados(self) -> dict[str, int]:
    """Retorna os dados de experiência acumulada e necessária para o próximo nível.

    returns:
      dict[str, int]: Dicionário contendo 'acumulado' e 'necessario' como chaves, representando a experiência acumulada e a necessária para o próximo nível, respectivamente.
    """
    return self._exp_dados

  def upar_status_soma(self, hp: int, forca: int, velocidade: int, inteligencia: int) -> None:
    """Aumenta os atributos de combate do jogador com base nos valores fornecidos.

    Args:
      hp (int): Quantidade de pontos de vida a ser adicionada.
      forca (int): Quantidade de força a ser adicionada.
      velocidade (int): Quantidade de velocidade a ser adicionada.
      inteligencia (int): Quantidade de inteligência a ser adicionada.
    """
    self._hp + hp
    self._forca += forca
    self._velocidade += velocidade
    self._inteligencia += inteligencia

  def upar_status_mult(self, all: float = STATUS_MULT, hp: float = 0.0, forca: float = 0.0, velocidade: float = 0.0, inteligencia: float = 0.0) -> None:
    """Aumenta os atributos de combate do jogador com base nos multiplicadores fornecidos.

    Se um multiplicador específico não for fornecido, usa o multiplicador padrão (STATUS_MULT) para todos os atributos. Se fornecido, aplica o multiplicador específico para esse atributo.

    Args:
      all (float): Multiplicador para todos os atributos de combate, por padrão é STATUS_MULT. 
      hp (float): Multiplicador para os pontos de vida. Padrão é 0.0.
      forca (float): Multiplicador para a força. Padrão é 0.0.
      velocidade (float): Multiplicador para a velocidade. Padrão é 0.0.
      inteligencia (float): Multiplicador para a inteligência. Padrão é 0.0.
    """

    if not hp:
      hp = all

    if not forca:
      forca = all

    if not velocidade:
      velocidade = all

    if not inteligencia:
      inteligencia = all

    self._hp = round(self._hp * hp, 2)
    self._forca = round(self._forca * forca, 2)
    self._velocidade = round(self._velocidade * velocidade, 2)
    self._inteligencia = round(self._inteligencia * inteligencia, 2)

  def rank_up(self) -> None:
    """Promove o jogador para o próximo rank, ajustando o nível necessário para o próximo rank up.

    Para ranks mais baixos (E, D, C, B), o incremento é menor. Para rank A, o incremento é maior (2x). Para rank S, é ainda maior (4x). E para rank Nacional, é o maior (8x).
    """
    self.rank = RANKS[RANKS.index(self.rank) + 1]

    if self.rank in RANKS[:4]: # Todos abaixo de A
      self.upar_status_mult(all = 1.5)
      self.rank_up_level += RANK_UP_INCREMENT
    elif self.rank == 'A':
      self.upar_status_mult(all = 2.0)
      self.rank_up_level += RANK_UP_INCREMENT * 2
    elif self.rank == 'S':
      self.upar_status_mult(all = 3.0)
      self.rank_up_level += RANK_UP_INCREMENT * 4
    elif self.rank == 'Nacional':
      self.upar_status_mult(all = 4.0)
      self.rank_up_level += RANK_UP_INCREMENT * 8
    else: #monarca
      self.upar_status_mult(all = 5.0)
      self.rank_up_level = None

  def level_up(self, vezes: int = 1) -> None:
    """Aumenta o nível do jogador, ajustando a experiência necessária para o próximo nível e aumentando seus atributos.

    Se o jogador atingir o nível necessário para rank up, chama o método rank_up.

    Args:
      vezes (int): Número de vezes que o jogador deve subir de nível. Padrão é 1.
    """
    for i in range(vezes):
      self._exp_dados['acumulado'] = 0
      self._exp_dados['necessario'] = int(self.exp_dados['necessario'] * EXP_MULT)
      self.level += 1
      self.upar_status_mult()
      
      if self.rank in ['E', 'D']: # Todos abaixo de A
        self.upar_status_soma(10, 1, 1, 1)
      elif self.rank in ['C', 'B']:
        self.upar_status_soma(20, 2, 2, 2)
      elif self.rank == 'A':
        self.upar_status_soma(30, 3, 3, 3)
      elif self.rank == 'S':
        self.upar_status_soma(40, 4, 4, 4)
      elif self.rank == 'Nacional':
        self.upar_status_soma(50, 5, 5, 5)
      else: #monarca
        self.upar_status_soma(100, 10, 10, 10)

      if self.level == self.rank_up_level:
        self.rank_up()
  
  def ganhar_exp(self, exp: int, mult: float = 1.0) -> None:
    """Adiciona experiência ao jogador, atualizando os dados de experiência acumulada e necessária.

    Se a experiência acumulada atingir ou ultrapassar a necessária para o próximo nível, chama o método level_up.

    Args:
      exp (int): Quantidade de experiência a ser adicionada.
      mult (float): Multiplicador de experiência a ser aplicado. Padrão é 1.0.
    """
    exp = int(exp * mult)
    while exp >= self.exp_dados['necessario'] - self.exp_dados['acumulado']: #enquanto conseguir upar de nível:
      exp -= self.exp_dados['necessario'] - self.exp_dados['acumulado']
      self.level_up()

    self._exp_dados['acumulado'] += exp

  def __str__(self) -> str:
    """Retorna uma representação em string do jogador, incluindo classe, rank, nível e atributos de combate.
    """
    return f"Player {self.classe}, rank {self.rank}, level {self.level} ({self.exp_dados['acumulado']}/{self.exp_dados['necessario']}), stats: hp = {self.hp} ({self._hp}), forca = {self.forca} ({self._forca}), velocidade = {self.velocidade} ({self._velocidade}), inteligencia = {self.inteligencia} ({self._inteligencia})"

if __name__ == '__main__':
  player = Player()
  player.ganhar_exp(1)
  print(player)
  player.ganhar_exp(462)
  print(player)
  player.ganhar_exp(1)
  print(player)
  player.ganhar_exp(886)
  print(player)
  player.ganhar_exp(1)
  print(player)
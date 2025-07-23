EXP_MULT = 1.2

class Player:
  def __init__(self) -> None:
    self._health = 100
    self._def = 3
    self._speed = 3
    self._level = 1
    self._total_xp = 0
    self._required_xp = 100

  def gain_exp(self, xp: int) -> None:
    if self._re

  def level_up(self) -> None:
    self.level

  @property
  def level(self) -> int:
    return self._level

  @level.setter
  def level(self, increment) -> None: 

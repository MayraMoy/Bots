from itertools import combinations
from typing import List, Tuple

from bot_abstract import BotAbstract

#Está diseñada para generar un calendario de enfrentamientos
class Fixture:
    #Recibe una lista de bots (bots) que implementan la clase BotAbstract.
    def __init__(self, bots: List[BotAbstract]):
        self.bots = bots
        #Para generar el enfrentamientos entre los bots.
        self.fixture = self._generate_fixture()

    #Utiliza combinations de la librería itertools para generar todas las posibles combinaciones de enfrentamientos 
    #de dos en dos entre los bots.
    #El resultado es una lista de tuplas, donde cada tupla contiene dos bots que se enfrentarán.
    def _generate_fixture(self) -> List[Tuple[BotAbstract, BotAbstract]]:
        return list(combinations(self.bots, 2))

    #Devuelve la lista de enfrentamientos generada por _generate_fixture. Este método no modifica el fixture; 
    #simplemente lo devuelve en la misma forma en que fue generado.
    def get_fixture(self) -> List[Tuple[BotAbstract, BotAbstract]]:
        return [(bot1, bot2) for bot1, bot2 in self.fixture]
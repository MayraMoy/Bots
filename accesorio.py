#Permite generar todas las combinaciones posibles (en este caso entre los bots).
from itertools import combinations
#Se usa para anotar los tipos en Python, en este caso, listas y tuplas.
from typing import List, Tuple

# Importa la clase base para los bots.
from bot_abstract import BotAbstract

#La clase Fixture crea un "fixture", o calendario, para enfrentar a todos los bots entre sí.
class Fixture:
    #Inicializa la clase con una lista de bots y genera el fixture, es decir, todos los emparejamientos posibles entre los bots.
    def __init__(self, bots: List[BotAbstract]):
        self.bots = bots
        self.fixture = self._generate_fixture()

    #Este método genera todas las combinaciones posibles de pares de bots (bot1, bot2) usando itertools.combinations
    def _generate_fixture(self) -> List[Tuple[BotAbstract, BotAbstract]]:
        return list(combinations(self.bots, 2))

    #Devuelve una lista de todos los emparejamientos generados en _generate_fixture. Aquí se itera sobre self.fixture y se retornan los emparejamientos tal como están.
    def get_fixture(self) -> List[Tuple[BotAbstract, BotAbstract]]:
        return [(bot1, bot2) for bot1, bot2 in self.fixture]
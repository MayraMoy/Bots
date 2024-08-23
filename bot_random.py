import random
from bot_abstract import BotAbstract

class BotRandom(BotAbstract):
    
    @property
    def Nombre(self) -> str:
        return "Random"

    #Este bot seleccionará de manera completamente aleatoria entre estas dos opciones, 
    #sin considerar el número de la jugada ni la jugada previa del oponente.
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        return random.choice(['M', 'S'])
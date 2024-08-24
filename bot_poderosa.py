import random
from bot_abstract import BotAbstract

class Bot_las_Chicas_Super_Poderosas(BotAbstract):
    @property
    def Nombre(self) -> str:
        return "Las Chicas Super Poderosas"
    
    def __init__(self):
        self.historial_oponente = []

    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        if jugada_previa_oponente:
            self.historial_oponente.append(jugada_previa_oponente)

        if len(self.historial_oponente) > 1:
            ultima_jugada = self.historial_oponente[-1]
            penultima_jugada = self.historial_oponente[-2]

            # Si el oponente juega "Sapo" dos veces seguidas, lanza "Murciélago"
            if ultima_jugada == 'S' and penultima_jugada == 'S':
                return 'M'
            # Si el oponente juega "Murciélago" dos veces seguidas, lanza "Sapo"
            elif ultima_jugada == 'M' and penultima_jugada == 'M':
                return 'S'
            else:
                # Introduce aleatoriedad: elige aleatoriamente "Murciélago" o "Sapo"
                return random.choice(['M', 'S'])
        else:
            # Primera jugada, elige aleatoriamente
            return random.choice(['M', 'S'])










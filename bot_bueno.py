from bot_abstract import BotAbstract

class BotBueno(BotAbstract):
    
    @property
    def Nombre(self) -> str:
        return "Bueno"
    
    #Este bot al momento de jugar siempre arrojara una carta "Sapo".
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        return 'S'
    
    
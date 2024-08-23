from bot_abstract import BotAbstract

class BotPoderosa(BotAbstract):
    
    @property
    def Nombre(self) -> str:
        return "Poderosa"
    
    #Se inicializa una lista historial_oponente para almacenar las jugadas 
    #anteriores del oponente.
    def __init__(self): #Hace referencia al objeto que se está manipulando cuando se llama al método.
        self.historial_oponente = []
    
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        # Guardar la jugada previa del oponente
        if jugada_previa_oponente:
            #con la funcion append vamos a guardar las jugadas del adversario en la lista que
            #creamos "historial_oponente"
            self.historial_oponente.append(jugada_previa_oponente)
        
        # Análisis de patrones
        #Con la funcion len contara la cantidad de elementos de la lista. 
        #Abrimos el if para analizar el historial del oponente y si este es mayor a 1 
        #se ejejutara otro if de la cual anteriormente habremos creado una variable llamada "ultima jugada"
        #que guardara la ultima jugada del oponente [-1]
        if len(self.historial_oponente) > 1:
            ultima_jugada = self.historial_oponente[-1]
            #Si la ultima jugada del oponente es un Sapo lanzar un Murcielago
            if ultima_jugada == 'S':
                return 'M'  
            else:
                #Pero si el oponente juega con Murcielago entonces devolver Sapo
                return 'S'  
        else:
            #Primera jugada, elegir aleatoriamente
            #Decide qué jugada realizar en función de si el número de jugada (jugada_numero) es par o impar:
            #Murcielago si es par y si es impar Sapo
            return 'M' if jugada_numero % 2 == 0 else 'S'

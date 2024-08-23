#La clase abstracta (ABC) para un bot con dos métodos abstractos. 
from abc import ABC, abstractmethod

class BotAbstract(ABC):
    
    #Se utiliza para definir un método como una propiedad, lo que significa que se puede 
    #acceder a él como si fuera un atributo. En este caso, Nombre es una propiedad abstracta 
    #que debe ser implementada por cualquier subclase.
    @property
    @abstractmethod
    def Nombre(self) -> str:
        pass
    
    #Este decorador obliga a que el método sea implementado por cualquier subclase de 
    #BotAbstract. En tu ejemplo, Jugar es un método abstracto que toma dos parámetros 
    #(jugada_numero y jugada_previa_oponente) y devuelve una cadena de texto.
    @abstractmethod
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        pass

    
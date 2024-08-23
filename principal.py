import time

#Importan los modulos.py
from Arena import Arena
from bot_bueno import BotBueno
from bot_random import BotRandom
from bot_poderoso import BotPoderosa
from fixture import Fixture

#crea una lista con los bots que van a competir
bots = [BotBueno(), BotRandom(), BotPoderosa()]
#esto generara el calendario de enfrentamientos
fixture = Fixture(bots)
#Llama al método get_fixture() para obtener la lista de partidos, que es una lista de tuplas.
#Cada tupla contiene dos bots que se enfrentarán.
partidos = fixture.get_fixture()

#Se crea un diccionario tabla_posiciones donde cada bot de la lista bots es una clave,
#y el valor asociado es 0, que representa el puntaje inicial del bot.
tabla_posiciones = {}
for bot in bots:
    tabla_posiciones[bot] = 0

numeroDePartido = 1
for bot1, bot2 in partidos:
    #En cada iteración, se imprime el número de partido y los nombres de los bots que están combatiendo.
    print("\nPartido", numeroDePartido)
    print("Combate entre ", bot1.Nombre, bot2.Nombre)
    time.sleep(2) #pausa de 2 segundos entre los partidos 

    #Devuelve los puntos obtenidos por cada bot en ese partido.
    puntaje_bot1, puntaje_bot2 = Arena.Jugar(bot1, bot2)
    tabla_posiciones[bot1] += puntaje_bot1
    tabla_posiciones[bot2] += puntaje_bot2

    #Utilizando sorted() con una función lambda ordena por el segundo elemento de cada tupla (x[1]), 
    #que es el puntaje de mayor a menor.
    print("\n\nTabla de Posiciones:")
    sorted_posiciones = sorted(tabla_posiciones.items(), key=lambda x: x[1], reverse=True)
    for bot, puntos in sorted_posiciones:
        print(bot.Nombre, puntos, sep="\t|\t")

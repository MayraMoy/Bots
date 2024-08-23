#creamos la funcion juego
def Juego():
    #Creamos la variable que guardara en una lista las jugadas que hara el usuario
    cartas = []
    #Le preguntamos 3 veces solamente para poder tener una lista mas amplia para buscar
    for _ in range(3):
        carta = input("Ingresa una carta (M = 2, S = 1): ")
        #agregamos las respuestas en li lista llamada cartas
        cartas.append(carta)

    #de acuerdo a la respuesta del usuario respondera
    nuestra = cartas[-1]
    if nuestra == '1':
        return 'Tiro un 2'
    else:
        return 'Tiro un 1'

# Llama a la función para jugar
resultado = Juego()
print(resultado)


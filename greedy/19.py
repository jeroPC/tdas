""" Nos proponen el siguiente juego de cartas en el que tenemos que adivinar la carta que
tiene un rival. El mazo tiene 1 carta de “1 de Oro”, 2 cartas de “2 de Oro” y así hasta 9 cartas
de “9 de Oro”. El rival mezcla y selecciona una carta. Mediante preguntas que solo se pueden
responder por sí o por no tenemos que averiguar en la menor cantidad de consultas cual es
la carta. (ejemplos: “La carta es mayor a 4?, “La carta es un “1” o un “3”, etc). Proponer un
algoritmo greedy que resuelva el problema minimizando la cantidad probable de preguntas
a realizar."""
cartas = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]

def preguntas_greedy(cartas):
    intentos = 0

    while len(cartas) > 1: 
        peso_total = sum(cartas[i][1] for i in range(len(cartas)))
        mitad_ideal = peso_total / 2
        
        mejor_k  = 0
        menor_diferencia = float('inf')
        suma_acumulada = 0

        for i in range(len(cartas)-1):
            suma_acumulada += cartas[i][1]
            diferencia = abs(suma_acumulada - mitad_ideal)

            if diferencia < menor_diferencia:
                menor_diferencia = diferencia
                mejor_k = i
        
        carta_corte = cartas[mejor_k][0]
        print(f"Pregunta óptima: ¿La carta es menor o igual a {carta_corte}?")
        intentos += 1

        if respuesta == "sí":
            cartas = cartas[:mejor_k + 1]
        else:
            cartas = cartas[mejor_k + 1:]
           

    print(f"La carta es: {cartas[0][0]} y se necesitaron {intentos} preguntas.")
    return intentos

"""
Complejidad del algoritmo:

- Complejidad temporal: O(n^2). En cada iteración se recorre la lista de cartas para calcular el mejor corte, y el tamaño de la lista disminuye en cada paso. En el peor caso, la suma de operaciones es n + (n-1) + ... + 1 = O(n^2).

- Complejidad espacial: O(n). Solo se almacena la lista de cartas y algunas variables auxiliares.
"""



"""
El Criterio Greedy (Estrategia)
"En cada paso, elegir la pregunta que divida el mazo actual en dos subconjuntos cuya suma de frecuencias (pesos) sea lo más cercana posible al 50% del total restante."

"""
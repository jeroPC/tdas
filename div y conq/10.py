"""Todos los años la asociación de un importante deporte individual profesional realiza
una preclasificación de los n jugadores que terminaron en las mejores posiciones del ranking
para un evento exclusivo. En la tarjeta de invitación adjuntan el número de posición en la
que está actualmente y a cuantos rivales invitados superó en el ranking comparado el año
pasado. Contamos con un listado que tiene el nombre del jugador y la posición del ranking
del año pasado ordenado por el ranking actual. Ejemplo: LISTA: A,3 | B,4 | C,2 | D,8 | E,6 |
F,5. Se puede ver que el jugador “A” superó al jugador “C”. El jugador “B” superó al jugador
“C”. El jugador “C” no superó a ninguno de los invitados. Etc. Proponer una solución
utilizando la metodología de división y conquista."""

n jugadores mejores posiciones del ranking 

A supero a c, porque esta primero y paso antes estbaba 3, b supero a c, que esta segundo y antes
estaba 4 , c estaba segudno y ahora 3, perdio , D estaba 8 y ahora 4to 


def recusivo(lista_jugadores,rivales_superados):
    total = len(lista_jugadores)

    if total == 1:
        return lista_jugadores[0]
    
    mitad = total // 2
    izq = lista_jugadores[:mitad]
    der = lista_jugadores[mitad:]

    RECURSIVO_izq = recusivo(izq)
    RECURSIVO_der = recusivo(der)

    mezcla = mezcla(RECURSIVO_izq, RECURSIVO_der,rivales_superados)
    return mezcla
def mezcla(lista_izq, lista_der, rivales_superados):
    resultado = []
    i = 0   # <-- SE CREA Y ARRANCAN EN 0 CADA VEZ QUE SE LLAMA A mezcla()
    j = 0   # <-- SE CREA Y ARRANCAN EN 0 CADA VEZ QUE SE LLAMA A mezcla()

    # 1. Mientras queden elementos en AMBAS listas:
    while i < len(lista_izq) and j < len(lista_der):
        if lista_izq[i][1] <= lista_der[j][1]:
            resultado.append(lista_izq[i])
            nombre_jugador = lista_izq[i][0]
            rivales_superados[nombre_jugador] += j
            i += 1
        else:
            resultado.append(lista_der[j])
            j += 1

    # 2. Si sobraron elementos en la izquierda:
    while i < len(lista_izq):
        resultado.append(lista_izq[i])
        nombre_jugador = lista_izq[i][0]
        rivales_superados[nombre_jugador] += j
        i += 1

    # 3. Si sobraron elementos en la derecha:
    while j < len(lista_der):
        resultado.append(lista_der[j])
        j += 1

    return resultado
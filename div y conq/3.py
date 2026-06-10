"""3. Se realiza un torneo con n jugadores en el cual cada jugador juega con todos los otros
n-1. El resultado del partido solo permite la victoria o la derrota. Se cuenta con los resultados
almacenados en una matriz. Queremos ordenar los jugadores como P1, P2, …, Pn tal que P1 le
gana a P2, P2 le gana a P3, …, Pn-1 le gana a Pn (La relación “le gana a” no es transitiva). Ejemplo:
P1 le gana a P3, P2 le gana a P1 y P3 le gana a P2. Solución: [P1, P3, P2]. Resolver por división y
conquista con una complejidad no mayor a O(n log n)."""

n jugadores --> juegan contra n -1 (todos los que no son el )
victoria o derrota ( 0 o 1 )
resultados en una matriz

objetivo : ordenar a los jugadores por p1 p2 ... /

p1 gana a p3 
p2 gana p1 
p3 gana a p2 , por lo tanto el mejor es p1  luego p3 luego p2 

     P1   P2   P3
P1 [ [-]  [0]  [1] ]  <- P1 le gana a P3 (1) y pierde con P2 (0)
P2 [ [1]  [-]  [0] ]  <- P2 le gana a P1 (1) y pierde con p3 (0)
P3 [ [0]  [1]  [-] ]  <- P3 le gana a P2 (1) y pierde con P1 (0)


def encontrar_ganador(jugadores,matriz):
    if len(jugadores) <= 1 : return jugadores 

    mitad = len(jugadores) // 2
    izq = jugadores[:mitad]
    der = jugadores[mitad:]

    izq_ord = encontrar_ganador(izq, matriz)
    der_ord = encontrar_ganador(der,matriz)

    resultado = mezclar(izq_ord,der_ord)

    return resultado

def mezclar(izq_ord, der_ord, matriz):
    i, j =0 
    resultado =[]

    while i < izq_ord && j < der_ord: 
        #matriz[i][j] el jugador i le gano al jugador j

        if matriz[izq[i]][der[j]] == 1:
            resultado.append(izq[i])
            i++
        else:
            resultado.append(der[j])
            j++
    
    resultado.extend(izq[i:])
    resultado.extend([der[j:]])
    return resultado
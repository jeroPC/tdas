"""1. El ajedrez se juega con un tablero cuadriculado. La pieza llamada “Rey” puede moverse en
cualquiera de los 8 cuadrados aledañas a su posición actual comiendo cualquier otra pieza
que esté en ellos. Contamos con un tablero especial de nxm cuadrados y una cantidad
ilimitada de piezas “Rey”. Queremos ubicar la mayor cantidad de reyes sin que estos se
puedan comer entre si. Proponer un algoritmo greedy para resolverlo. Brindar complejidad.
Justificar la optimalidad de su propuesta.
"""

total_reyes = n/2 * m/2 
def solucion_optima(tablero,k):
    resultado = [][]
    for fila in range(0, n, 2):
        for columna in rang(0, m, 2):
            resultado.agregar_matriz[fila][columna]
    
    return resultado

 
complejidad final o(n * m )
primer bucle se ejecuta n/2 veces , lo mimos que el interno m/2

a eleccion greedy , es tomar valores imares, partiendo del cero, porque como un rey toma solo cualquier posiciomn en cualquier direccion , con colocar uno en la esquina 0 0 y los sigueintes saltando 1 lugar y frenando en el siguente del que salte, esta es la eleccion mas rentable
Dividimos el tablero de n x m en bloques independientes de 2 x 2.Como cada bloque puede contener como máximo 1 rey, 
ninguna estrategia en el mundo podrá superar esa cota.Nuestro algoritmo Greedy
 coloca exactamente 1 rey en cada uno de esos bloques (y maneja los bordes impares de la misma forma óptima).
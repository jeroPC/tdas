"""Un centro de distribución de repuestos ferroviarios se encuentra en un punto de la red
de este transporte. Es la encargada de distribuir a demanda los materiales y recursos para
las reparaciones que solicitan las diferentes estaciones. Como la red es antigua y está mal
mantenida la cantidad de kilos que se puede transferir sobre cada trayecto es variable. Esto
para ellos es un problema porque quieren enviar la mayor cantidad posible de material por
viaje. Tanto es así que no les importa realizar un camino más largo siempre que eso implique
transportar más materiales. Se pueden armar diferentes caminos que unan el centro de
distribución con cada estación. Estos estarán conformados por una secuencia de trayectos,
cada uno con su propia limitación de kilos que soporta. Llamamos cuello de botella al valor
mínimo entre ellos. Construir un algoritmo greedy que permita calcular el camino con el
máximo cuello de botella entre el punto de partida y el resto de los puntos."""

def max_cuello_botella(grafo, origen):
    cuellos = {origen: float('inf')}
    
    heap = MaxHeap()
    heap.encolar(origen, cuellos[origen])
    
    while not hip.esta_vacia():
        u, capacidad_actual = hip.desencolar()
        
        if capacidad_actual < cuellos.get(u, 0):
            continue
            
        for vecino, peso_arista in grafo[u].items():
            camino_posible = min(capacidad_actual, peso_arista)
            
            if camino_posible > cuellos.get(vecino, 0):
                cuellos[vecino] = camino_posible
                heap.encolar(vecino, camino_posible)
                
    return cuellos

    complejidad o(e log v)

    
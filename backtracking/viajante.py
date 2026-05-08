
mejor_costo = [float('inf')]
mejor_ruta = []
#grafo = lista de adyacencia con costos, por ejemplo:
grafo = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def tsp_backtrack(nodo_actual, visitados, ruta, costo_actual, grafo, nodo_origen):
    
    # Condición de solución: visité todos y puedo volver
    if len(visitados) == len(grafo):
        if nodo_origen in grafo[nodo_actual]:  # Verifico que pueda volver al origen
            costo_total = costo_actual + grafo[nodo_actual][nodo_origen]
            if costo_total < mejor_costo[0]:
                mejor_costo[0] = costo_total
        return

    # Condición de corte (poda): ya supero el mejor conocido
    if costo_actual >= mejor_costo[0]:
        return

    for vecino in range(len(grafo)):
        if vecino not in visitados:
            visitados.add(vecino)
            tsp_backtrack(vecino, visitados, ruta + [vecino],
                          costo_actual + grafo[nodo_actual][vecino],
                          grafo, nodo_origen)
            visitados.remove(vecino)  # ← backtrack real

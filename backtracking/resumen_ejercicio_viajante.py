"""
Resumen teórico y ejemplo del problema del viajante (TSP) con backtracking

1) Enunciado clásico:
Dado un conjunto de ciudades y las distancias entre cada par de ellas, encontrar el camino de costo mínimo que pase exactamente una vez por cada ciudad y regrese a la ciudad de origen.

2) Representación del grafo:
- Puede ser una matriz de costos (grafo denso)
- O una lista de adyacencia con pesos (grafo disperso)

3) Lógica del algoritmo (backtracking):
- Se exploran todas las rutas posibles que visitan todos los nodos y vuelven al origen.
- Se guarda el menor costo encontrado.
- Se usa poda: si el costo parcial ya supera el mejor conocido, se corta esa rama.

4) Ejemplo de matriz de costos:

grafo = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

5) Código explicado paso a paso:
"""

mejor_costo = [float('inf')]  # Guarda el menor costo encontrado
# mejor_ruta = []  # Si quieres guardar la ruta, descomenta

def tsp_backtrack(nodo_actual, visitados, costo_actual, grafo, nodo_origen):
    """
    nodo_actual: ciudad donde estoy parado
    visitados: conjunto de ciudades ya visitadas
    costo_actual: suma de los costos hasta ahora
    grafo: matriz de costos
    nodo_origen: ciudad de inicio (para cerrar el ciclo)
    """
    # Condición de solución: visité todos y puedo volver
    if len(visitados) == len(grafo):
        # En matriz siempre existe el camino de vuelta
        costo_total = costo_actual + grafo[nodo_actual][nodo_origen]
        if costo_total < mejor_costo[0]:
            mejor_costo[0] = costo_total
            # mejor_ruta[:] = list(visitados) + [nodo_origen]  # Si quieres guardar la ruta
        return

    # Poda: si el costo parcial ya supera el mejor conocido
    if costo_actual >= mejor_costo[0]:
        return

    for vecino in range(len(grafo)):
        if vecino not in visitados:
            visitados.add(vecino)
            tsp_backtrack(vecino, visitados, costo_actual + grafo[nodo_actual][vecino], grafo, nodo_origen)
            visitados.remove(vecino)  # ← backtrack real

# Ejemplo de uso:
if __name__ == "__main__":
    grafo = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    mejor_costo = [float('inf')]
    visitados = set([0])
    nodo_origen = 0
    tsp_backtrack(0, visitados, 0, grafo, nodo_origen)
    print(f"Costo mínimo: {mejor_costo[0]}")
    # print(f"Ruta: {mejor_ruta}")

"""
Consejos para aplicar backtracking en otros problemas:
- Identifica el estado: ¿qué información necesitas para saber dónde estás en la búsqueda?
- Define la condición de solución: ¿cuándo encontraste una solución válida?
- Implementa la poda: ¿cuándo puedes dejar de explorar una rama?
- Haz el backtracking real: marca el estado antes de la llamada recursiva y desmárcalo después.
- Actualiza la mejor solución cuando encuentres una mejor.
"""

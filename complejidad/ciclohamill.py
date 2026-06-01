def reducir_a_ciclo_hamiltoniano(grafo_camino):
    # Creamos un grafo nuevo copiando el original
    grafo_ciclo = copiar(grafo_camino)
    
    # Truco conceptual: Agregamos un nodo extra ficticio 'X'
    grafo_ciclo.agregar_nodo("X")
    
    # Conectamos 'X' a absolutamente todos los nodos del grafo original
    # Esto permite que 'X' funcione como el eslabón de cierre entre el final y el inicio
    for nodo in grafo_camino.vertices:
        grafo_ciclo.agregar_arista("X", nodo)
        
    return grafo_ciclo
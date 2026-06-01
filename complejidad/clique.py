def reducir_a_clique(grafo_CI, k_CI):
    # Creamos un grafo que tiene los mismos nodos
    grafo_clique = crear_grafo_vacio(nodos = grafo_CI.vertices)
    
    # Damos vuelta las aristas (Grafo Complementario)
    # Si NO había arista en CI, significa que en Clique SÍ va arista
    for u in grafo_CI.vertices:
        for v in grafo_CI.vertices:
            if u != v and not grafo_CI.existe_arista(u, v):
                grafo_clique.agregar_arista(u, v)
                
    # El K que buscamos es exactamente el mismo
    k_clique = k_CI
    return grafo_clique, k_clique
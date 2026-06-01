def reducir_a_conjunto_independiente(grafo_clique, k_clique):
    grafo_CI = crear_grafo_vacio(nodos = grafo_clique.vertices)
    
    # Invertimos la lógica de conectividad
    for u in grafo_clique.vertices:
        for v in grafo_clique.vertices:
            if u != v and not grafo_clique.existe_arista(u, v):
                grafo_CI.agregar_arista(u, v)
                
    k_CI = k_clique
    return grafo_CI, k_CI
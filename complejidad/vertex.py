def reducir_a_vertex_cover(grafo_CI, k_CI):
    # El grafo se mantiene EXACTAMENTE IGUAL
    grafo_VC = copiar(grafo_CI)
    
    # Si querías un CI de tamaño 'k', el Vertex Cover que queda 
    # afuera tiene que tener tamaño: N - k
    total_nodos = len(grafo_CI.vertices)
    k_VC = total_nodos - k_CI
    
    return grafo_VC, k_VC
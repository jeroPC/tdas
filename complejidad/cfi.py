def reducir_independent_set_a_CFI(grafo_IS, k_IS):
    # Creamos un grafo nuevo que empieza con los mismos vértices que el de IS
    grafo_CFI = crear_grafo_vacio(nodos = grafo_IS.vertices)
    
    contador_nodos_ficticios = 0
    
    # Por cada arista original (u, v), rompemos la conexión directa 
    # y metemos un nodo "puente" en el medio
    for (u, v) in grafo_IS.aristas:
        # Creamos un nombre único para el nodo intermedio
        nodo_puente = f"ficticio_{contador_nodos_ficticios}"
        contador_nodos_ficticios += 1
        
        # Agregamos el nodo puente al nuevo grafo
        grafo_CFI.agregar_nodo(nodo_puente)
        
        # Conectamos 'u' con el puente, y el puente con 'v'
        grafo_CFI.agregar_arista(u, nodo_puente)
        grafo_CFI.agregar_arista(nodo_puente, v)
        
    # El tamaño del conjunto que buscamos (k) se mantiene exactamente igual
    k_CFI = k_IS
    
    return grafo_CFI, k_CFI
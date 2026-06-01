def reducir_a_camino_hamiltoniano(grafo_ciclo):
    grafo_camino = copiar(grafo_ciclo)
    
    # Elegimos un nodo cualquiera del ciclo, por ejemplo 'v'
    # Lo duplicamos en un nodo 'v_inicio' y 'v_fin'
    grafo_camino.eliminar_nodo('v')
    grafo_camino.agregar_nodo('v_inicio')
    grafo_camino.agregar_nodo('v_fin')
    
    # Todos los que eran vecinos entrantes a 'v' ahora se conectan a 'v_fin'
    # Todos los vecinos salientes de 'v' ahora salen de 'v_inicio'
    for vecino in grafo_ciclo.vecinos('v'):
        grafo_camino.agregar_arista('v_inicio', vecino)
        grafo_camino.agregar_arista(vecino, 'v_fin')
        
    return grafo_camino
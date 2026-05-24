certificador_VertexCover(grafo, evidencia_nodos, k):
    if evidencia_nodos.length > k:
        return "Usa más de k nodos"
        
    for arista in grafo.E:
        nodo_origen = arista.origen
        nodo_destino = arista.destino
        # La arista debe estar cubierta por alguno de sus dos extremos
        if (nodo_origen not in evidencia_nodos) and (nodo_destino not in evidencia_nodos):
            return "Arista no cubierta" # [18]
            
    return "Cobertura válida"

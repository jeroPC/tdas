Pseudocódigo del Certificador (Conjunto Independiente): Se busca validar si existe un conjunto de tamaño k
.
certificador_CI(grafo, evidencia_conjunto_nodos, k):
    if evidencia_conjunto_nodos.length < k: 
        return "No cumple el tamaño mínimo"
    
    for nodo in evidencia_conjunto_nodos:
        if nodo not in grafo.V: 
            return "Nodo inválido"
            
    # Verificar que no existan aristas entre ningún par del conjunto
    for u in evidencia_conjunto_nodos:
        for v in evidencia_conjunto_nodos:
            if u != v and existe_arista(grafo, u, v):
                return "Conflicto: Hay una arista entre ellos" # [11]
                
    return "Es un conjunto independiente válido"

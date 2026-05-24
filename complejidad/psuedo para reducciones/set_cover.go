certificador_SetCover(universo, subconjuntos_evidencia, k):
    if subconjuntos_evidencia.length > k:
        return "Se superó el límite k de subconjuntos" # [26, 27]
        
    elementos_cubiertos = set()
    
    for subconjunto in subconjuntos_evidencia:
        for elemento in subconjunto:
            elementos_cubiertos.add(elemento)
            
    if elementos_cubiertos != universo:
        return "El universo no fue cubierto en su totalidad"
        
    return "Cobertura completa válida"
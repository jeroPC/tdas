"""Greedy: Se planeó un nuevo sendero en una montaña. Para ser habilitado requiere la construcción de refugios con guardaparques distribuidos sobre el mismo. Existen "$n$" proyectos. Cada proyecto propone construir un refugio en cierta ubicación sobre el sendero. Cada refugio "$r_i$" cubre una cantidad de kilómetros $ka_i$ antes de donde está ubicado y $kd_i$ después de donde está ubicado. Nos solicitan determinar la menor cantidad posible de refugios a seleccionar para cubrir todo el camino. Proponga un algoritmo greedy eficiente que lo resuelva."""

def seleccionar_refugios(proyectos, longitud_total):
    proyectos_ordenados = ordenar_por_inicio(proyectos)
    
    refugios_seleccionados = []
    actual = 0  
    i = 0
    n = len(proyectos_ordenados)
    
    while actual < longitud_total:
        mejor_fin = -1
        mejor_proyecto = None
        
        while i < n and proyectos_ordenados[i].inicio <= actual:
            if proyectos_ordenados[i].fin > mejor_fin:
                mejor_fin = proyectos_ordenados[i].fin
                mejor_proyecto = proyectos_ordenados[i]
            i += 1
        
        if mejor_fin <= actual:
            return None  
        
        refugios_seleccionados.append(mejor_proyecto)
        actual = mejor_fin
        
    return refugios_seleccionados
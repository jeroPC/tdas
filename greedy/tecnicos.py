def seleccionar_subconjunto_tecnicos(tecnicos):
    tecnicos_ordenados = ordenar_por_fin(tecnicos)
    
    seleccionados = []
    ultimo_fin_elegido = -1 
    
    for t in tecnicos_ordenados:
        if t.inicio > ultimo_fin_elegido:
            seleccionados.append(t)
            ultimo_fin_elegido = t.fin
            
    return seleccionados
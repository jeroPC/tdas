certificador_BinPacking(elementos, contenedores_evidencia, capacidad_M, k):
    if contenedores_evidencia.length > k:
        return "Se usan demasiados contenedores"
        
    elementos_guardados = []
    
    for contenedor in contenedores_evidencia:
        suma_pesos = 0
        for item in contenedor:
            suma_pesos += item.peso
            elementos_guardados.add(item)
        if suma_pesos > capacidad_M:
            return "Contenedor excedió su capacidad"
            
    if elementos_guardados.length != elementos.length:
        return "Faltaron elementos por guardar"
        
    return "Empaquetamiento válido"
def previo_compatible(cuadras):
    n = len(cuadras)
    # compatible[i] nos va a dar el índice (1-indexed) del último compatible
    compatible = [0] * (n + 1)
    j = 1
    
    # cuadras viene indexado de 0 a n-1
    for i in range(1, n + 1):
        # Mientras j sea menor que i y falten 3 o más cuadras de distancia
        while j < i and cuadras[i - 1]['nro'] - cuadras[j - 1]['nro'] >= 3:
            j += 1
        
        # Guardamos j - 1 (en base 1)
        compatible[i] = j - 1
        
    return compatible

def maxima_ganancia(cuadras):
    n = len(cuadras)
    compatible = previo_compatible(cuadras)
    
    # Tabla OPT de tamaño n + 1 (el índice 0 representa el caso base = 0 de ganancia)
    OPT = [0] * (n + 1)
    
    for i in range(1, n + 1):
        opcion_no_ubicar = OPT[i - 1]
        
        # Buscamos cuál es el índice compatible para la cuadra actual
        indice_compatible = compatible[i]
        opcion_ubicar = cuadras[i - 1]['importe'] + OPT[indice_compatible]
        
        OPT[i] = max(opcion_no_ubicar, opcion_ubicar)
        
    return OPT, compatible

def reconstruccion(cuadras, compatible, OPT):
    cuadras_elegidas = []
    i = len(cuadras)
    
    while i > 0:
        if OPT[i] != OPT[i - 1]:
            cuadras_elegidas.append(cuadras[i - 1]['nro'])
            i = compatible[i]  # Saltamos directo al compatible anterior
        else:
            i = i - 1  # Pasamos a la cuadra anterior
            
    cuadras_elegidas.reverse()
    return cuadras_elegidas
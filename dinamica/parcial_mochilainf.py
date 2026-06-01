def max_ganancia_matriz(perfumes, k):
    n = len(perfumes)
    
    # Renombramos la matriz a 'opt'
    Para i desde 0 hasta n:
        OPT[i][0] = 0
    Para w desde 0 hasta k:
        OPT[0][w] = 0

    for i in range(1, n + 1):
        g_i = perfumes[i]['ganancia']
        w_i = perfumes[i]['peso']
        
        for p in range(1, k + 1):
            if w_i > p:
                # CASO NO ENTRA: Copia directo lo que se logró en la fila anterior
                opt[i][p] = opt[i - 1][p]
            else:
                # CASO ENTRA: Elegimos el máximo entre:
                no_usar = opt[i - 1][p]       # Mirar la fila de arriba (perfume anterior)
                usar_uno = g_i + opt[i][p - w_i] # Quedarse en la misma fila (puedo repetir)
                
                opt[i][p] = max(no_usar, usar_uno)
                
    return opt[n][k]





# --- RECONSTRUCCIÓN DEL CAMINO ---
    perfumes_elegidos = []
    i = n  # Empezamos en el último perfume
    p = k  # Empezamos con la capacidad máxima

    # Iteramos hasta que nos quedemos sin capacidad o sin perfumes que evaluar
    while p > 0 and i > 0:
        w_i = perfumes[i]['peso']
        
        # Si el valor actual es igual al de la fila de arriba, no compramos este perfume
        if opt[i][p] == opt[i - 1][p]:
            i -= 1  # Pasamos al perfume anterior
        else:
            # Si es distinto, significa que compramos el perfume i
            perfumes_elegidos.append(perfumes[i])
            p -= w_i  # Reducimos la capacidad del bolso
            # OJO: NO restamos 'i' porque podemos volver a elegir el mismo perfume
            
    return opt[n][k], perfumes_elegidos
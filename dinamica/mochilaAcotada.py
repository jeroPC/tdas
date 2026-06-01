def mochila_acotada(perfumes, k):
    # perfumes: lista de dicts [{"ganancia": g, "peso": w, "cantidad": c}] (1 a n)
    n = len(perfumes)
    
    opt = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        g_i = perfumes[i]['ganancia']
        w_i = perfumes[i]['peso']
        c_i = perfumes[i]['cantidad']  # Límite de stock para este perfume
        
        for p in range(1, k + 1):
            mejor_opcion = opt[i - 1][p]
            
            for cant in range(1, c_i + 1):
                if cant * w_i <= p:
                    # Ganancia de las 'cant' unidades + óptimo de los anteriores con el peso restante
                    opcion = (cant * g_i) + opt[i - 1][p - (cant * w_i)]
                    if opcion > mejor_opcion:
                        mejor_opcion = opcion
                else:
                    break  # Si con 'cant' ya nos pasamos de peso, no hace falta seguir probando más unidades
            
            opt[i][p] = mejor_opcion
            
    return opt[n][k]
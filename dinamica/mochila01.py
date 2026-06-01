def mochila_01(perfumes, k):
    # perfumes: lista de dicts [{"ganancia": g, "peso": w}] (indexada de 1 a n)
    n = len(perfumes)
    
    # Matriz opt de (n + 1) x (k + 1)
    opt = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        g_i = perfumes[i]['ganancia']
        w_i = perfumes[i]['peso']
        
        for p in range(1, k + 1):
            if w_i > p:
                opt[i][p] = opt[i - 1][p]
            else:
                no_usar = opt[i - 1][p]
                # OJO: Acá usamos opt[i - 1][p - w_i] (fila i-1, porque no se puede repetir)
                usar_uno = g_i + opt[i - 1][p - w_i]
                
                opt[i][p] = max(no_usar, usar_uno)
                
    return opt[n][k]
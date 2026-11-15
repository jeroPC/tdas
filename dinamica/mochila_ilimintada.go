Programación dinámica: Juan desea comprar perfumes para revender entre sus conocidos. 
Puede llevar "k" kilos antes de superar el límite de su bolso. 
Por cada uno de los "n" perfumes que le interesan conoce el PRECIO  DE COMPRA y el de REVENTA.
 Todos los perfumes cuentan con un peso unitario y stock ilimitado. Ayudar a Juan a maximizar 
 la ganancia a obtener. Solucione el problema utilizando programación dinámica.

RECURRENCIA = opt(i,p) = max { opt(i -1 , p ) , vi + opt( i, p - ci)}
ci es el peso de cada objeto 


ganancia NETA = PRECIO DE VENTA - COMPRA 

Gi = PVi - Ci
func mochila_ilimitada(k, n, pesos, compras, reventas):
    # 1. Creamos la matriz de (n + 1) filas x (k + 1) columnas inicializada en 0
    # Fila 0 y Columna 0 ya quedan en 0 como casos base
    opt = matriz de (n + 1) x (k + 1) inicializada en 0

    # 2. Llenamos la matriz iterando por perfume (i) y capacidad (p)
    para i desde 1 hasta n:
        ganancia = reventas[i] - compras[i]
        
        para p desde 1 hasta k:
            no_lo_llevo = opt[i - 1][p]
            
            si pesos[i] <= p y ganancia > 0:
                lo_llevo = ganancia + opt[i][p - pesos[i]]
                opt[i][p] = max(no_lo_llevo, lo_llevo)
            sino:
                opt[i][p] = no_lo_llevo

    # 3. Reconstrucción de la solución desde la esquina inferior derecha
    perfumes_elegidos = []
    i = n
    p = k
    
    mientras i > 0 y p > 0:
        si opt[i][p] == opt[i - 1][p]:
            # El óptimo venía de arriba: no usamos el perfume i
            i = i - 1
        sino:
            # El valor cambió respecto a arriba: sí llevamos el perfume i
            perfumes_elegidos.agregar(i)
            p = p - pesos[i]    # Restamos su peso y seguimos en la misma fila i

    retornar opt[n][k], perfumes_elegidos
"""
Luego de aprender programación dinámica un estudiante en una charla de café le
explica a un amigo que atiende un negocio el algoritmo de cambio mínimo de monedas. Con
eso, afirma, podrá optimizar el despacho de mercadería. El comerciante despacha pedidos
de cierto producto que viene en empaques prearmados de distintas cantidades o sueltos en
unidades. Sin embargo, el amigo le replica que su algoritmo es poco realista. Supone que
uno tiene una cantidad ilimitada de empaques de cada presentación. Luego de pensar unos
momentos, el estudiante llega a una variante de este problema teniendo en cuenta esta
restricción. ¿Podría usted detallar cuál es esta solución?

"""

#pedidos cierto productos vienen con distintas cantidades o sueltos en unidades

#solucion programacion dinamica bidireccional

#i: Los tipos de empaques disponibles (por ejemplo, considerar solo los primeros $i$ tipos de empaque).
#j: La cantidad exacta de unidades que queremos despachar en este momento.

#empaques = [1, 5, 10]
#stock = [2, 1, 1]
# opt (i,j ) = min ( opt (i -1 , j), min { opt(j -k * ci )  + k }  

# Convención: empaques y stock están 1-indexados (de 1 a n).
# opt es una matriz de (n + 1) filas por (X + 1) columnas.

def optimizar_despacho(X, empaques, stock):
    n = len(empaques)
    opt = [[inf] * (X + 1) for _ in range(n + 1)]

    # Caso base: despachar 0 unidades requiere 0 empaques
    for i in range(n + 1):
        opt[i][0] = 0

    for i in range(1, n + 1):
        capacidad = empaques[i]
        limite_stock = stock[i]

        for j in range(1, X + 1):
            # 1. Caso base de la celda (k = 0): no uso este tipo de empaque
            opt[i][j] = opt[i - 1][j]

            # 2. Caso k >= 1: pruebo usar 1, 2, ... hasta limite_stock empaques
            for k in range(1, limite_stock + 1):
                if j - k * capacidad >= 0:
                    opt[i][j] = min(opt[i-1][j], opt[i - 1][j - k * capacidad] + k)
                else:
                    break

    return opt[n][X]
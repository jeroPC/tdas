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
# opt (i,j ) = min { opt (i -1 , j -k * ci ) + k }  


def optimizar_despacho(X, empaques, stock):

    n = len(empaques)
    infinito =  inf 

    opt = [[infinito ] * n + 1]

# Caso base: Para despachar 0 unidades con cualquier cantidad de empaques,
    # se necesitan 0 cajas.
    for i in range(n + 1):
        opt[i][0] = 0

    for i in range (1, n+1 ):
        capacidad = empaques[i - 1]
        limite_stock = stock[i - 1]
        for j in range(0, X + 1):
            
            # El bucle del stock: probamos usar 'k' cajas de este tipo
            for k in range(limite_stock + 1):
                # Si poner 'k' cajas no supera el pedido actual 'j'
                if j - k * capacidad >= 0:
                    
                    # Nos fijamos si el estado anterior (sin estas 'k' cajas) era alcanzable
                    if dp[i - 1][j - k * capacidad] != INFINITO:
                        # Evaluamos si es mejor quedarnos con lo que ya teníamos 
                        # o usar las 'k' cajas nuevas más lo que costaba el resto del pedido
                        dp[i][j] = min(dp[i][j], dp[i - 1][j - k * capacidad] + k)
                else:
                    # Si ya nos pasamos de 'j', no tiene sentido seguir probando con más cajas 'k'
                    break
                    
    # El resultado final estará en la última celda de la matriz
    resultado = dp[n][X]
    
    # Si el valor sigue siendo INFINITO, significa que con el stock actual
    # es imposible armar el pedido exacto.
    if resultado == INFINITO:
        return "Imposible despachar esa cantidad con el stock disponible."
    
    return f"Cantidad mínima de empaques necesarios: {resultado}"

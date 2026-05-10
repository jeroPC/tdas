def cuello_de_botella(flujo, camino, capacidad):
    return min(capacidad[(u,v)] - flujo[(u,v)] para cada (u,v) en camino)

def aumentar_flujo(flujo, camino, capacidad):
    b = cuello_de_botella(flujo, camino, capacidad)
    
    para cada arista (u, v) en camino:
        si (u, v) es arista hacia adelante:
            flujo[(u, v)] += b
        sino:                        # arista hacia atrás
            flujo[(v, u)] -= b       # deshacemos flujo del eje original
    
    retornar b                #VA A SER LA SUMA DE FLUJO MAX FINAL        

def flujo_maximo(grafo, capacidad, fuente, sumidero):
    # Inicializar flujo en 0 para toda arista
    flujo[(u, v)] = 0  para toda arista (u,v) en grafo
    
    flujo_total = 0
    
    mientras exista camino P de fuente a sumidero en grafo_residual(grafo, flujo, capacidad):
        flujo_total += aumentar_flujo(flujo, P, capacidad)
    
    retornar flujo_total


def grafo_residual(grafo, flujo, capacidad):
    residual = grafo vacío
    
    para cada arista (u, v) en grafo:
        
        # Arista hacia adelante
        si capacidad[(u,v)] - flujo[(u,v)] > 0:
            agregar (u, v) con peso capacidad[(u,v)] - flujo[(u,v)]
            
            # Arista hacia atrás SOLO si ya mandé flujo por acá
            si flujo[(u,v)] > 0:
                agregar (v, u) con peso flujo[(u,v)]
    
    retornar residual














    

def bottleneck(flujo, path):
    b = infinito
    para cada eje e = (u, v) en path:
        si e va hacia adelante:
            b = min(b, capacidad(e) - flujo(e))
        sino si e va hacia atrás:
            e´ = (v, u)
            b = min(b, flujo(e´))


            
def construir_grafo_residual(grafo, flujo):
    grafo_residual = {}
    para cada arista (u, v) en grafo:
        capacidad = grafo[(u, v)]
        flujo_actual = flujo.get((u, v), 0)
        # Si queda capacidad en la arista original, la agrego al residual
        if capacidad - flujo_actual > 0:
            grafo_residual[(u, v)] = capacidad - flujo_actual
        # Si hay flujo, agrego la arista reversa con esa capacidad
        if flujo_actual > 0:
            grafo_residual[(v, u)] = flujo_actual
    return grafo_residual
    retornar b
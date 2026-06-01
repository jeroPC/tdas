"""
. Se cuenta con una grafo G=(V,E) con capacidad 1 en cada uno de sus ejes. Existen 2 nodos
que tomaremos como “s” fuente y “t” sumidero. Podemos determinar el flujo máximo F entre
s-t. Se pide proponer un algoritmo eficiente que dado un valor “k”, determine la cantidad
mínima de ejes y cuáles de ellos eliminar para que el nuevo flujo máximo sea F-k.
Determinar su complejidad y detallar mediante pseudocódigo y una explicación cómo
funciona

"""

def obtener_corte_minimo(grafo, grafo_residual, s):
    alcanzables = BFS_nodos_alcanzables(grafo_residual, s) # Retorna un conjunto/set
    
    aristas_corte = []
    
    for u in grafo.nodos():
        for v in grafo.adyacentes(u):
            if u in alcanzables and v not in alcanzables:
                aristas_corte.append((u, v))
                
    return aristas_corte



def actualizar_grafo_residual(grafo_residual, u, v, valor):

    peso_anterior = grafo_residual.peso(u, v)
    
    if peso_anterior == valor:
        grafo_residual.remover_arista(u, v)
    else:
        grafo_residual.cambiar_peso(u, v, peso_anterior - valor)
        
    if not grafo_residual.hay_arista(v, u):
        grafo_residual.agregar_arista(v, u, valor)
    else:
        grafo_residual.cambiar_peso(v, u, grafo_residual.peso(v, u) + valor)


def flujo_edmonds_karp(grafo, s, t):

    flujo = {}
    
    for v in grafo:
        for w in grafo.adyacentes(v):
            flujo[(v, w)] = 0
            
    grafo_residual = copiar(grafo)
    
    while (hay un camino desde s a t ):
        
        capacidad_residual_camino = min_peso(grafo_residual, camino)
        
        for i in range(1, len(camino)):
            u = camino[i-1]
            v = camino[i]
            
            if grafo.hay_arista(u, v):
                flujo[(u, v)] += capacidad_residual_camino
            else:
                flujo[(v, u)] -= capacidad_residual_camino
            
            actualizar_grafo_residual(grafo_residual, u, v, capacidad_residual_camino)
            
    return flujo


def reducir_flujo_maximo(grafo, s, t, k):
    
    grafo_residual = edmonds_karp_residual(grafo, s, t)
    
    aristas_del_corte = obtener_corte_minimo(grafo, grafo_residual, s)
    
    aristas_a_eliminar = aristas_del_corte[0:k]
    
    return aristas_a_eliminar


"""
complejidad o ( v * | e | )



"""
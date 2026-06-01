"""Te refresco rápido el enunciado: tenemos satélites que comunican una nave espacial con la Tierra. Queremos saber cuántos satélites (como máximo) se pueden romper en el peor de los casos de forma tal que la nave quede incomunicada, y cuáles son."""
def construir_red_flujo(grafo_satelites, nave, tierra):
    red = GrafoDirigido()
    
    red.agregar_vertice(nave)
    red.agregar_vertice(tierra)
    
    for v in grafo_satelites.obtener_vertices():
        if v != nave and v != tierra:
            red.agregar_vertice(f"{v}_in")
            red.agregar_vertice(f"{v}_out")
            red.agregar_arista(f"{v}_in", f"{v}_out", 1)
            
    for u in grafo_satelites.obtener_vertices():
        for v in grafo_satelites.adyacentes(u):
            
            if u == nave:
                red.agregar_arista(nave, f"{v}_in", float('inf'))
                
            elif v == tierra:
                red.agregar_arista(f"{u}_out", tierra, float('inf'))
                
            else:
                red.agregar_arista(f"{u}_out", f"{v}_in", float('inf'))
                
    return red



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


def flujo_ford_fulkerson(grafo, s, t):
    
    flujo = {}
    
    for v in grafo:
        for w in grafo.adyacentes(v):
            flujo[(v, w)] = 0
            
    grafo_residual = copiar(grafo)
    
    while (camino = obtener_camino(grafo_residual, s, t)) is not None:
        
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


def corte_minimo(grafo, flujo, capacidad, s):
    residual = grafo_residual(grafo, flujo, capacidad)
    
    alcanzables = BFS(residual, s)
    
    zonas_debiles = []
    para cada arista (u, v) en grafo original:
        si u está en alcanzables Y v NO está en alcanzables:
            zonas_debiles.agregar((u, v))   
    
    retornar zonas_debiles


    
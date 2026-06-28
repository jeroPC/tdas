"""La red ARPANET, antecesora de internet, se creó para seguir funcionando incluso ante
fallas en parte de su red. El país “Atrasoñia” - que se mantuvo cerrado a los avances
tecnológicos de las últimas décadas - ha decidido construir su propia red de redes. Han leído
la documentación desclasificada de ARPANET y se han instruido en conectividad de redes.
Proponen una red informática para unir sus principales organismos estatales. Nos convocan
para que validemos su diseño. Debemos responder: ¿Cuántos cables de datos de la red se
tienen que romper antes que la conectividad del grafo se rompa? (tener en cuenta que los
cables de datos son bidireccionales) ¿Cuántos nodos se tienen que romper antes que el
grafo restante deje de ser conexo? (Sugerencia: piense en transformar de alguna forma los
nodos para resolverlo mediante lo creado en el punto a)"""



def actualizar_grafo_residual(grafo_residual, u, v, botella):
    peso_ant = grafo_residual.peso(u, v)
    if peso_ant == botella:
        grafo_residual.remover_arista(u, v)
    else:
        grafo_residual.cambiar_peso(u, v, peso_ant - botella)
    
    if not grafo_residual.hay_arista(v, u):
        grafo_residual.agregar_arista(v, u, botella)
    else:
        peso_retorno_ant = grafo_residual.peso(v, u)
        grafo_residual.cambiar_peso(v, u, peso_retorno_ant + botella)

def ford_fulkerson(grafo, s, t):
    flujo = {}
    flujo_total = 0  

    for v in grafo:
        for w in grafo.ady(v):
            flujo[(v, w)] = 0

    grafo_residual = copiar(grafo)

    while (camino := buscar_camino_bfs(grafo_residual, s, t)): 
        botella = min_peso(grafo_residual, camino)
        flujo_total += botella  

        for i in range(1, len(camino)):
            u = camino[i - 1]
            v = camino[i]

            if grafo.hay_arista(u, v):
                flujo[(u, v)] += botella
            else:
                flujo[(v, u)] -= botella
            
            actualizar_grafo_residual(grafo_residual, u, v, botella)
            
    return flujo_total, flujo, grafo_residual


def corte_minimo(grafo, flujo, capacidad, s):
    residual = grafo_residual(grafo, flujo, capacidad)
    
    # BFS para ver qué nodos siguen siendo alcanzables desde fuente
    alcanzables = BFS(residual, s)
    
    zonas_debiles = []
    para cada arista (u, v) en grafo original:
        si u está en alcanzables Y v NO está en alcanzables:
            zonas_debiles.agregar((u, v))  
    retornar zonas_debiles

def mapear_grafo_para_cables(grafo_original):
    grafo_aux = Grafo(dirigido=True)
    
    for v in grafo_original:
        grafo_aux.agregar_vertice(v)

    for u in grafo_original:
        for v in grafo_original.ady(u):
            if not grafo_aux.hay_arista(u, v):
                grafo_aux.agregar_arista(u, v, peso=1)
            if not grafo_aux.hay_arista(v, u):
                grafo_aux.agregar_arista(v, u, peso=1)
                
    return grafo_aux



def resolver_punto_a(grafo_original):
    # Paso 1: Llamamos a tu función auxiliar para que arme el grafo
    grafo_flujo = mapear_grafo_para_cables(grafo_original)
    
    # Paso 2: Buscamos la conectividad global usando tus algoritmos
    vertices = list(grafo_original.obtener_vertices())
    s = vertices[0]  # Fijamos el primer nodo como ancla
    
    min_cables = float('inf')
    mejor_corte_aristas = []

    for t in vertices[1:]:
        flujo_total, flujo, grafo_residual = ford_fulkerson(grafo_flujo, s, t)
        
        if flujo_total < min_cables:
            min_cables = flujo_total

            mejor_corte_aristas = corte_minimo(grafo_flujo, flujo, s) 

    return min_cables, mejor_corte_aristas


Adentro del bucle (Ford-Fulkerson o Edmonds-Karp): * Si uso Edmonds-Karp (que es Ford-Fulkerson implementado con BFS para buscar el camino más corto, asegurando que termine rápido), la complejidad de una sola corrida es O(V * E^2)
complejidad final o (v^2 * e^2)
"""Una compañía minera nos pide que la ayudemos a analizar su nueva explotación. Ha
realizado el estudio de suelos de diferentes vetas y porciones del subsuelo. Con estos datos
se ha construido una regionalización del mismo. Cada región cuenta con un costo de
procesamiento y una ganancia por extracción de metales preciosos. (En algunos casos el
costo supera al beneficio). Al ser un procesamiento en profundidad ciertas regiones
requieren previamente procesar otras para acceder a ellas. La compañía nos solicita que le
ayudemos a maximizar su ganancia, determinando cuales son las regiones que tiene que
trabajar. Tener en cuenta que el costo y ganancia de cada región es un valor entero. Para
cada región sabemos cuales son aquellas regiones que le preceden. Resolver el problema
planteado utilizando una aproximación mediante flujo de redes."""

modelado del grafo

SUPER fuente S, super sumidero T

s ----> regiones con ganancia neta positiva (valor arista: ganancia neta)

region b ---> a OSEA a depende de b , valor arista : inf

region neta negativa ---> T le asingo la perdida


def corte_minimo(grafo, flujo, capacidad, s):
    residual = grafo_residual(grafo, flujo, capacidad)
    
    # BFS para ver qué nodos siguen siendo alcanzables desde fuente
    alcanzables = BFS(residual, s)
    
    zonas_debiles = []
    para cada arista (u, v) en grafo original:
        si u está en alcanzables Y v NO está en alcanzables:
            zonas_debiles.agregar((u, v))  
    retornar zonas_debiles


def actualizar_grafo_residual(grafo_residual, u, v, botella):
    # Arista hacia adelante (u -> v): pierde capacidad
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


    from copy import deepcopy

def resolver_explotacion_minera(regiones, dependencias):
    """
    regiones: Diccionario {nombre_region: (ganancia, costo)}
    dependencias: Diccionario {nombre_region: [regiones_que_le_preceden]}
    """
    grafo = GrafoDirigido()
    s = 'S'
    t = 'T'
    
    grafo.agregar_vertice(s)
    grafo.agregar_vertice(t)
    
    for region, (ganancia, costo) in regiones.items():
        grafo.agregar_vertice(region)
        valor_neto = ganancia - costo
        
        if valor_neto > 0:
            grafo.agregar_arista(s, region, valor_neto)
        elif valor_neto < 0:
            grafo.agregar_arista(region, t, abs(valor_neto))
            
    # 3. Agregar las restricciones de dependencia con capacidad infinita
    for region, precedentes in dependencias.items():
        for prec in precedentes:
            # Si elijo 'region', estoy obligado a procesar 'prec'
            grafo.agregar_arista(region, prec, float('inf'))
            
    # 4. Ejecutar Ford-Fulkerson / Edmonds-Karp
    flujo_total, flujo, grafo_residual = ford_fulkerson(grafo, s, t)
    
    # 5. Encontrar las regiones óptimas mediante el Corte Mínimo
    # Buscamos los nodos alcanzables desde S en el grafo residual
    alcanzables = buscar_camino_bfs_conjunto(grafo_residual, s)
    
    # Filtramos para devolver solo las regiones reales (eliminando la fuente 'S')
    regiones_a_trabajar = [nodo for nodo in alcanzables if nodo != s]
    
    return regiones_a_trabajar

def buscar_camino_bfs_conjunto(grafo_residual, s):
    # Un BFS estándar que devuelve el conjunto de todos los nodos visitados
    visitados = set([s])
    cola = [s]
    
    while cola:
        u = cola.pop(0)
        for v in grafo_residual.ady(u):
            if v not in visitados:
                visitados.add(v)
                cola.append(v)
    return visitados
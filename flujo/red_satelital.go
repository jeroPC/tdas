Redes de Flujo: Una red de satélites se construyó para permitir la 
comunicación entre una nave espacial y la tierra. Ciertos satélites pueden 
intercambiar mensajes entre otros. Algunos con la tierra y otros con la nave
 espacial. Contamos con la red y nos piden que midamos su robustez: cuántos 
 satélites en el peor de los casos se 
pueden romper que dejan incomunicada la nave con la tierra? ¿Cuáles?


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


	def modelar_red_satelites(grafo_original, nave, tierra):
    grafo_desdoblado = CrearGrafoDirigido()
    
    # 1. Agregar la Nave y la Tierra al nuevo grafo
    grafo_desdoblado.agregar_vertice(nave)
    grafo_desdoblado.agregar_vertice(tierra)
    
    # 2. Desdoblar los satélites intermedios
    para cada vertice v en grafo_original:
        si v != nave Y v != tierra:
            v_in = (v, "in")
            v_out = (v, "out")
            
            grafo_desdoblado.agregar_vertice(v_in)
            grafo_desdoblado.agregar_vertice(v_out)
            
            grafo_desdoblado.agregar_arista(v_in, v_out, 1)
            
    # 3. Mapear las conexiones originales al nuevo grafo
    para cada arista (u, w) en grafo_original:
        si u == nave:
            origen = nave
        sino:
            origen = (u, "out") 
            
        si w == tierra:
            destino = tierra
        sino:
            destino = (w, "in")
            
        grafo_desdoblado.agregar_arista(origen, destino, INFINITO)
        
    retornar grafo_desdoblado



	def resolver_robustez_satelites(grafo_original, nave, tierra):
    grafo_desdoblado = modelar_red_satelites(grafo_original, nave, tierra)
    
    flujo_final = flujo_ford_fulkerson(grafo_desdoblado, nave, tierra)
    
    flujo_maximo = 0
    para cada vecino en grafo_desdoblado.adyacentes(nave):
        flujo_maximo += flujo_final[(nave, vecino)]
        
    aristas_cortadas = corte_minimo(grafo_desdoblado, flujo_final, nave)
    
    satelites_rotos = []
    para cada (u, v) en aristas_cortadas:
        si es_tupla(u) Y u[1] == "in" Y v[1] == "out":
            satelites_rotos.agregar(u[0]) # u[0] es el nombre original del satélite
            
    retornar flujo_maximo, satelites_rotos
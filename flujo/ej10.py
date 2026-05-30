""". Una red de espías se encuentran diseminados por todo el país. Cada uno de ellos
únicamente conoce a un número limitado de sus pares con los que pude tener contacto
dejando un mensaje escrito en una ubicación conocida. Este conocimiento no es recíproco.
En caso de una crisis la agencia puede enviar mensajes utilizando esta red desde su base
principal a un determinado agente especial. Una cuestión importante es que una vez
utilizado un espía para transmitir un mensaje durante el resto de la crisis no se vuelve a
utilizar. La agencia desea conocer, dada su red y un agente de destino de sus mensajes.
¿Cuál es la mínima cantidad de espías que un rival podría neutralizar para reducir en un 30%
la cantidad de mensajes máximos que puede enviar desde la base al agente? Utilizando
redes de flujos dar una solución al problema."""







def actualizar_grafo_residual(grado_residual,u,v , valor):
    peso_ant= grado_residual.peso(u,v)

    if pseo_anterior == valor :
        grafo_residual.remover_arista(u,v)
    else:
        grado_residual.cambiar_peso(u,v,pseo_anterior)
    
    if not grafo_residual.hay_arista(v,u):
        grado_residual.agregar_arista(v,u,valor)
    else:
        grado_residual.cambiar_peso(v,u,grado_residual)


def ford_fulkerson(grafo,s,t):
    flujo={}

    for v in grafo:
        for w in grafo.ady(v):
            flujo[(v,w)] = 0

    grafo_residual = copiar(grafo)

    while camino_valido(s,t): 
        botella = min_peso(grafo_residual, camino)

        for i in range(len(camino)):
            u = camino[i -1]
            v = camino[i]

            if grafo.hay_arista(u,v):
                flujo[(u,v)] += botella
            else:
                flujo[(v,u)] -= botella
            
            actualizar_grafo_residual(grafo_residual,u,v,botella)


def corte_minimo(grafo, matriz_flujo, s):
    residual = generar_grafo_residual(grafo, matriz_flujo)
    
    alcanzables = BFS(residual, s) 
    
    zonas_debiles = []
    
    for u in grafo.obtener_vertices():
        for v in grafo.ady(u):
            if u in alcanzables and v not in alcanzables:
                zonas_debiles.append((u, v)) 
    
    return zonas_debiles



def construir_grafo_red_espias(grafo_espias, agencia_base, espia_destino):
    grafo_flujo = Grafo(dirigido=True)

    S = "AGENCIA_FUENTE"
    T = "AGENTE_DESTINO"

    grafo_flujo.agregar_vertice(S)
    grafo_flujo.agregar_vertice(T)

    for espia in grafo_espias.obtener_vertices():
        if espia == agencia_base or espia == espia_destino:
            continue
            
        u_in = f"{espia}_in"
        u_out = f"{espia}_out"

        grafo_flujo.agregar_vertice(u_in)
        grafo_flujo.agregar_vertice(u_out)
        grafo_flujo.agregar_arista(u_in, u_out, 1)

    for espia_inicial in grafo_espias.ady(agencia_base):
        grafo_flujo.agregar_arista(S, f"{espia_inicial}_in", float('inf'))

    for u in grafo_espias.obtener_vertices():
        if u == agencia_base or u == espia_destino:
            continue
            
        for v in grafo_espias.ady(u):
            if v == espia_destino:
                grafo_flujo.agregar_arista(f"{u}_out", T, float('inf'))
            elif v != agencia_base:
                grafo_flujo.agregar_arista(f"{u}_out", f"{v}_in", float('inf'))

    return grafo_flujo, S, T


import math

def espias_a_neutralizar(grafo_espias, agencia_base, espia_destino):
    # 1. Construimos la red con nodos duplicados y capacidades
    # Cambié el nombre al que definimos arriba
    grafo_flujo, S, T = construir_grafo_red_espias(grafo_espias, agencia_base, espia_destino)
    
    # 2. Corremos Ford-Fulkerson para obtener el diccionario de flujos
    flujo_optimo = ford_fulkerson(grafo_flujo, S, T)
    
    # 3. Calculamos el valor del flujo máximo total sumando lo que sale de S
    flujo_maximo_total = 0
    for w in grafo_flujo.ady(S):
        flujo_maximo_total += flujo_optimo[(S, w)]
        
    # Si no puede llegar ningún mensaje, el rival no necesita neutralizar a nadie
    if flujo_maximo_total == 0:
        return []
        
    # 4. Calculamos cuántos mensajes hay que reducir (30%) con techo entero
    K = math.ceil(flujo_maximo_total * 0.3)
    
    # 5. Buscamos las aristas saturadas del corte mínimo
    zonas_debiles = corte_minimo(grafo_flujo, flujo_optimo, grafo_flujo, S)
    
    # 6. Seleccionamos K espías del corte para neutralizar
    espias_rivales = []
    
    # Nos aseguramos de no pasarnos de la cantidad de zonas débiles disponibles
    limite_neutralizar = min(K, len(zonas_debiles))
    
    for i in range(limite_neutralizar):
        u_in, v_out = zonas_debiles[i]
        nombre_espia = u_in.replace("_in", "")
        espias_rivales.append(nombre_espia)
        
    return espias_rivales

"""
complejidad o(v*e^2 )

espacial = o(v + e   )
"""
package flujo
# ==============================================================================
# FUNCIONES AUXILIARES (Asumidas por el entorno del grafo)
# ==============================================================================
# copiar(grafo): Retorna una copia profunda del grafo original (vértices y aristas).
# obtener_camino(grafo, s, t): Retorna una lista de vértices representando un camino 
#                              desde 's' hasta 't' (se recomienda implementar con BFS). 
#                              Retorna None si no existe camino.
# min_peso(grafo, camino): Retorna el valor mínimo de los pesos de las aristas 
#                          que conforman el camino dado.

# ==============================================================================
# ALGORITMO PRINCIPAL
# ==============================================================================

def actualizar_grafo_residual(grafo_residual, u, v, valor):
    """
    Actualiza las capacidades de las aristas en el grafo residual tras 
    enviar flujo por un camino de aumento.
    
    Parámetros:
    - grafo_residual: La instancia actual del grafo residual.
    - u: Vértice de origen de la arista actual en el camino.
    - v: Vértice de destino de la arista actual en el camino.
    - valor: La capacidad enviada por el camino (cuello de botella).
    """
    peso_anterior = grafo_residual.peso(u, v)
    
    # 1. Restar la capacidad a la arista directa (forward edge)
    if peso_anterior == valor:
        grafo_residual.remover_arista(u, v)
    else:
        grafo_residual.cambiar_peso(u, v, peso_anterior - valor)
        
    # 2. Sumar la capacidad a la arista de retroceso (back edge)
    if not grafo_residual.hay_arista(v, u):
        grafo_residual.agregar_arista(v, u, valor)
    else:
        grafo_residual.cambiar_peso(v, u, grafo_residual.peso(v, u) + valor)


def flujo_ford_fulkerson(grafo, s, t):
    """
    Calcula la red de flujos máximos desde un origen a un destino.
    
    Parámetros:
    - grafo: El grafo dirigido original con las capacidades máximas.
    - s: Vértice fuente (source).
    - t: Vértice sumidero (sink o target).
    
    Retorna:
    - flujo: Un diccionario con las aristas originales como claves y el 
             flujo final asignado como valores.
    """
    flujo = {}
    
    # Inicializamos el flujo de toda arista del grafo original a 0
    for v in grafo:
        for w in grafo.adyacentes(v):
            flujo[(v, w)] = 0
            
    # El grafo residual inicial es exactamente igual al grafo original
    grafo_residual = copiar(grafo)
    
    # Mientras siga existiendo un camino en la red residual desde 's' hasta 't'
    while (camino = obtener_camino(grafo_residual, s, t)) is not None:
        
        # Determinamos el flujo máximo que puede pasar por este camino específico
        capacidad_residual_camino = min_peso(grafo_residual, camino)
        
        # Iteramos sobre cada par de vértices consecutivos del camino
        for i in range(1, len(camino)):
            u = camino[i-1]
            v = camino[i]
            
            # Actualizamos el registro del flujo real
            if grafo.hay_arista(u, v):
                # Si la arista es original, sumamos el flujo
                flujo[(u, v)] += capacidad_residual_camino
            else:
                # Si es una arista de retroceso, estamos cancelando flujo, así que restamos
                flujo[(v, u)] -= capacidad_residual_camino
            
            # Actualizamos las capacidades en nuestro grafo residual
            actualizar_grafo_residual(grafo_residual, u, v, capacidad_residual_camino)
            
    return flujo
"""Contamos con una red de Flujo definida sobre el grafo G=(V,E) y tenemos una
asignación de flujo f(e) sobre G. Nos solicitan elaborar un algoritmo que en base a esta
información nos indique cómo se actualiza el flujo si uno de los ejes tiene un cambio de
capacidad (puede ser positiva o negativa). Debemos evitar volver a ejecutar el algoritmo de
Ford-Fulkerson desde cero. Explicar los diferentes casos que podrían suceder. Utilizar los
conceptos de flujo máximo/corte mínimo en su explicación. Brindar pseudocódigo de su
propuesta y análisis de complejidad."""


nos dan un grafo con flujo en las aristas 



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


# --- FUNCIÓN AUXILIAR: El motor que avanza linealmente ---
def buscar_caminos_residuales(grafo, grafo_residual, flujo, s, t, historial_botellas):
    """
    Esta función NO resetea el flujo a cero. 
    Toma el flujo y el residual tal como están en ese instante en la memoria,
    corre el while y los modifica directamente.
    """
    flujo_acumulado_en_esta_tanda = 0

    while (camino := buscar_camino_bfs(grafo_residual, s, t)): 
        botella = min_peso(grafo_residual, camino)
        flujo_acumulado_en_esta_tanda += botella  
        
        historial_botellas.append(botella)

        for i in range(1, len(camino)):
            u = camino[i - 1]
            v = camino[i]

            if grafo.hay_arista(u, v):
                flujo[(u, v)] += botella
            else:
                flujo[(v, u)] -= botella
            
            actualizar_grafo_residual(grafo_residual, u, v, botella)
            
    return flujo_acumulado_en_esta_tanda

def procesar_cambio(grafo, capacidades, grafo_residual, flujo, flujo_total, s, t, cambio):
    u, v, nueva_cap = cambio
    cap_vieja = capacidades[(u, v)]
    capacidades[(u, v)] = nueva_cap

    # Caso 1: Subió la capacidad -> busco caminos nuevos s -> t
    if nueva_cap > cap_vieja:
        grafo_residual.sumar_peso(u, v, nueva_cap - cap_vieja)
        flujo_total += buscar_caminos_residuales(grafo, grafo_residual, flujo, s, t, limite=float('inf'))

    # Caso 2: Bajó la capacidad, pero sigue entrando el flujo actual -> no hago nada
    elif nueva_cap >= flujo[(u, v)]:
        grafo_residual.cambiar_peso(u, v, nueva_cap - flujo[(u, v)])

    # Caso 3: Bajó por debajo del flujo actual -> rebalsa 'exceso'
    else:
        exceso = flujo[(u, v)] - nueva_cap
        flujo[(u, v)] = nueva_cap
        flujo_total -= exceso
        grafo_residual = reconstruir_residual(grafo, capacidades, flujo)

        # 1) Devuelvo 'exceso' hacia atrás: de u -> s y de t -> v
        buscar_caminos_residuales(grafo, grafo_residual, flujo, u, s, limite=exceso)
        buscar_caminos_residuales(grafo, grafo_residual, flujo, t, v, limite=exceso)

        # 2) Intento redirigir lo perdido por otro camino: de s -> t
        flujo_total += buscar_caminos_residuales(grafo, grafo_residual, flujo, s, t, limite=exceso)

    return flujo_total, grafo_residual
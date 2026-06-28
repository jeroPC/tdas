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


def procesar_red_de_flujo(grafo, s, t, lista_de_cambios):
    flujo = {}
    for v in grafo:
        for w in grafo.ady(v):
            flujo[(v, w)] = 0
            
    grafo_residual = copiar(grafo)
    historial_botellas = []
    flujo_total = 0

    flujo_total += buscar_caminos_residuales(grafo, grafo_residual, flujo, s, t, historial_botellas)

    for (u, v, nueva_capacidad) in lista_de_cambios:
        
        grafo_residual.cambiar_capacidad_o_peso(u, v, nueva_capacidad) 
        
        flujo_total += buscar_caminos_residuales(grafo, grafo_residual, flujo, s, t, historial_botellas)

    return flujo_total, flujo, historial_botellas
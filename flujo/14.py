"""
Un grupo de "n" amigos participan en un torneo de voley. En cada partido se debe
presentar una planilla de "y" jugadores. Se juegan partidos 1 vez por semana, durante un
periodo de 9 meses. Para lograr que juegue la mayoría se propuso que cada amigo no
juegue más de 4 partidos. Esos partidos deben estar lo más separados posible, por lo que no
pueden jugar más de 1 partido por mes. Finalmente se tiene que tener en cuenta que
algunos amigos en ciertas fechas no pueden asistir por cuestiones personales. Proponer un
algoritmo polinomial que utilizando esta información realice la asignación de jugadores por
partido (o que indique que con esas restricciones no es posible realizarlo)


"""

"""
n amigos , y jugadores por equipo , 1 vez por semana juegan durante 9meses 

dato = para que todos jueguen , cada jugador no ouede jugar mas de 4 partidos (no juega mas de un partido por mes)

algunos no puedne asistir por x cuestion 

"""



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



def resolver_torneo_voley(n_amigos, partidos_por_mes, disponibilidades, y):
    """
    n_amigos: Lista de nombres/IDs de los amigos.
    partidos_por_mes: Diccionario { mes_id: [lista_de_partidos] }
    disponibilidades: Diccionario { amigo_id: set(partidos_a_los_que_puede_asistir) }
    y: Cantidad de jugadores requeridos por partido.
    """
    # 1. Construir el grafo inicial
    grafo = Grafo(dirigido=True)
    S = "FUENTE"
    T = "SUMIDERO"
    
    total_partidos = 0
    
    # Capa 1: Fuente -> Amigos (Capacidad 4)
    for amigo in n_amigos:
        grafo.agregar_arista(S, amigo, 4)
        
        # Capa 2: Amigos -> Meses (Capacidad 1)
        for mes in range(1, 10): # 9 meses
            nodo_mes_amigo = f"M_{amigo}_{mes}"
            grafo.agregar_arista(amigo, nodo_mes_amigo, 1)
            
            # Capa 3: Meses -> Partidos (Capacidad 1, si hay disponibilidad)
            partidos_del_mes = partidos_por_mes.get(mes, [])
            for partido in partidos_del_mes:
                if partido in disponibilidades[amigo]:
                    grafo.agregar_arista(nodo_mes_amigo, partido, 1)
                    
    # Capa 4: Partidos -> Sumidero (Capacidad y)
    for mes, partidos in partidos_por_mes.items():
        for partido in partidos:
            total_partidos += 1
            grafo.agregar_arista(partido, T, y)
            
    # 2. Correr tu función de Edmonds-Karp
    flujo_dict = flujo_edmonds_karp(grafo, S, T)
    
    # 3. Calcular el valor del flujo máximo (sumando lo que sale de S)
    flujo_maximo = 0
    for amigo in n_amigos:
        flujo_maximo += flujo_dict.get((S, amigo), 0)
        
    # 4. Verificar la condición de éxito: flujo_max == P * y
    if flujo_maximo != total_partidos * y:
        return "No es posible realizar la asignación con estas restricciones."
        
    # 5. Si es posible, reconstruir las planillas mirando el flujo
    planillas = {} # { partido: [lista_de_amigos] }
    
    for amigo in n_amigos:
        for mes in range(1, 10):
            nodo_mes_amigo = f"M_{amigo}_{mes}"
            # Miramos a qué partidos les llegó flujo desde los meses de este amigo
            for partido in partidos_por_mes.get(mes, []):
                if flujo_dict.get((nodo_mes_amigo, partido), 0) == 1:
                    if partido not in planillas:
                        planillas[partido] = []
                    planillas[partido].append(amigo)
                    
    return planillas



# ==============================================================================
# ANÁLISIS DE COMPLEJIDAD COMPUTACIONAL
# ==============================================================================
#
# Para el análisis, definimos las siguientes variables basadas en el enunciado:
#   - n: Cantidad de amigos en el grupo.
#   - M: Cantidad de meses del torneo (M = 9, una constante fija).
#   - P: Cantidad total de partidos en los 9 meses. 
#        Dado que se juega 1 vez por semana, P ≈ 4 partidos/mes * 9 meses = 36.
#        Por lo tanto, P también opera como una constante pequeña en la práctica.
#   - y: Cantidad de jugadores requeridos por planilla en cada partido.
#
# ------------------------------------------------------------------------------
# 1. COMPLEJIDAD ESPACIAL (MEMORIA)
# ------------------------------------------------------------------------------
# El espacio en memoria está determinado por el tamaño del Grafo construido 
# (Vértices y Aristas) y las estructuras auxiliares del flujo (diccionarios).
#
# • VÉRTICES (V):
#   Los nodos del grafo se dividen en 4 capas + Fuente (S) y Sumidero (T):
#   - Fuente y Sumidero: 2 nodos.
#   - Capa Amigos: n nodos.
#   - Capa Meses por Amigo: 9 * n nodos (M meses para cada uno de los n amigos).
#   - Capa Partidos: P nodos.
#   Total Vértices |V| = 2 + n + 9n + P = 10n + P + 2  ==>  O(n)
#
# • ARISTAS (E):
#   - De Fuente a Amigos: n aristas.
#   - De Amigos a sus Meses: 9 * n aristas.
#   - De Meses a Partidos: En el peor caso (disponibilidad total), cada mes-amigo
#     se conecta a los partidos de ese mes. Si hay ~4 partidos por mes, son 
#     9n * 4 = 36n aristas.
#   - De Partidos a Sumidero: P aristas.
#   Total Aristas |E| = n + 9n + 36n + P = 46n + P  ==>  O(n)
#
# • ESTRUCTURAS AUXILIARES:
#   El diccionario de flujos, el grafo residual y las estructuras del BFS (cola, 
#   visitados, padres) son proporcionales al tamaño de |V| o |E|.
#
# CONCLUSIÓN ESPACIAL: 
# Como tanto |V| como |E| escalan linealmente respecto a la cantidad de amigos:
# Memoria total = O(V + E) = O(n + n) = O(n) -> Complejidad Espacial Lineal.
#
# ------------------------------------------------------------------------------
# 2. COMPLEJIDAD TEMPORAL (TIEMPO DE EJECUCIÓN)
# ------------------------------------------------------------------------------
# El tiempo de ejecución se divide en tres etapas claramente marcadas:
#
# A) CONSTRUCCIÓN DEL GRAFO:
#    Se recorren los amigos y los meses realizando operaciones de inserción en 
#    el grafo que toman O(1) en promedio usando listas de adyacencia/diccionarios.
#    Tiempo de construcción: O(V + E) = O(n).
#
# B) ALGORITMO DE EDMONDS-KARP:
#    Es la parte central del algoritmo. Su cota teórica es O(V * E^2).
#    ¿Por qué se cumple esta cota?
#    - Cada búsqueda de camino de aumento se realiza mediante un BFS, el cual 
#      tarda O(V + E) = O(n).
#    - Teóricamente, el número máximo de caminos de aumento (veces que el BFS 
#      puede encontrar un camino antes de terminar) está acotado por O(V * E).
#    
#    Multiplicando ambos factores: O(V * E) * O(V + E) = O(V * E^2).
#    Sustituyendo nuestro tamaño del grafo en función de 'n':
#    O(V * E^2) = O(n * n^2) = O(n^3)
#
# C) RECONSTRUCCIÓN DE PLANILLAS:
#    Se recorren los amigos, sus meses y los partidos correspondientes para 
#    verificar si la arista retuvo flujo = 1.
#    Tiempo de reconstrucción: O(n * M * (P/M)) = O(n * P) = O(n).
#
# CONCLUSIÓN TEMPORAL:
# El término dominante es el algoritmo de flujo máximo.
# Tiempo total = O(n) + O(n^3) + O(n) = O(n^3) -> Complejidad Temporal Polinomial.
#
# ==============================================================================
# SÍNTESIS FINAL PARA EL EXAMEN:
# El algoritmo propuesto es eficientemente POLINOMIAL con una complejidad 
# temporal de O(n^3) y espacial de O(n), donde 'n' es la cantidad de amigos.
# ==============================================================================
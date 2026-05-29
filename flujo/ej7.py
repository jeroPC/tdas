La policía de la ciudad tiene “n” comisarías dispersas por la ciudad. Para un evento
deportivo internacional deben asignar la custodia de “m” centros de actividades. Una
comisaría y un centro de actividades pueden ser emparejados si y sólo si la distancia entre
ellos no es mayor a un valor d. Contamos con la distancia entre todos los centros y las
comisarías. Una comisaría sólo puede custodiar un centro. El centro puede ser custodiado
por una comisaría. Determinar si es posible la asignación de tal forma que todos los centros
estén custodiados. ¿Cómo modificaría la resolución del problema si en lugar de que cada
centro de actividades i tenga que ser asignado a una sola comisaría, tenga que ser asignado
a mi comisarías? ¿Cómo modificaría la resolución del problema si además hubiera una
restricción entre comisarías que implicaría que una comisaría Ni y una Nj no pudieran ser
asignadas juntas a un centro Mi
? ¿Para qué casos dejaría de ser eficiente la resolución?



parte 1:

def actualizar_grafo_residual(grafo_residual, u, v, valor):
 
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


def verificar_custodia_centros(comisarias, centros, d):
    # 1. Armás el grafo con las capacidades del Caso Base
    grafo = armar_grafo_bipartito(comisarias, centros, d, caso=1)
    s = "Fuente"
    t = "Sumidero"
    
    # 2. Corrés tu función de flujo (con el nombre corregido)
    flujo_resultado = flujo_ford_fulkerson(grafo, s, t) 
    
    # 3. Calculás el valor total del flujo máximo sumando lo que sale de 's'
    flujo_maximo_total = 0
    for vecino in grafo.adyacentes(s):
        flujo_maximo_total += flujo_resultado[(s, vecino)]
        
    # 4. Verificás si pudiste cubrir todos los centros (m)
    if flujo_maximo_total == len(centros):
        return "Es posible realizar la asignación"
    else:
        return "No es posible"



extra

def armar_grafo_bipartito(comisarias, centros, d):
    grafo = Grafo()
    
    # 1. Creamos e interconectamos los nodos Fuente y Sumidero
    grafo.agregar_vertice("Fuente")
    grafo.agregar_vertice("Sumidero")
    
    for c in comisarias:
        grafo.agregar_vertice(c)
        grafo.agregar_arista("Fuente", c, 1) # Capacidad 1 de Fuente a Comisaría
        
    for a in centros:
        grafo.agregar_vertice(a)
        grafo.agregar_arista(a, "Sumidero", 1) # Capacidad 1 de Centro a Sumidero (Caso Base)

    # 2. AQUÍ SE ESPECIFICA LA CONDICIÓN DE DISTANCIA
    for c in comisarias:
        for a in centros:
            # Calculamos la distancia real entre los dos puntos
            if calcular_distancia(c, a) <= d:
                # Si cumple, la arista existe con capacidad 1
                grafo.agregar_arista(c, a, 1)
            # Si no cumple, directamente NO hacemos nada (la arista no existe)
                
    return grafo
"""La red de transporte intergaláctico es una de las maravillas del nuevo imperio terráqueo.
Cada tramo de rutas galácticas tiene una capacidad infinita de transporte entre ciertos
planetas. No obstante, por burocracia - que es algo que no los enorgullece - existen puestos
de control en cada planeta que reduce cuantos naves espaciales pueden pasar por día por
ella. Por una catástrofe en el planeta X, la tierra debe enviar la mayor cantidad posible de
naves de ayuda. Por un arreglo, durante un día los planetas solo procesaran en los puestos
de control aquellas naves enviadas para esta misión. Tenemos que determinar cuál es la
cantidad máxima de naves que podemos enviar desde la tierra hasta el planeta X.
Sugerencia: considerar a este un problema de flujo con capacidad en nodos y no en ejes"""




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


def transformar_grafo_capacidades_en_nodos(grafo_original, capacidades_planetas):
    """
    Transforma un grafo con capacidades en los nodos a uno con capacidades en las aristas.
    
    - grafo_original: El grafo de la red intergaláctica (rutas con cap. infinita).
    - capacidades_planetas: Un diccionario donde la clave es el planeta y el valor 
                            es la capacidad de su puesto de control.
    """
    grafo_transformado = Grafo(dirigido=True) 
    
    for v in grafo_original:
        v_in = f"{v}_in"
        v_out = f"{v}_out"
        
        grafo_transformado.agregar_vertice(v_in)
        grafo_transformado.agregar_vertice(v_out)
        
        capacidad_nodo = capacidades_planetas.get(v, float('inf'))
        grafo_transformado.agregar_arista(v_in, v_out, capacidad_nodo)
        
    for u in grafo_original:
        for v in grafo_original.ady(u):
            u_out = f"{u}_out"
            v_in = f"{v}_in"
            
            grafo_transformado.agregar_arista(u_out, v_in, float('inf'))
            
    return grafo_transformado

def obtener_maximo_naves(grafo_original, capacidades_planetas, origen, destino):

    grafo_transformado = transformar_grafo_capacidades_en_nodos(grafo_original, capacidades_planetas)
    
    s_transformado = f"{origen}_out"
    t_transformado = f"{destino}_in"
    
    flujo_total, flujo, grafo_residual = ford_fulkerson(grafo_transformado, s_transformado, t_transformado)
    
    return flujo_total
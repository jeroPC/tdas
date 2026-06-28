"""Redes de flujo:
Una nueva empresa de transporte de gas se conformó con la unión de "r" empresas.
 Cada una contaba con un centro de procesamiento y un puerto de exportación unidos por
una ramificada red de transporte con tramos direccionados. Al momento de la unificación, 
cada una aportó un diagrama que asignaba a cada tramo un valor de flujo 
correspondiente al transporte máximo de esa red. La nueva empresa desea interconectar
 las redes mediante algunos tramos bidireccionales que unan empalmes
 de redes distintas, manteniendo la identidad de los empalmes y tramos preexistentes,
  de forma tal de aumentar lo máximo posible el flujo total que llega a los puertos de 
  exportación. Cuentan con un conjunto de ofertas de construcción en forma de pares de
   empalmes a unir.

Se solicita: (a) diseñar una herramienta algorítmica eficiente que determine cuánto flujo adicional permite 
transportar la interconexión; y (b) evaluar el siguiente pseudocódigo,
 propuesto para identificar sobre la red integrada los tramos afectados por
 la unificación, indicando si es correcto y proponiendo su integración o
  las correcciones necesarias:

tramosAfectados (redesExistentes, NuevaRedIntegrada)
    Sea tramosAfectados = []
    Por cada red en redesExistentes
        Por cada eje e(x,y) tramo en red
            Si tramo.flujo < NuevaRedIntegrada[tramo].flujo
                Agregar tramo a tramosAfectados
    Retornar tramosAfectados




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
"""




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



def calcular_flujo_adicional(redes_existentes, ofertas_interconexion):
    suma_flujos_iniciales = 0
    # Guardamos los flujos originales de cada tramo para la parte (b)
    flujos_originales = {} 

    # 1. Calculamos el flujo máximo de cada empresa por separado
    for red, centro, puerto in redes_existentes:
        flujo_max, flujo_red, _ = ford_fulkerson(red, centro, puerto)
        suma_flujos_iniciales += flujo_max
        # Guardamos cuánto flujo pasaba por cada tramo originalmente
        for arista, valor in flujo_red.items():
            flujos_originales[arista] = valor

    # 2. Construimos la súper red integrada
    super_grafo = crear_super_grafo(redes_existentes, ofertas_interconexion)
    
    # 3. Corremos Ford-Fulkerson en la súper red (desde S_SUPER hasta T_SUPER)
    flujo_max_total, flujos_finales, _ = ford_fulkerson(super_grafo, "S_SUPER", "T_SUPER")

    # 4. El flujo adicional es la resta
    flujo_adicional = flujo_max_total - suma_flujos_iniciales

    return flujo_adicional, flujos_originales, flujos_finales



complejidad temporal = o (r * v * e^2)
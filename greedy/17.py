""". Una empresa de telecomunicaciones ganó una licitación para construir un conjunto de “r”
líneas de comunicación bidireccional para “n” ciudades. Cada línea de comunicación “l” une
dos ciudades y de generarla le permite obtener una ganancia mensual Gl. Puede elegir
construir cualquier línea a menos que una nueva línea conecte 2 ciudades previamente
conectadas que un camino que pase por 1 o más líneas. Nos solicitan nuestro
asesoramiento para determinar qué líneas construir maximizando la ganancia obtenida."""


r lineas de comunicacion bidireccional para n ciudades

cada linea (L) une dos ciudades y le da una ganancia mensual de Gl


def forma_ciclo_dfs(nodo_actual, padre, visitados, grafo_elegido):
    visitados.add(nodo_actual)

    for vecino in grafo_elegido.adyacentes(nodo_actual):
        if not in visitados:
            if forma_ciclo_dfs(vecino, nodo_actual, visitados, grafo_elegido):
            return True

        elif vecino != padre:
            return True

    return False



def elegir_lineas(rutas_disponibles):
    ordeno de mayor a menor rutas_disponibles, con merge sort

    elegidas = []
    ganancia_total = 0

    for ruta de U -> V en rutas_disponibles:
            if ruta !forma_cliclo:
                eligidas.add(ruta)
                ganancia_total += ruta.ganancia


    return elegidas, ganancia_total


    complejidad o(v * e) ya que recorro el grafo de veces la cantidad de vértices y aplico mi función auxiliar formar ciclo la cual tiene complejidad o(n)
    Si yo me paro un vértice aleatorio la cantidad de vecinos posibles son B -1 y las aristas igual por eso o(v +e ) = o(2n)

    osea o bien(n)
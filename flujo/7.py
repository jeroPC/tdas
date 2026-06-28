"""La policía de la ciudad tiene “n” comisarías dispersas por la ciudad. Para un evento
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
? ¿Para qué casos dejaría de ser eficiente la resolución?"""

n comisarias CO
m centros de act CE

PARA que CE cubierto por CO su distancia <= D 

datos = tenemos la distanicas de todas las comisarias con los centros
un comisaria puede custodiar un solo centro


primer caso, una comisaria por un centro

modelo un grafo G(v,e) /

-tengo una super fuente S
- un nodo por cada COMISARIA COi
- un nodo por cada centro de actividad CEi
-un super sumidero T

conexiones:

- DE S a COi arista que vale 1
- DE COi a CEi arista que vale 1 (SI LA DISTANCIA ES MENOR IGUAL A D)
- DE CEi a T arista que vale 1

def modelado_grafo(n, m , distancias):
    grafo = crear_grafo()

    grafo.agregar_vertice("S")
    grafo.agregar_vertice("T")


    para cada i  de n:
        grafo.agregar_vertice("COi")
        grafo.agregar_arista("S","COi",1)
    

    para cada j de m:
        grafo.agregar_vertice("CEj")
        grafo.agregar_arista("CEj","T",1)


    para cada CO de n:
            para cada CE de m:
                if distancias[CE] <= D:
                    grafo.agregar_arista(CO,CE,1)

    return grafo



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


def main(grafo,m):

    flujo_total, flujo, _ = ford_fulkerson(grafo, "S", "T")

    # Si el flujo es igual a m, se pudieron custodiar todos los centros
    if flujo_total == m:
        return True, flujo 
    else:
        return False, None



Si cambiamos la capacidad de la arista que va desde el Centro de Actividades hacia el Sumidero (T) para que sea igual a la cantidad de comisarías que necesita ese centro, permitimos que le llegue más flujo. Y como bien dijiste, al mantener las aristas intermedias (Comisaría ==> Centro) con capacidad 1, garantizamos que el algoritmo no use la misma comisaría dos veces para el mismo lugar

ultima pregunta es np hard resolverlo, se puede usar backtracking pero la complejidad de dispara
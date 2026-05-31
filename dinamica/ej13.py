"""

3. En un grafo se conoce como conjunto independiente a un subconjunto de vértices del
mismo tal que ninguno sea adyacente a otro. Es decir, es un conjunto X de vértices tal que
para ningún par de ellos existe alguna arista que los conecte. No se conoce un algoritmo
eficiente que resuelva el problema. Sin embargo, para algunos casos especiales de grafos si
es posible. Considerar el siguiente caso: Un grafo es un camino si se pueden escribir sus
nodos como una sucesión V1, V2, ..., Vn donde cada nodo Vi tiene un eje únicamente con Vi-1 y
Vi+1. (Excepto en los extremos donde solo tienen un eje con el siguiente o el anterior).
Considerar que cada nodo tiene un peso entero positivo. Construir un algoritmo utilizando
programación dinámica que encuentre el set independiente de mayor peso

"""


def maximo_set_independiente(grafo):
    set_ind = []
    n = len(grafo)
    if n == 0: return 0
    if n == 1: return grafo[0].valor

    opt = [0] * n
    opt[1] = max(grafo[0].valor, grafo[1].valor)


    for i in range(2,n ):
        vertice_act = grafo[i]
        no_actualizo = opt[i -1]
        actualizo = vertice_act.valor + opt[i -2]

        opt[i] = max(no_actualizo, actualizo)
        
    retunr opt[n -1]
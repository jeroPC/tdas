""". Problema del camino más largo en un grafo general con aristas sin peso: Dados G = (V, E)
un grafo no dirigido y un natural k, determinar si existe un camino simple en G de longitud
>=k. Probar que es un problema NP-completo (Usar el problema del camino hamiltoniano
para probarlo)"""


certificacion :  recibo un grafo , con vertices y aristas, no dirido y un numero natural k

|la len del camino deber ser >= k
|
|tiene que ser un camino simple = camino donde no se repiten vertices 
|
|

verificador 
    mediante un for : 
      Si se repite un nodo : false

      Las arista que forman el camino deben ser cant nodos -1 y verificar que sea igual 
      el numero natural K  :  sino false

      CADA PAR DE NODIS CONSECUTIVOS DEBEN ESTAR CONECTADOS MEDIANTE UNA ARISTA  EN EL GRAFO
      : SINO FALSE


esto tiene una complejiadad como mucho O(v+e )
que es lo que cuesta recorrer un grafo y corroborar estas condiciones

puedo decir que pertenece al grupo np 


def ResolverCaminoHamiltoniano(grafo = g(v,e), caja_negra):
    n = len(grafo)

    k_objetivo = n -1 (aristas, conexiones, caminos)

    resultado = caja_negra(grafo, k_objetivo)
    if resultado :
        print "el camino mas largo existe, y vale {k_objetivo}"
    else:
        print "el camino mas largo no existe



Camino Hamiltoniano busca específicamente un camino de longitud n -1
pero en el Enunciado me piden ayer si hay un camino mayor igual a k Y yo sé que acá es n -1
En camino Hamilton no está incluido o es menor igual a el camino más largo que es el que me están pidiendo resolver en el enunciado
Además como mi caja negra me devuelve True  si existe un camino simple de longitud K que es N -1
por lo que puedo decir que 


camino hamil <= p camino mas largo (enunciado)

por lo tanto pertenece al grupo np-h , como camino hamiltoniano

entonces al pertenecer a np y nph ==> pertenece a np C
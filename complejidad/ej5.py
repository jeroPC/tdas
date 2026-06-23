"""Un almacén registra en una matriz qué productos compra cada uno de sus clientes. Un
conjunto de clientes es diverso si cada uno de ellos compra cosas diferentes (tiene
intersección vacía con lo que compran los demás). Definimos al problema de los clientes
diversos como: Dada una matriz de registro, de tamaño m (clientes) x n (productos), y un
número k<=m, ¿existe un subconjunto de tamaño al menos k de los clientes que sea diverso?
Probar que el problema es NP-completo. Sugerencia: Reducir polinomialmente conjuntos
independientes a clientes diversos"""

matriz = registro compras de clientes (productos)

conjunto clientes diversos si = cada uno compra cosas diferentes interseccion vacia con los demas

problema de los clientes diversos 

matriz de registro , m (clientes ) n (productos)  k <= m (clients)

objetivo = existe un subconjunot de tamanio k de clientes que sea diverso
    1 2 3 
1   x x
2   x
3.      x    ====> el resultado es que el subconjunto tiene un tamanio 2 gracias a 1 y 3 otra opcion 2 y 3

CERTIFICACION: 

RECIBO UNA MATRIZ DE M X N , DONDE M = clientes ,  N = productos y el entero k que es el numero del posible subgrupo valido

Certificado (c): Un subconjunto de clientes elegidos al azar (por ejemplo: c = {1, 3, 7}) tal que el tamaño de c sea exactamente k (o al menos k)

verificador : 
    comprobar si el el certificado C >= k : sino false
    que los clientes vayan del 1 al m

    validar que un cliente no repita con otro el mismo producto
    creo un diccionario que almacene listas
    para cada cliente en el certificado:
        almaceno sus productos
    para cada prodcuto de mi cliente actual de 1 a len(certificado):
        si se repite algun producto : false



complejidad o(n * m ) en el caso mas costoso , es polinomial, por lo que puedo decir que el
problema de los clientes diversos es NP

reduccion :
    quiero demostrar que conjunto ind <= p problema de los clientes diversos


def reduccion_clientes(matriz, k, caja_negra):
    grafo = crear_grafo_vacio()
    m = cantidad_de_filas(matriz)      
    n = cantidad_de_columnas(matriz)

    para i desde 1 hasta m:
        grafo.agregar_vertice(i)

    para j desde 1 hasta n :
        personas_que_compraron = []
        para i desde 1 hasta m:
            if matriz[i][j] == x :
                personas_que_compraron.append(i)

        para cada P1 en personas_que_compraron:
            para p2 en personas_que_compraron:
                si p1 != p2:
                    grafo.agregar_arista(p1, p2)

    resultado = caja_negra(grafo, k)

    return resultado






"""

REDUCCIÓN: Conjunto Independiente (Independent Set) <=_P Clientes Diversos
    
    DEMOSTRACIÓN DE EQUIVALENCIA (SI Y SOLO SI):
    -------------------------------------------
    (=>) Si el grafo tiene un Conjunto Independiente de tamaño >= k, significa 
         que existen k vértices sin aristas entre ellos. En la matriz generada, 
         esos k clientes no tendrán productos compartidos (ya que las aristas 
         son productos), formando un conjunto de clientes diversos válido.
         
    (<=) Si el almacén tiene un subconjunto de clientes diversos de tamaño >= k, 
         ninguno comparte productos. Como los productos representan aristas de 
         conflicto, significa que en el grafo original esos vértices no tienen 
         conexiones entre sí, conformando un Conjunto Independiente válido.
         
    COMPLEJIDAD DE LA REDUCCIÓN:
    ----------------------------
    La construcción de la matriz requiere inicializarla y recorrer las aristas 
    del grafo para marcar las compras, lo cual toma un tiempo O(|V| * |E|). 
    Al ser una complejidad polinomial respecto al tamaño del grafo de entrada, 
    se demuestra que la reducción es válida bajo el modelo de Karp (NP-Hard).
    """

por lo que es npc ,al ser np y nph


notas = 1. El Certificado (c) no sabe si es válido de antemano
En la teoría, el certificado c es simplemente una pista candidata que te tiran (un subconjunto cualquiera de clientes de tamaño $k$). El certificado intenta ser la solución, pero le corresponde al Verificador chequear si realmente cumple las condiciones
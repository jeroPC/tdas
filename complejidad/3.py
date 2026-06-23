"""La siguiente es una versión de Conjunto Independiente. Dado un grafo G= (V, E) y un
entero k, decimos que I ⊆ V es fuertemente independiente si dados dos vértices u y v en I, la
arista (v, u) no pertenece a E y además no hay ningún camino de tamaño 2 (con dos aristas)
de u a v. El problema de Conjuntos Fuertemente Independientes consiste en decidir si G
tiene un conjunto fuertemente independiente de tamaño al menos k. Probar que el
problema de Conjuntos Fuertemente Independientes es NP completo. Utilizar para ello que
Conjuntos Independientes es NP completo."""


certificacion :  tengo un grafo con V = vertices E =aristas k = entero

el enunciado propone la solucion I c V 

verificador : 
    si u, v E I y ademas no hay una arista de v a u : cumple ,sino false

    Para cada par u, v in I, comprobar que no exista un vértice intermedio w tal que (u, w) in E y (w, v) in E

    ademas I que es la solucion debe ser >= K

lo mas costoso aqui es chequear que para cada par , no exista el vertice intermedio, 
la complejidad es recorrer un grafo O(v+ e) , que es polinomial por lo tanto E a NP


REDUCCION : 

    DIGO QUE conjunto  indp <= p conjunto  fuertemente independiente

def conjunto_fuertemente_ind_k(grafo, caja_negra,k):
    grafo_aux = copiar(grafo)

    para cada par de vertice(u,v ) en grafo_aux:
        creo una vertice w entre u y v en grafo_aux
        que la arista de u conecte con w y w con v 
        u---> w---> v

    resultado = caja_negra(grafo_aux , k)

    return resultado

Si la caja negra encuentra ese subgrupo en el grafo modificado, significa que en el grafo original existía el conjunto independiente que buscábamos.

creacion de grafo_aux = o(v + e) , recorrerlo y aplicar una conexion  o(v+e ) y o(1)
si la caja negra te devuelve True para el grafo modificado, significa que encontró un conjunto I fuertemente independiente de tamaño k
Como los nodos nuevos w que agregamos están a distancia 1 de los vértices originales, es imposible que la caja negra elija a dos nodos vecinos w o a un nodo original junto con su nuevo vecino w. La restricción de distancia >= 3
 del problema fuerte obliga a la caja negra a ignorar esos nodos intermedios y seleccionar únicamente los vértices del grafo original


 Si el grafo original tiene un conjunto independiente de tamaño k, el grafo modificado tendrá un conjunto fuertemente independiente de tamaño k 
 .Si el grafo modificado tiene un conjunto fuertemente independiente de tamaño k, este debe estar compuesto 
 solo por vértices originales que forman un conjunto independiente en el grafo inicial.

 📂 Pertenencia a NP: Primero demostramos que el problema está en NP porque tu algoritmo verificador puede chequear un certificado en tiempo polinomial.

🔥 NP-Hard: Al lograr reducir un problema NP-completo conocido (Conjunto Independiente) a nuestro problema (Conjunto Fuertemente Independiente), demostramos que el nuestro es al menos tan difícil como cualquier problema en NP. Eso lo convierte en NP-hard.

🏆 NP-Completo: Como el problema es NP y también es NP-hard, queda demostrado por definición que pertenece a la clase de los NP-completos (NPC).
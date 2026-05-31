


"""
certificado : subconjunto de vertices I C V


verificador = una lgortimo que toma un grafo , el enteor k y el certificado I :
    chequea que el tamanio de  I  sea al menos k 
    que para cada par de vertices ( u, v) e I
        no exista la arista (u,v) en E 
        No compartan ningún vecino en común
        
         (ya que si hubiera un vecino W tal que (U,W ) e E Y ( W,V ) e E
          existiría un camino de longitud 2).

usar BFS/DFS o simplemente mirar las listas de adyacencia. Para cada par de vértices en $I$ (que son a lo sumo $|V|^2$ combinaciones)

En el peor de los casos, esto toma tiempo polinomial O(|V|^3) o O(|V| .(|V| + |E|))

CON ESTO DEMOSTRAMOS QUE ES NP 
"""



"""
demostrar que es np h , con reduccion polinomial


conjunto indp <= p conjunto fuertemente independiente 

"""


def reduccion(grafo_original, k):

    nuevo_grafo = Grafo(dirigido=False)

    for vertice in grafo_original.obtener_vertices():
        nuevo_grafo.agregar_vertice(v)

    for u, v in grafo_original.obtener_aristas():
        nodo_intermedio = f"w_{u}_{v}"

        nuevo_grafo.agregar_vertice(nodo_intermedio)

        nuevo_grafo.agregar_arista(u, nodo_intermedio)
        nuevo_grafo.agregar_arista(nodo_intermedio, v)

    nuevo_k = k

    return nuevo_grafo, nuevo_k 
      

def resolver_ci_usando_cfi(grafo_original, k):
    grafo_deformado, nuevo_k = transformar_instancia_ci_a_cfi(grafo_original, k)
    
    # 2. LLAMADO A LA CAJA NEGRA 
    # (Asumimos que existe esta función 'resolver_cfi_exacto')
    resultado = resolver_cfi_exacto(grafo_deformado, nuevo_k)
    
    return resultado


#complejidad o(v + e ) recorrer el grafo original , copiarlo y agregar aristas para vertice intermido para simular un cfi y determinar
#si la caja negra me devuelve si o no , en caos de si , peudo decir que ci <= cfi y demuestor que es np h 

# como tnato en la reduccion como certifacion demostre qu es np h y np , se puede considerar a este problema np-c



""" en el grafo original tengo un grupo de nodos que no se tocan entre sí (ci) Como no hay ninguna arista entre ellos, están "lejos".Cuando aplico el invento de meter un 
nodo intermedio en cada arista del grafo, a los nodos que ya estaban separados no les cambia nada. El camino más corto para ir de uno a otro ahora va a ser de 4 aristas o más, porque tuvimos que estirar 
todo el grafo. Como quedaron re lejos (a distancia 4 o más), 
no tienen aristas directas (distancia 1) y tampoco comparten amigos en común (distancia 2). Por lo tanto, ese mismo grupo de nodos cumple perfectamente la regla del "Conjunto Fuertemente Independiente". 
encotnramos los k nodos en el grafo

2. La "Vuelta": Si el nuevo grafo tiene solución, el original también. Ahora  al revés. Viene la caja negra de cfi y  dice: 
"Encontré k nodos en el grafo modificado que no están ni a distancia 1 ni a distancia 2".Acá hay un truco: la caja negra solo va a elegir nodos originales. 
¿Por qué? Porque si elige un nodo intermedio w, ese nodo está pegado (a distancia 1) de dos nodos originales, bloqueando la chance de elegirlos. Siempre rinde más elegir 
los nodos originales de las puntas.Entonces, si la caja negra eligió k nodos originales y nos asegura que no están a distancia 2, ¿qué significa eso para nuestro grafo 
viejo? Estar a distancia 2 en el grafo nuevo significa que hay un nodo intermedio w entre ellos. Y que haya un nodo w significa que en el grafo original había una arista que los unía.
Como la caja negra nos garantiza que no están a distancia 2, nos está garantizando que en el grafo original no había ninguna arista entre ellos. Por lo tanto, esos mismos knodos eran un Conjunto Independiente en el grafo original.




""""
""". Una agencia de marketing coloca publicidad en la Web. Se han ilusionado con vender
publicidad con la siguiente idea, que llamaremos el problema de la Publicidad Estratégica:
Un sitio Web se puede modelar como un grafo G = (V, E). Las acciones habituales de los
usuarios que visitan un sitio se pueden modelar mediante “t” recorridos posibles P1, P2, ... , Pt
(donde cada Pi es un camino dirigido en G). Dado un número k, se quieren elegir a lo sumo k
vértices en G para poner publicidad, de modo tal que todos los “t” recorridos habituales
pasen por al menos uno de esos vértices. Tenemos que mostrarle a esta empresa que su
idea no es realizable por el momento ya que el problema de la Publicidad Estratégica es
NP-completo. Sugerencia: relacionarlo con cubrimiento de vértices."""


nombre del problema = publicidad estrategica

sitio web modelado como G = (v ,e )
acciones de los usuarios = t recorridos posibles p1,p2 ... pt 

donde cada p es una camino dirigido en G  osea un arista conectada por dos vertices

NUMERO k

objetivo = elegir K vertices en G para publicidad 
de modo tal que todos los recorridos pasen por al menos uno de esos vertices



Para demostrar que el problema de la Publicidad Estratégica pertenece a la clase NP,
 necesitás definir un certificado y un algoritmo verificador que corra en tiempo polinomial.

 1) certificado(C): Un subconjunto de vértices V' incluido V. Es decir, la lista de nodos donde se propone colocar la publicidad.

 2)verificador :  el algoritmo toma el grafo , los caminos p , k Y el subconjunto de vertices(I) y :
    verifica que el grafo sea valido
    que los vertices de v' esten en v (pertenencia)
    que el subconjunto I <= k ( A LO SUMO ) (presupuesto)
Para cada uno de los t caminos habituales (P_1, P_2, ..., P_t), el algoritmo debe recorrer sus nodos y verificar que al menos uno de ellos pertenezca al conjunto de publicidad V'.

comlejidad mas costosa, recorrer un grafo = o(v + e ) , por lo tanto es np 


reduccion:

debo demostra que el objetivo no es poible porque es un problema tan complicado como vertex cover

vertex cover <= problema publicidad

def resolver_vertex_cover(G_vc, k_vc, caja_negra):
    
    G_publicidad = copiar(G_vc)  
    
    Definir Caminos = Lista Vacía
    Para cada arista {u, v} en G_publicidad.aristas:
        Definir nuevo_camino = [u, v]
        Caminos.agregar(nuevo_camino)
        
    Retornar caja_negra(G_publicidad, Caminos, k_vc)


que hace la caja negra ?
    "La caja_negra recibe el G_publicidad, la lista de Caminos y el número k_vc. El algoritmo analiza de forma exacta si existe 
    un subconjunto de vértices de tamaño menor o igual a k que logre interceptar (cubrir) todos los caminos de la lista. 
    Si este subconjunto existe, significa que el problema de la publicidad tiene solución, por lo que la caja negra devuelve TRUE. 
    De lo contrario, devuelve FALSE."


/**
 * =============================================================================
 * DEMOSTRACIÓN DE NP-COMPLETITUD: PROBLEMA DE LA PUBLICIDAD ESTRATÉGICA (PE)
 * =============================================================================
 *
 * Para demostrar que el problema de la Publicidad Estratégica es NP-Completo (NPC),
 * se deben cumplir dos condiciones estrictas:
 * 1) PE ∈ NP  (El problema pertenece a la clase NP)
 * 2) PE ∈ NPH (El problema es al menos tan difícil como cualquier problema en NP)
 *
 * -----------------------------------------------------------------------------
 * 1. PERTENENCIA A NP (Certificado + Verificador Polinomial)
 * -----------------------------------------------------------------------------
 * - Certificado (C): Un subconjunto de vértices V' ⊆ V (la solución candidata).
 * - Algoritmo Verificador:
 * 1. Comprueba formato/pertenencia: Verifica que V' ⊆ V en O(|V|).
 * 2. Comprueba presupuesto: Verifica que |V'| ≤ k en O(1).
 * 3. Comprueba cobertura: Para cada uno de los t caminos P_i, recorre sus 
 * nodos y chequea si al menos uno pertenece a V'. Esto toma O(t * |V|).
 *
 * Como todo el proceso de verificación toma tiempo O(t * |V|), el cual es
 * polinomial respecto al tamaño de la entrada, queda demostrado que PE ∈ NP.
 *
 * -----------------------------------------------------------------------------
 * 2. REDUCCIÓN Y NP-HARDNESS (Vertex Cover ≤_P Publicidad Estratégica)
 * -----------------------------------------------------------------------------
 * Tomamos el problema Vertex Cover (VC), el cual ya está demostrado que es NPC.
 * Reducimos una instancia genérica de VC (G_vc, k_vc) a una instancia de PE en
 * tiempo polinomial mediante la función 'resolver_vertex_cover' implementada arriba.
 *
 * - Complejidad de la reducción: Copiar el grafo y recorrer las aristas para
 * crear la lista de caminos toma un tiempo O(|V| + |E|), que es polinomial.
 *
 * -----------------------------------------------------------------------------
 * 3. DEMOSTRACIÓN DE LA EQUIVALENCIA (Si y solo si)
 * -----------------------------------------------------------------------------
 * Para asegurar que la reducción es correcta, demostramos la equivalencia de
 * las respuestas de la caja negra en ambos sentidos:
 *
 * (=>) Si G_vc tiene un Vertex Cover de tamaño ≤ k:
 * Existe un conjunto de ≤ k vértices que toca todas las aristas de G_vc. 
 * Como cada camino en nuestra instancia de PE representa exactamente una 
 * arista de G_vc, ese mismo conjunto de vértices interceptará todos los 
 * caminos de la lista. Por lo tanto, la caja negra de PE devolverá TRUE.
 *
 * (<=) Si la caja negra de PE devuelve TRUE:
 * Significa que existe un conjunto de ≤ k vértices que intercepta todos 
 * los caminos de la lista. Como cada camino fue construido a partir de una 
 * arista {u, v} de G_vc, para que el camino sea interceptado, el conjunto 
 * debió incluir obligatoriamente al nodo 'u' o al nodo 'v' (o ambos). 
 * Por lo tanto, este mismo conjunto toca todas las aristas en G_vc, 
 * formando un Vertex Cover válido de tamaño ≤ k para el grafo original.
 *
 * =============================================================================
 * CONCLUSIÓN:
 * Dado que Vertex Cover es NP-Completo y pudimos reducirlo a Publicidad 
 * Estratégica en tiempo polinomial (VC ≤_P PE), queda demostrado que el problema 
 * de la Publicidad Estratégica es NP-Hard (PE ∈ NPH).
 *
 * Finalmente, al cumplirse que PE ∈ NP y PE ∈ NPH, queda formalmente demostrado 
 * que el problema de la Publicidad Estratégica es NP-Completo (PE ∈ NPC).
 * =============================================================================
 */
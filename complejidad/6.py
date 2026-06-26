"""'Nos piden que organicemos una jornada de apoyo de estudio para exámenes. Tenemos
que poder dar apoyo a “n” materias y hemos recibido currículos de “m” postulantes para ser
potenciales ayudantes. Cada ayudante puede ayudar en un determinado subconjunto de
materias. Para cada una de las materias hay un subconjunto de postulantes que pueden dar
apoyo en ella. La pregunta es: dado un número k < m, ¿es posible seleccionar a lo sumo “k”
ayudantes de modo tal que siempre haya un ayudante que pueda dar consultas en alguna
de las n materias? Este problema se llama Contratación Eficiente. Probar que “Contratación
Eficiente” es NP-completo. Sugerencia: se puede tratar de usar Cubrimiento de Vértices."""

problema = contratacion eficiente

n materias
m postulantes posibles ayudantes

cada ayudante, ayuda en un determinado subconjunto de materias (cantidad posible)
cada materia tiene un limite (subconjunto) de ayudantes que puede dar apoyo

dado K < m , m ayudantes

pregunta = es posible seleccionar a lo sumo 'k' ayudantes / sieempre haya un ayudante que pueda
dar consultas en alguna de las n materias ? 

certificacion : C es un subconjunto de los m postulantes.

validacion : 
    si no es c <= k :return false
    si los m ayudantes del subgrupo no cubren las n materias : return false ==> creo un conjunto y a medida de que veo que cubren los ayudantes, asocio ayudnte con materia


todo estas validaciones a lo sumo es o(n * m), por recorrer todas la materias y ver si 
tiene algun ayudante asociado a esta materia, en el caso de que un ayudante tenga muchas
debe iterarse mas de una posible materia , perjudicando la complejidad


ayudantes {'juan:[b,v,c,a]'  'messi:[a, r ,t ,c] ...'}

 
al ser polinomial su complejidad, puedo decir que contratacion eficiente pertenece a np 

reduccion:

debo demostrar que el poblema de vertex cover <= p contratacion eficiente

vertex_conver = dado un grafo g(v,e) y un numero k, quiero ver si en un subconjunto de vertices
v' de v de tamanio a lo sumo k / para cada arista (u,v) e E  al menos uno de sus extremos esté en V' es decir, u e V' o v e V'. 

def resolver_contratacion_con_vertex(grafo_vertex k , caja_negra):
    ayudantes_vertices = grafo_vertex.obtener_todos_los_vertices()

    aristas_materias = []
    materias_por_ayudante = crear_diccionario_vacio()


    para cada v en ayudantes_vertices:
        materias_por_ayudante[v] = []

    para cada vertice de grafo_vertex:
        para cada vecino de vertice:
            # Para evitar duplicar la materia (ej: evitar meter "A_B" y luego "B_A")
            # Solo la procesamos en un sentido (por ejemplo, si el id de vertice < vecino)
            si vertice < vecino:
                nombre_materia = "Materia_" + vertice + "_" + vecino

                aristas_materias = aniadir(aristas_materias, nombre_materia)
                materias_por_ayudante[vertice] = aniadir(materias_por_ayudante[vertice], nombre_materia)
                materias_por_ayudante[vecino] = aniadir(materias_por_ayudante[vecino], nombre_materia)

    return caja_negra(aristas_materias,materias_por_ayudante, k)

# =============================================================================
# CONCLUSIÓN Y CIERRE FORMAL DE LA DEMOSTRACIÓN (NP-COMPLETITUD)
# =============================================================================
#
# 1. COMPLEJIDAD DE LA REDUCCIÓN:
#    El algoritmo de transformación recorre cada vértice y sus vecinos, lo que 
#    equivale a transitar las aristas del grafo. Por lo tanto, el tiempo de
#    procesamiento de la reducción es O(V + E). Al ser un orden lineal respecto
#    al tamaño del grafo de entrada, se demuestra que la reducción corre en 
#    TIEMPO POLINOMIAL (<=_P).
#
# 2. PERTENENCIA A NP-HARD:
#    Dado que pudimos reducir un problema NP-Completo conocido y consolidado 
#    como Vertex Cover al problema de Contratación Eficiente en tiempo 
#    polinomial (Vertex Cover <=_P Contratación Eficiente), demostramos que nuestro 
#    problema es, como mínimo, igual de difícil que Vertex Cover. 
#    Por lo tanto, Contratación Eficiente pertenece a la clase NP-HARD.
#
# 3. PERTENENCIA A NP:
#    Al principio del ejercicio se demostró la existencia de un Certificado (el 
#    subconjunto de ayudantes C) y un Verificador Polinomial capaz de chequear 
#    en tiempo O(m * n) que el subgrupo sea válido (que |C| <= k y que cubra las 
#    n materias). Por lo tanto, Contratación Eficiente pertenece a la clase NP.
#
# CONCLUSIÓN FINAL:
#    Al cumplir en simultáneo con ambas condiciones fundamentales de la teoría:
#      a) Contratación Eficiente pertenece a NP
#      b) Contratación Eficiente pertenece a NP-Hard
#
#    Queda formalmente PROBADO que el problema de Contratación Eficiente 
#    es NP-COMPLETO (NPC).
# =============================================================================


""'tips:

Conversación con Gemini
hice la certificacion , algun consejo ?"""'Nos piden que organicemos una jornada de apoyo de estudio para exámenes. Tenemos

que poder dar apoyo a “n” materias y hemos recibido currículos de “m” postulantes para ser

potenciales ayudantes. Cada ayudante puede ayudar en un determinado subconjunto de

materias. Para cada una de las materias hay un subconjunto de postulantes que pueden dar

apoyo en ella. La pregunta es: dado un número k < m, ¿es posible seleccionar a lo sumo “k”

ayudantes de modo tal que siempre haya un ayudante que pueda dar consultas en alguna

de las n materias? Este problema se llama Contratación Eficiente. Probar que “Contratación

Eficiente” es NP-completo. Sugerencia: se puede tratar de usar Cubrimiento de Vértices."""



problema = contratacion eficiente



n materias

m postulantes posibles ayudantes



cada ayudante, ayuda en un determinado subconjunto de materias (cantidad posible)

cada materia tiene un limite (subconjunto) de ayudantes que puede dar apoyo



dado K < m , m ayudantes



pregunta = es posible seleccionar a lo sumo 'k' ayudantes / sieempre haya un ayudante que pueda

dar consultas en alguna de las n materias ?



certificacion : tengo n materias , m ayudastes potenciales , un k < m / todas las materias esten cubiertas por ayudantes



validacion :

si hay muhcas materias (n) , muy pocos ayudantes : false

si una materia no tiene ayudante : false

si ayudantes <= 0 : false



todo estas validaciones a lo sumo es o(n), por recorrer todas la materias y ver si

tienen todas ayudantes


al ser polinomial su complejidad, puedo decir que contratacion eficiente pertenece a np










"""


1. El Certificado (¿Qué te dan?)
Para demostrar que un problema está en NP, vos no intentás resolver el problema desde cero. Imagina que viene alguien y te dice: "Che, encontré la solución, es este grupo de ayudantes".

Ese grupo es tu certificado (o testigo) C.

C es un subconjunto de los m postulantes. """

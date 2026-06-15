"""Nos brindan una caja negra A que, dado un grafo no dirigido G = (V, E) y un número k se
comporta de la siguiente manera:
○ Si G es no conexo devuelve “no conexo”.
○ Si G es conexo y tiene un conjunto independiente de tamaño al menos k devuelve
“Sí”.
○ Si G es conexo y no tiene un conjunto independiente de tamaño al menos k devuelve
“No”.
Mostrar cómo podríamos resolver el problema del máximo conjunto independiente en
tiempo polinomial, usando llamadas a A si suponemos que A corre en tiempo polinomial en
el tamaño de G y k. Describir la solución. ¿Tiene sentido la hipótesis de que A corre en
tiempo polinomial en el tamaño de G y k? ¿Por qué?"""


-----Si G es no conexo devuelve “no conexo”.
-----Si G es conexo y tiene un conjunto independiente de tamaño al menos k devuelve "si"
-----Si G es conexo y no tiene un conjunto independiente de tamaño al menos k devuelve "no"


nos piden , preguntandole a A(caja negra), mostrar como podemos resolver el problema en tiempo 
polinomial

conjunto indp = si para un grafo , con un par de nodos, no tienen una arista que los conecte 


El valor de k en el rango [1, n_i] (donde n_i es la cantidad de vértices de la componente conexa C_i ) representa el tamaño posible 
del conjunto independiente que le vas a consultar a la caja negra 📦 .No es que te "quedás" con k nodos al azar para achicar el grafo.
 Lo que hacés es preguntarle a la caja negra: ¿Existe algún subconjunto de al menos k nodos en esta componente que no estén 
 conectados entre sí por ninguna arista


def buscar_k_MAX(conjunto):
    n = CantidadDeVértices(C)

    Para k_prueba desde n bajando hasta 1:     
       Si CajaNegra(C, k_prueba) == "Sí":
            Devolver k_prueba
    return 0

  

def k_max_max(grafo, caja_negra):
    formo grupos de conjuntos conexos entre si y les asigno un id a cada grupo lo llamo conjuntos_conexos
    ejemplo [c1 ,c2 ...]. #complejidad o(n)
    k_max =0 
    for cada conjunto in len(conjunto_conexos)
        conjuto[k] = buscar_k_MAX(conjunto)
        k_max += conjuto[k]

    return k_max

def reconstruir_conjunto(conjunto, k_max_inicial, caja_negra):
    grafo_resultado = copiar(conjunto)
    resultado = []
    k_target = k_max_inicial

    para cada nodo de obtener_nodos(conjunto):
        si k_target == 0:
            break  
            
        si nodo no está en grafo_resultado:
            continue  

        grafo_aux = quitar_nodo(grafo_resultado, nodo)
        
        k_actual = 0
        nuevas_componentes = obtener_componentes_conexas(grafo_aux)
        para cada sub_c en nuevas_componentes:
            k_actual += buscar_k_MAX(sub_c, caja_negra)

        if k_actual < k_target:
            resultado.add(nodo)
            k_target -= 1  
            
            grafo_resultado = quitar_nodo(grafo_resultado, nodo)
            para cada vecino de obtener_vecinos(nodo, grafo_resultado):
                grafo_resultado = quitar_nodo(grafo_resultado, vecino)
        sino:
            grafo_resultado = quitar_nodo(grafo_resultado, nodo)

    return resultado


    # =====================================================================
# MI RESUMEN DE LA LOGICA DE RECONSTRUCCIÓN (EXPLICACIÓN DE JERÓNIMO)
# =====================================================================

# 1. FUNCIÓN PRINCIPAL Y AUXILIARES:
# Tengo una función auxiliar que me da el máximo K de una componente.
# Y tengo otra función que, dependiendo de la caja negra, me da la 
# sumatoria de todos los conjuntos para reconstruir el resultado final.

# 2. VARIABLES INICIALES EN LA RECONSTRUCCIÓN:
# - 'grafo_resultado': Es la copia del conjunto que voy a ir modificando.
# - 'resultado': Es la lista donde voy a ir acumulando los nodos que 
#   cumplen y forman el conjunto independiente.
# - 'k_target': Es igual al K máximo inicial de la componente. Este valor 
#   va a ir decrementando a medida que encuentro un nodo de la solución óptima.

# 3. CONDICIONES DE CONTROL:
# - Si el 'k_target' llega a cero, ya terminé de buscar en esta componente.
# - Si el nodo actual ya no está en el 'grafo_resultado', significa que 
#   ya lo eliminé antes (porque era vecino de una solución) y lo salteo.

# 4. SIMULACIÓN CON GRAFO AUXILIAR:
# - 'grafo_aux': Quito el nodo actual del 'grafo_resultado' para probarlo.
# - 'k_actual': Es una variable local que empieza en cero y me ayuda a 
#   comparar los elementos actuales.
# - 'nuevas_componentes': Calculo de vuelta las componentes conexas. 
#   Al principio pasé un conjunto conexo, pero ahora, por culpa de quitar 
#   un nodo, el grafo se puede desarmar en varios subconjuntos.
# - Para cada subconjunto, calculo de vuelta su K máximo con la caja negra 
#   y lo sumo a 'k_actual'.

# 5. TOMA DE DECISIÓN (SITUACIÓN OPTIMA):
# - Si el 'k_actual' es menor que el 'k_target' inicial, significa que 
#   este nodo era obligatorio para la solución del conjunto independiente.
# - Entonces:
#   A) Añado este nodo a mi 'resultado'.
#   B) Decremento el 'k_target' (si era 3, ahora pasa a ser 2 porque ya 
#      tengo uno asegurado).
#   C) Quito este nodo de mi 'grafo_resultado'.
#   D) Elimino también a todos sus vecinos de 'grafo_resultado' (porque 
#      si este nodo es solución, sus vecinos no pueden estar).

# 6. CASO NO OBLIGATORIO Y FIN:
# - Si el nodo no disminuyó el target, significa que no influye en nada. 
#   Lo elimino igual de 'grafo_resultado' para avanzar con los siguientes.
# - Finalmente, devuelvo el 'resultado' total acumulado.



como ci es un problema np C , si la caja negra es polinomial, significa, que este problema perteneciente a 
np c , puede resolverse en tiempo polinomial 

Por la definición de completitud, todos los problemas de la clase NP se podrían resolver en tiempo polinomial.

Esto demostraría formalmente que P = NP, resolviendo de golpe el famoso Problema del Milenio.
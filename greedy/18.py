"""Para habilitar la realización de un importante evento multideportivo se solicitó como
precondición que durante el lapso que dura cada actividad exista junto a la misma personal
médico. Conocemos para cada una de las “n” actividades a realizar, el momento de inicio y
final. Como encargados de la inspección nos solicitan que programemos la menor cantidad
de inspecciones posibles en las que constatamos que (al menos al momento de la
inspección) se cumple la precondición. Una inspección verifica únicamente aquellos eventos
que se están llevando a cabo en el momento. Ninguna actividad debe quedar sin
inspeccionar. Presentar una solución greedy óptima al problema."""


n act inicio y fin 
tenemos que verificar que cuando estemos inspeccionando cada act, haya personal medico

inpeccion = eventos que se llevan a cabo en el momento

eleccion greedy = mientras un evento este de inicio y fin determinado coloco por lo menos un 
personal medico , en caso de que no haya un medico , hay un problema

def inspeccionar_actividades(actividades):
    actividades = mergesort(actividades de menor a mayor por tiempo de finalizacion)
    contador = 0
    inspecciones_totales = 0


    while contador < len(actividades):
        act_actual_fin = actividades[contador].fin
        inspecciones_totales += 1
        while contador < len(actividades) and actividades[contador].incio < act_actual_fin:
            contador += 1
    

    return inspecciones_totales


    Estructura O(n) de dos punteros / lectura lineal: El bucle interno continúa desde donde se quedó el anterior porque comparten la misma variable de control (como tu contador).



"""
DEMOSTRACIÓN DE OPTIMALIDAD: ARGUMENTO DE INTERCAMBIO (EXCHANGE ARGUMENT)

Sean:
  - G = {g_1, g_2, ..., g_k} el conjunto de inspecciones ordenadas de Greedy.
  - O = {o_1, o_2, ..., o_m} el conjunto de inspecciones ordenadas de un Óptimo.
Queremos demostrar que k = m (Greedy genera la misma cantidad de elementos).

PASO 1: Hipótesis de la primera diferencia
Supongamos por el absurdo que G no es óptimo. Si comparamos las inspecciones 
cronológicamente de izquierda a derecha, existirá un primer índice 'i' donde 
las decisiones difieren por primera vez, tal que:
g_1 = o_1,  g_2 = o_2,  ...,  g_{i-1} = o_{i-1},  pero  g_i != o_i

PASO 2: Acotación de la elección golosa (Greedy Stays Ahead)
Por definición del algoritmo, 'g_i' se clava exactamente en el tiempo de 
finalización (Fin) de la primera actividad que quedó sin cubrir por 'g_{i-1}'.
Como la solución Óptima 'O' es válida, está obligada a cubrir esa misma actividad. 
Para poder cubrirla, su inspección 'o_i' no puede ser mayor que el tiempo de fin 
de dicha actividad. Por lo tanto, se cumple la cota superior estricta:
o_i <= g_i

PASO 3: Intercambio y Reducción
Dado que o_i <= g_i, la inspección de Greedy está más (o igual) a la derecha en 
la línea de tiempo. Esto implica que cualquier actividad futura que fuera cubierta 
por 'o_i' también será cubierta por 'g_i', o incluso más.
Por lo tanto, podemos reemplazar 'o_i' por 'g_i' en la solución Óptima. La nueva 
solución modificada (O') sigue siendo válida y conserva el mismo tamaño (m).

CONCLUSIÓN:
Repitiendo este proceso de intercambio para cada diferencia, podemos transformar 
la solución Óptima O en la solución Greedy G sin aumentar jamás la cantidad de 
inspecciones. Así, se demuestra que k = m, por lo que Greedy es óptimo.
"""
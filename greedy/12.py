"""Un importante club de campo debe cerrar durante un mes sus instalaciones. En ese
tiempo tiene que licenciar a la mayoría de sus empleados. Entre ellos a los guardias de
seguridad. Cada uno de ellos trabaja 1 vez por mes en un horario de corrido por mes
iniciando un día determinado y finalizando unos días después. Habitualmente varios
guardias se superponen en algunos momentos del mes. Pero sabemos que siempre hay al
menos 1 de ellos en las instalaciones. Los que nos solicitan es que dejemos a la mínima
cantidad de guardias posibles y que aun siempre haya al menos uno custodiando durante el mes.
 Proponga un algoritmo greedy eficiente que lo resuelve."""

cada guardia trabaja 1 vez por mes en un horario de corrido por mes
iniciando un día determinado y finalizando unos días después.


varios se superponen en algunos momentos del mes
pero sabemos que siempre hay 1 en las instalaciones
nos piden dejar la cantidad minima de guardias, siempre y cuando haya uno custodiando


guardias = { a:[1 - 3], b:[2-3], c:[3- 8] , d:[6-8], e:[8-12]}
aca la solucion optima seria a , c, e 


def min_guardias(guardias):
    guardias = mergesort por dia de inicio de menor a mayor
    if len(guardias) <= 0:
        return

        
    resultado=[]
    resultado = [guardias[0]]
    fin_actual = guardias[0].dia_fin
    
    i = 1
    while i < len(guardias):
        max_fin = fin_actual
        mejor_guardia = None

        while i < n and guardias[i].dia_inicio <= max_fin:
            if guardias[i].dia_fin > max_fin:
                max_fin = guardias[i].dia_fin
                mejor_guardia = guardias[i]


            i += 1 

        if not mejor_guardia:
            break

        if mejor_guardia.dia_fin > guardias[0].dia_fin and mejor_guardia.dia_inicio == guardias[0].dia_inicio:
            resultado[0] = mejor_guardia
            fin_actual = mejor_guardia.dia_fin
            
        else:
            resultado.append(mejor_guardia)
            fin_actual = max_fin


    return resultado


    # =============================================================================
# JUSTIFICACIÓN DE LA ESTRATEGIA GREEDY (COBERTURA DE INTERVALOS)
# =============================================================================
# Criterio Greedy: 
# Se ordenan los guardias por día de inicio de menor a mayor. A partir de la 
# frontera actual de cobertura (fin_actual), el algoritmo selecciona de forma 
# avara (greedy) al guardia que se solape con lo ya cubierto (dia_inicio <= fin_actual) 
# y que maximice el día de finalización (dia_fin).
#
# Demostración de Optimalidad (Intuición):
# Al elegir en cada paso al guardia que llega lo más lejos posible en el tiempo, 
# minimizamos la necesidad de meter más guardias en el futuro cercano. Cualquier 
# otra elección dejaría una frontera de cobertura menor o igual, lo que limitaría 
# las opciones de solapamiento para los tramos siguientes. Por lo tanto, esta 
# estrategia estira al máximo cada decisión, garantizando la mínima cantidad total 
# de guardias (solución óptima).
# =============================================================================

# =============================================================================
# ANÁLISIS DE COMPLEJIDAD TEMPORAL: O(N log N)
# =============================================================================
# 1. Ordenamiento previo: 
#    Se utiliza Mergesort para ordenar los N elementos por día de inicio. 
#    Esto toma un tiempo de O(N log N).
#
# 2. Selección Greedy (Bucles While anidados):
#    A pesar de tener un bucle 'while' dentro de otro, ambos comparten exactamente 
#    el mismo contador 'i'. El contador 'i' arranca en 1 y SOLO incrementa (i += 1) 
#    dentro del bucle interno, avanzando siempre hacia adelante.
#    
#    Esto significa que cada guardia se procesa como máximo UNA SÓLA VEZ a lo largo 
#    de toda la ejecución del algoritmo. No hay retrocesos ni comparaciones redundantes.
#    Por análisis amortizado, la complejidad de todo el bloque de selección es 
#    lineal: O(N).
#
# Complejidad Total: O(N log N) + O(N) = O(N log N) -> Altamente eficiente.
# =============================================================================
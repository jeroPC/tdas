"""
Contamos con una impresora central en un centro de cómputos del campus universitario.
Entre varios departamentos y laboratorios nos solicitan al inicio de cada mes, la impresión
de “n” documentos. Cada uno de ellos tiene una duración determinada y cuenta con una
fecha de entrega. Si nos pasamos de esta recibimos un apercibimiento proporcional al
retraso más largo del mes. Como a la impresora le falta mantenimiento queremos lograr -
siempre que sea posible - tiempo entre los trabajos de impresión. Presentar un algoritmo
greedy que dada la lista de tareas proponga la fechas de inicio de publicación minimizando
el apercibimiento y dando tiempo entre las tareas siempre que sea posible
""""

#datos :


"""
inicio cada mes : n documentos para imprimir (dura cierto tiempo la impresion ) (fecha de entrega)

if not cumplimos (fecha de entrega ) : apercibimiento proporcional al retraso mas largo del mes

ojetivo + datos extra : dadas las lista de tareas , minimizae el apercibimeinto , y dando a tiempo las tareas
siempre que sea posible


apercibiemiento es proporcional a lo que tardamos. Lmax= max(0, fi - di ) donde f es el tiempo de finalizacion y di es la fecha de entrega
vamos a tratar de que este retraso sea 0 o lo minimo posible


criterio greedy= ordenar las tareas de menor a mayor por la fecha de entrega

Ordenamiento y Schedule Base: Ordenar por EDD y calcular las fechas asumiendo que se procesan lo antes posible. Esto nos asegura 
conocer cuál es el mínimo retraso máximo L_max alcanzable.Desplazamiento (Slack) hacia atrás: Empezando desde la última tarea programada, 
la empujamos hacia su fecha límite (o lo más tarde posible) para maximizar el tiempo de descanso de la impresora
 antes de que empiece.


'"""



def entregar_impresiones(documentos):
    #ordeno de menor a mayor por fecha de entrega 
    tareas_ordenadas = mergesort(documentos)
    n = len(documentos)

    fechas_inicio = arreglo_vacio(tamaño=n)
    fechas_fin = arreglo_vacio(tamaño=n)


    tiempo_actual = 0
    l_max = 0

    para cada i= 0 hasta n -1 :
        tarea =tareas_ordenada[i]

        fechas_inicio = tiempo_actual
        fechas_fin[i] = tiempo_actual + tarea[i].duracion


        retraso = max(0 , fechas_fin[i] - tarea[i].limite)
        if retraso > l_max:
            l_max = retraso

        tiempo_actual = fechas_fin[i]

    limite_sig_tarea = tarea.limte[n -1 ] + L_max

    para i dede n -1 hasta 0 : 
        tarea =tareas_ordenadas[i]

        maxima_fecha_fin + min(limite_sig_tarea, tarea.limite + L_max)
        fechas_fin[i] = maxima_fecha_fin
        fechas_inicio[i] = maxima_fecha_fin - tarea.duracion
        limite_siguiente_tarea = fechas_inicio[i]



    cronograma_final = []
    para i desde 0 hasta n - 1:
        cronograma_final.append({
            "id": tareas_ordenadas[i].id,
            "fecha_inicio": fechas_inicio[i],
            "fecha_fin": fechas_fin[i]
        })
        
    return cronograma_final




    1. Complejidad Temporal: $O(n \log n)$Como bien dijiste, el "cuello de botella" (lo más costoso) es el ordenamiento inicial.Paso 1 (Ordenar por Deadline): Usando un algoritmo eficiente como Merge Sort o QuickSort (que es lo que usa Python por detrás con Timsort), nos cuesta $O(n \log n)$.Paso 2 (Primer bucle for hacia adelante): Recorremos las $n$ tareas una sola vez para calcular l_max. Esto es lineal: $O(n)$.Paso 3 (Segundo bucle for hacia atrás): Volvemos a recorrer las $n$ tareas de atrás para adelante para acomodar los baches. También es lineal: $O(n)$.Paso 4 (Construir la respuesta): Otro recorrido lineal de $O(n)$.


    2. Complejidad Espacial: $O(n)$En el espacio de memoria también la pegaste de diez.Necesitamos almacenar la lista de tareas_ordenadas (tamaño $n$).Usamos los arreglos fechas_inicio y fechas_fin (tamaño $n$ cada uno).La estructura final que devolvemos tiene tamaño $n$.
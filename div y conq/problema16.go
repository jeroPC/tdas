
//Se cuenta con un vector V de “n” elementos. Este vector visto de forma circular está
//ordenado. Pero no necesariamente en la posición inicial se encuentra el elemento más
//pequeño. Deseamos conocer la cantidad total de rotaciones que presenta “V”. Ejemplo: V =
//[6, 7, 9, 2, 4, 5] se encuentra rotado en 3 posiciones. Podemos hacerlo en tiempo O(n) por
//fuerza bruta. Presentar una solución utilizando división y conquista que mejore esta
//complejidad.



Por qué es como el tuyo: En lugar de una curva en "V", aquí los datos suben, tienen una caída brusca 
(el mínimo) y vuelven a subir. El objetivo es encontrar esa caída. El truco es mirar el elemento del
 medio y compararlo con el inicio o el fin del vector;
 así determinas si la caída ocurrió en la mitad izquierda o en la derecha, descartando el resto.



V = [6, 7, 9, 2, 4, 5]  N ELEMENTOS

FUNC ENCONTRAR_ROTACION(V, inicio, fin):
	 
	if inicio > fin: return -1
	if V[inicio] <= v[fin] return inicio

	mitad  = (inicio + fin) / 2

	if mitad > inicio and V[mitad] < V[mitad - 1]: return mitad
	if mitad < fin and V[mitad] > V[mitad + 1]: return mitad + 1
		
	else if v[mitad]  > v[fin]:
		return ENCONTRAR_ROTACION(V , mitad+1, fin)
	
	else:
		return ENCONTRAR_ROTACION(v,inicio , mitad)
	

def encontrar_rotacion(V):
    inicio = 0
    fin = len(V) - 1

    while inicio < fin:
        mitad = (inicio + fin) // 2

        # Si el elemento del medio es mayor que el del extremo derecho,
        # la caída (el mínimo) está estrictamente en la mitad derecha.
        if V[mitad] > V[fin]:
            inicio = mitad + 1
        else:
            # Si V[mitad] <= V[fin], el mínimo está en la mitad izquierda
            # o es el propio V[mitad].
            fin = mitad

    return inicio


def encontrar_rotacion(V, inicio, fin):
    # Caso base: el rango converge a un único elemento (el mínimo)
    if inicio == fin:
        return inicio

    mitad = (inicio + fin) // 2

    # Si el del medio es mayor que el extremo derecho,
    # la caída está estrictamente a la derecha.
    if V[mitad] > V[fin]:
        return encontrar_rotacion(V, mitad + 1, fin)
    
    # Si no, el mínimo está a la izquierda o es el propio V[mitad].
    return encontrar_rotacion(V, inicio, mitad)


def encontrar_rotacion(V, inicio, fin):
    # Caso 1: el subarreglo ya está ordenado (0 rotaciones en este rango)
    if V[inicio] <= V[fin]:
        return inicio

    mitad = (inicio + fin) // 2

    # Caso 2: ¿el elemento en 'mitad' es justo el punto de caída?
    # Si V[mitad] es menor que su anterior, encontramos el mínimo.
    if mitad > inicio and V[mitad] < V[mitad - 1]:
        return mitad

    # Si el siguiente es menor que mitad, el mínimo es mitad + 1.
    if mitad < fin and V[mitad] > V[mitad + 1]:
        return mitad + 1

    # Caso 3: si no estaba justo en 'mitad', decidimos a qué mitad ir
    if V[mitad] > V[fin]:
        return encontrar_rotacion(V, mitad + 1, fin)     # Caída a la derecha
    else:
        return encontrar_rotacion(V, inicio, mitad - 1)  # Caída a la izquierda
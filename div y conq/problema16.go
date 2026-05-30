
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

	mitad  = (inicio +fin) / 2

	if mitad > inicio and V[mitad] < V[mitad - 1]: return mitad
	if mitad < fin and V[mitad] > V[mitad + 1]: return mitad + 1
		
	if mitad < fin and V[mitad] > V[mitad + 1]:
	return mitad + 1
	
	else if v[mitad]  > v[fin]:
		return ENCONTRAR_ROTACION(V , mitad+1, fin)
	
	else:
		return ENCONTRAR_ROTACION(v,inicio , mitad)
	


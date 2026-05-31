"""
Dado “L” un listado ordenado de “n” elementos y un elemento “e” determinado.
Deseamos conocer la cantidad total de veces que “e” se encuentra en “L”. Podemos hacerlo
en tiempo O(n) por fuerza bruta. Presentar una solución utilizando división y conquista que
mejore esta complejidad.
"""

def buscar_primera_aparicion(L, e, inicio, fin):
    if inicio > fin:
        return -1
    
    medio = (inicio + fin) // 2
    
    if L[medio] == e:
        # Es la primera aparición si está al principio o si el anterior es menor
        if medio == 0 or L[medio - 1] < e:
            return medio
        else:
            # Seguimos buscando en la mitad izquierda
            return buscar_primera_aparicion(L, e, inicio, medio - 1)
            
    elif L[medio] > e:
        # El elemento está a la izquierda
        return buscar_primera_aparicion(L, e, inicio, medio - 1)
    else:
        # El elemento está a la derecha
        return buscar_primera_aparicion(L, e, medio + 1, fin)


def buscar_ultima_aparicion(L, e, inicio, fin):
    if inicio > fin:
        return -1
    
    medio = (inicio + fin) // 2
    
    if L[medio] == e:
        # Es la última aparición si es el último índice o si el siguiente es mayor
        if medio == len(L) - 1 or L[medio + 1] > e:
            return medio
        else:
            # Seguimos buscando en la mitad derecha
            return buscar_ultima_aparicion(L, e, medio + 1, fin)
            
    elif L[medio] > e:
        return buscar_ultima_aparicion(L, e, inicio, medio - 1)
    else:
        return buscar_ultima_aparicion(L, e, medio + 1, fin)


def contar_ocurrencias(L, e):
    n = len(L)
    if n == 0:
        return 0
    
    primera = buscar_primera_aparicion(L, e, 0, n - 1)
    
    # Si primera es -1, el elemento no existe en la lista
    if primera == -1:
        return 0
        
    ultima = buscar_ultima_aparicion(L, e, 0, n - 1)
    
    return (ultima - primera) + 1


# --- Ejemplo de uso ---
if __name__ == "__main__":
    lista = [1, 2, 4, 4, 4, 4, 5, 7, 7, 9]
    elemento_buscado = 4
    
    total = contar_ocurrencias(lista, elemento_buscado)
    print(f"El elemento {elemento_buscado} aparece {total} veces.")
    # Debería imprimir: El elemento 4 aparece 4 veces.
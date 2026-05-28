16. Se conoce como “Longest increasing subsequences” al problema de, dado un vector de
numérico, encontrar la subsecuencia más larga de números (no necesariamente
consecutivos) donde cada elemento sea mayor a los anteriores. Ejemplo: En la lista → 2, 1, 4,
2, 3, 9, 4, 6, 5, 4, 7. Podemos ver que la subsecuencia más larga es de longitud 6 y
corresponde a la siguiente “1, 2, 3, 4, 6, 7”. Resolver el problema mediante programación
dinámica.



ejericico que se resuelve por lista: Busca elementos no necesariamente contiguos que mantengan un orden estricto de crecimiento.

def longitud_LIS(vector):
    if not vector:
        return 0
    
    n = len(vector)
    # Cada elemento por sí mismo es una secuencia de longitud 1
    opt = [1] * n
    
    # Llenamos la tabla DP
    for i in range(1, n):
        for j in range(0, i):
            # Si el elemento actual es mayor y encontramos una secuencia más larga
            if vector[i] > vector[j]:
                DP[i] = max(DP[i], DP[j] + 1)
                
    return max(DP)
Función buscar_elemento(Matriz M, f_inicio, f_fin, c_inicio, c_fin, objetivo):
    Si f_inicio > f_fin O c_inicio > c_fin:
        Retornar NULO

    Si objetivo > M[f_inicio][c_inicio] O objetivo < M[f_fin][c_fin]:
        Retornar NULO

    f_mitad = (f_inicio + f_fin) / 2
    
    c_encontrada = busqueda_binaria_fila(M, f_mitad, c_inicio, c_fin, objetivo)

    Si M[f_mitad][c_encontrada] == objetivo:
        Retornar (f_mitad, c_encontrada)

    res = buscar_elemento(M, f_inicio, f_mitad - 1, c_encontrada, c_fin, objetivo)
    Si res != NULO: 
        Retornar res

    Retornar buscar_elemento(M, f_mitad + 1, f_fin, c_inicio, c_encontrada, objetivo)

---

Función busqueda_binaria_fila(Matriz M, fila, inicio, fin, objetivo):
    Mientras inicio <= fin:
        medio = (inicio + fin) / 2
        Si M[fila][medio] == objetivo:
            Retornar medio
        Si M[fila][medio] > objetivo:
            inicio = medio + 1
        Sino:
            fin = medio - 1
    Retornar inicio
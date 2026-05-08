
#contamos con un grafo g = (v,e) con n vertices  y m ejes , queremos asingarles no mas de k colorees a sus vertices
#cualquier par de vertices ady no pueden compartir el mismo color

def principal(grafo,colores):
    color_asignado = {}
    soluciones = []
    backtracking(grafo, 0, colores, color_asignado, soluciones)
    return soluciones

def es_valido(grafo, color_asignado, vertice, color):
    for vecino in grafo[vertice]:
        if vecino in color_asignado and color_asignado[vecino] == color:
            return False
    return True

def backtracking(grafo, i, colores, color_asignado, soluciones):
    if i == len(grafo):
        soluciones.append((color_asignado))  # copia
        return  True

    for color in colores:
        if es_valido(grafo, color_asignado, i, color):
            color_asignado[i] = color
            backtracking(grafo, i + 1, colores, color_asignado, soluciones)
            del color_asignado[i]  # backtrack real
    return False
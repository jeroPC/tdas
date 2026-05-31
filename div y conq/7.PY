"""
. Para la elaboración de un juego se desea construir un cielo nocturno de una ciudad
donde se vea el contorno de los edificios en el horizonte. Cada edificio “ei“ está representado
por rectángulos mediante la tripla (izquierda, altura, derecha). Dónde “izquierda”
corresponde a la coordenada x menor, “derecha” la coordenada x mayor y altura la
coordenada y. Todos los edificios inician en la coordenada 0 de y. Se cuenta con una lista de
N edificios que llegan sin un criterio de orden específico. Se desea emitir como resultado el
contorno representado como una lista de coordenadas “x” y sus alturas. Tenga en cuenta el
siguiente ejemplo: Lista de edificios: (1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16) , (14, 3, 25),
(19,18,22). Contorno: (1,11),(3,13),(9,0),(12,7),(16,3),(19,18),(22,3),(25,0). Presentar un
algoritmo utilizando división y conquista que dado el listado de edificios retorna como
resultado el contorno de la ciudad.

"""

def obtener_skyline(edificios):
    # CASO BASE: Si no hay edificios
    if not edificios:
        return []
    # CASO BASE: Si hay un solo edificio, su contorno es su techo y luego cae a 0
    if len(edificios) == 1:
        izq, h, der = edificios[0]
        return [[izq, h], [der, 0]]
    
    # DIVISIÓN: Dividimos la lista a la mitad
    medio = len(edificios) // 2
    izq_skyline = obtener_skyline(edificios[:medio])
    der_skyline = obtener_skyline(edificios[medio:])
    
    # COMBINACIÓN: Mezclamos ambos contornos
    return mezclar_skylines(izq_skyline, der_skyline)


def mezclar_skylines(izq, der):
    resultado = []
    # Punteros para recorrer ambos contornos
    i, j = 0, 0
    # Alturas actuales mientras barremos de izquierda a derecha
    h1, h2 = 0, 0
    
    while i < len(izq) and j < len(der):
        # Elegimos la coordenada X más a la izquierda para procesar
        if izq[i][0] < der[j][0]:
            x, h1 = izq[i][0], izq[i][1]  # Avanzamos en el contorno izquierdo
            i += 1
        elif izq[i][0] > der[j][0]:
            x, h2 = der[j][0], der[j][1]  # Avanzamos en el contorno derecho
            j += 1
        else:
            # Si coinciden en X, actualizamos ambas alturas y avanzamos ambos
            x = izq[i][0]
            h1 = izq[i][1]
            h2 = der[j][1]
            i += 1
            j += 1
        
        # La altura real en este punto X será la máxima entre ambos sub-contornos
        h_max = max(h1, h2)
        
        # Para evitar puntos duplicados con la misma altura o en la misma X
        if not resultado or resultado[-1][1] != h_max:
            if resultado and resultado[-1][0] == x:
                resultado[-1][1] = h_max # Actualizamos la altura si es la misma X
            else:
                resultado.append([x, h_max])
                
    # Si quedaron puntos residuales en el contorno izquierdo, los agregamos
    while i < len(izq):
        resultado.append(izq[i])
        i += 1
        
    # Si quedaron puntos residuales en el contorno derecho, los agregamos
    while j < len(der):
        resultado.append(der[j])
        j += 1
        
    return resultado
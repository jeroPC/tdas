""". Esta peculiar empresa se dedica a cubrir patios cuadrados de n*n metros (“n” es un
número entero potencia de 2 y mayor o igual a 2). Cuenta con baldosas especiales que
tienen forma en L (como se muestra en celeste en la
imágen). Las baldosas no se pueden cortar. Todo patio
cuenta con un único sumidero de agua de lluvia. Ocupa
1x1 metro y su ubicación depende del patio (Se muestra en
la figura de ejemplo como un cuadrado negro). Nos piden
que, dado un patio con un valor “n” y una ubicación del
sumidero en una posición x,y desde la punta superior
izquierda, determinemos cómo ubicar las baldosas.
Presentar un algoritmo que lo resuelva utilizando división y
conquista."""


# Variable global para contar las baldosas (geles) colocadas
contador_baldosas = 0

def resolver_patio(matriz, x_inicio, y_inicio, size, x_sumidero, y_sumidero):
    global contador_baldosas
    
    # 🛑 CASO BASE: Si el cuadrante es de 2x2, colocamos la L directamente
    if size == 2:
        contador_baldosas += 1
        # Llenamos los 3 casilleros que NO son el sumidero
        for i in range(x_inicio, x_inicio + 2):
            for j in range(y_inicio, y_inicio + 2):
                if not (i == x_sumidero and j == y_sumidero):
                    matriz[i][j] = contador_baldosas
        return

    #  PASO RECURSIVO: Calcular el centro para dividir en 4
    centro_x = x_inicio + size // 2
    centro_y = y_inicio + size // 2
    
    # Numeramos la L central que unirá los cuadrantes vacíos
    contador_baldosas += 1
    id_l_central = contador_baldosas

    # 1re Cuadrante Superior Izquierdo ↖
    if x_sumidero < centro_x and y_sumidero < centro_y:
        # El sumidero real está aquí
        resolver_patio(matriz, x_inicio, y_inicio, size // 2, x_sumidero, y_sumidero)
    else:
        # No está aquí: ponemos sumidero virtual y llamamos
        matriz[centro_x - 1][centro_y - 1] = id_l_central
        resolver_patio(matriz, x_inicio, y_inicio, size // 2, centro_x - 1, centro_y - 1)

    # 2️⃣ Cuadrante Superior Derecho ↗️
    if x_sumidero < centro_x and y_sumidero >= centro_y:
        resolver_patio(matriz, x_inicio, centro_y, size // 2, x_sumidero, y_sumidero)
    else:
        matriz[centro_x - 1][centro_y] = id_l_central
        resolver_patio(matriz, x_inicio, centro_y, size // 2, centro_x - 1, centro_y)

    # 3️⃣ Cuadrante Inferior Izquierdo ↙️
    if x_sumidero >= centro_x and y_sumidero < centro_y:
        resolver_patio(matriz, centro_x, y_inicio, size // 2, x_sumidero, y_sumidero)
    else:
        matriz[centro_x][centro_y - 1] = id_l_central
        resolver_patio(matriz, centro_x, y_inicio, size // 2, centro_x, centro_y - 1)

    # 4️⃣ Cuadrante Inferior Derecho ↘️
    if x_sumidero >= centro_x and y_sumidero >= centro_y:
        resolver_patio(matriz, centro_x, centro_y, size // 2, x_sumidero, y_sumidero)
    else:
        matriz[centro_x][centro_y] = id_l_central
        resolver_patio(matriz, centro_x, centro_y, size // 2, centro_x, centro_y)

# --- Ejemplo de uso para iniciar el algoritmo ---
# n = 4
# patio = [[0]*n for _ in range(n)]
# patio[2][1] = -1  # Marcamos el sumidero inicial con -1 (el negro de la imagen)
# resolver_patio(patio, 0, 0, n, 2, 1)
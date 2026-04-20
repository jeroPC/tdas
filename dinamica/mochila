Función Mochila_01(n, W, peso, valor):
    // 'n' es la cantidad de objetos
    // 'W' es la capacidad total máxima de la mochila
    // 'peso' es un arreglo con los pesos de los objetos: peso[1] a peso[n]
    // 'valor' es un arreglo con el valor de los objetos: valor[1] a valor[n]
    
    // 1. Creamos la matriz OPT de tamaño (n+1) filas y (W+1) columnas
    OPT = nueva matriz[n + 1][W + 1]
    
    // 2. Llenamos los casos base (la fila 0 y la columna 0 con ceros)
    Para i desde 0 hasta n:
        OPT[i][0] = 0
    Para w desde 0 hasta W:
        OPT[0][w] = 0
        
    // 3. Iteramos sobre los objetos (filas)
    Para i desde 1 hasta n:
        
        // 4. Iteramos sobre cada capacidad posible (columnas)
        Para w desde 1 hasta W:
            
            // Si el objeto actual pesa más que la capacidad 'w', NO entra
            Si peso[i] > w:
                OPT[i][w] = OPT[i-1][w]
                
            // Si el objeto entra, tomamos el máximo entre dejarlo o llevarlo
            Sino:
                valor_lo_dejo = OPT[i-1][w]
                valor_lo_tomo = valor[i] + OPT[i-1][w - peso[i]]
                
                OPT[i][w] = MAX(valor_lo_dejo, valor_lo_tomo)
                
    // 5. El resultado óptimo para todos los objetos y la capacidad total
    // se encuentra en la esquina inferior derecha de la matriz.
    Retornar OPT[n][W]


    Tiempo: $O(n \cdot W)$. Tenemos dos bucles anidados, uno recorre los $n$ objetos y
     el otro recorre hasta la capacidad $W$.Espacio: $O(n \cdot W)$ para almacenar la matriz OPT. 
     (Al igual que otros problemas de DP, esto se puede optimizar a $O(W)$ si solo guardamos la fila actual y la anterior,
     pero la versión 2D es la más clara para entender y la que suelen pedir en los exámenes).
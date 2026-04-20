Función AgruparEnPilas(mazo_de_cartas):
    // Cada elemento de esta lista guardará solamente la carta que está "arriba" de todo en esa pila
    cimas_de_pilas = [] 

    Para cada carta actual en el mazo_de_cartas:
        pila_ideal_index = NULO
        menor_diferencia = INFINITO

        // 1. Comparo la carta en mano contra todas las cimas visibles
        Para cada indice, cima en cimas_de_pilas:
            
            // Condición principal: la cima DEBE ser mayor a la carta que tengo en la mano
            Si cima > carta actual:
                
                // Condición Greedy (Best-Fit): de todas las mayores, quiero la más ajustada
                diferencia = cima - carta actual
                
                Si diferencia < menor_diferencia:
                    menor_diferencia = diferencia
                    pila_ideal_index = indice // Me guardo la posición de esta pila porque es la mejor hasta ahora

        // 2. Terminé de mirar todas las pilas. ¿Qué hago ahora?
        Si pila_ideal_index NO es NULO:
            // Encontré una pila válida. 
            // Apilo mi carta ahí, por lo que mi carta pasa a ser la nueva cima visible de esa pila.
            cimas_de_pilas[pila_ideal_index] = carta actual
        
        Sino:
            // Si es NULO, significa que ninguna cima era mayor a mi carta.
            // No me queda otra que armar una pila nueva.
            Agregar (carta actual) al final de cimas_de_pilas

    // Al final, la cantidad de pilas que tuve que abrir es el tamaño de mi lista
    Retornar longitud(cimas_de_pilas)
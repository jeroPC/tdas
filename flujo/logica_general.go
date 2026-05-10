

		// 1. Arma la red que nos dice por dónde podemos empujar flujo o deshacerlo
Función armar_red_residual(Grafo, Flujo, Capacidad):
    G_f = Crear nuevo grafo con los mismos vértices que Grafo
    
    Para cada arista (u,v) en el Grafo original:
        capacidad_restante = Capacidad(u,v) - Flujo(u,v)
        
        // Arista hacia adelante: cuánto más podemos empujar
        Si capacidad_restante > 0:
            Agregar arista (u,v) a G_f con peso = capacidad_restante
            
        // Arista hacia atrás: cuánto flujo podemos "deshacer"
        Si Flujo(u,v) > 0:
            Agregar arista (v,u) a G_f con peso = Flujo(u,v)
            
    Retornar G_f


// 2. Encuentra el límite de lo que podemos mandar por un camino
Función calcular_cuello_botella(Camino, G_f):
    cuello_botella = INFINITO
    Para cada arista (u,v) en Camino:
        cuello_botella = MIN(cuello_botella, peso de (u,v) en G_f)
    Retornar cuello_botella


// 3. Algoritmo Principal
Función ford_fulkerson(Grafo, s, t, Capacidad):
    // Inicializamos todo el flujo en 0
    Para cada arista (u,v) en Grafo:
        Flujo(u,v) = 0  
        
    flujo_total = 0
    G_f = armar_red_residual(Grafo, Flujo, Capacidad)
    
    // Mientras haya un camino desde el origen (s) al destino (t) en la red residual
    Mientras exista un Camino P de s a t en G_f (buscando con BFS o DFS):
        
        cuello_botella = calcular_cuello_botella(P, G_f)
        
        // Actualizamos el flujo original basándonos en el camino encontrado
        Para cada arista (u,v) en Camino P:
            Si la arista (u,v) existe en el Grafo original:
                // Es una arista hacia adelante, sumamos flujo
                Flujo(u,v) = Flujo(u,v) + cuello_botella
            Sino:
                // Es una arista hacia atrás en G_f, significa que estamos "deshaciendo" flujo
                Flujo(v,u) = Flujo(v,u) - cuello_botella
                
        flujo_total = flujo_total + cuello_botella
        
        // Reconstruimos la red residual con los nuevos valores de flujo
        G_f = armar_red_residual(Grafo, Flujo, Capacidad)
        
    Retornar flujo_total, Flujo
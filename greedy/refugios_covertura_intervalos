// Asumimos que el sendero va desde 'inicio_sendero' hasta 'fin_sendero'
Función MinimosRefugios(proyectos, inicio_sendero, fin_sendero):
    
    intervalos = []
    
    // 1. Convertir los datos a intervalos [inicio, fin]
    Para cada p en proyectos:
        L = p.ubicacion - p.ka
        R = p.ubicacion + p.kd
        Agregar (L, R) a intervalos
        
    // 2. Ordenar por inicio (L) de menor a mayor
    Ordenar(intervalos) por L
    
    refugios_elegidos = 0
    km_actual = inicio_sendero
    i = 0
    n = longitud(intervalos)
    
    // 3. Ciclo principal para cubrir todo el camino
    Mientras km_actual < fin_sendero:
        mejor_fin = -INFINITO
        
        // Mientras haya proyectos que arranquen en o antes de la zona que ya tengo cubierta...
        Mientras i < n y intervalos[i].L <= km_actual:
            
            // ...busco el que me tire lo más lejos posible hacia adelante
            Si intervalos[i].R > mejor_fin:
                mejor_fin = intervalos[i].R
                
            i = i + 1
            
        // Si no encontré ningún proyecto que avance más allá de donde estoy, 
        // significa que hay un "hueco" en el camino que nadie cubre.
        Si mejor_fin <= km_actual:
            Retornar "Es imposible cubrir todo el sendero"
            
        // Hago mi elección greedy: salto hasta el nuevo fin máximo
        km_actual = mejor_fin
        refugios_elegidos = refugios_elegidos + 1
        
    Retornar refugios_elegidos
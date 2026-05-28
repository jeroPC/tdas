funcion algoritmo_greedy_generico(datos_del_problema, restriccion_global):
    
    # 1. INICIALIZACIÓN DE VARIABLES
    # Aquí creamos los contenedores para las respuestas y los acumuladores.
    solucion_final = []          # Colección o estructura para el resultado
    estado_actual = 0            # Lleva la cuenta del progreso (ej. peso, volumen, tiempo)
    metrica_optimizacion = 0     # Lo que queremos minimizar o maximizar (ej. costo, ganancia)
    
    # 2. PASO DE VIABILIDAD INICIAL / OBLIGATORIO (Si el enunciado lo pide)
    # Algunos problemas exigen cumplir un mínimo antes de empezar a elegir libremente.
    para cada elemento en datos_del_problema:
        # Asignar lo mínimo obligatorio por regla
        # Actualizar estado_actual
        # Actualizar metrica_optimizacion
        
    # Control de seguridad: ¿Es posible resolver el problema con estos mínimos?
    si estado_actual > restriccion_global:
        retornar "Error: El problema no tiene solución válida"
        
    # 3. CRITERIO GREEDY (EL ORDENAMIENTO) 📊
    # Es el corazón del algoritmo. Ordenamos según lo que nos acerque más rápido al óptimo.
    # - Si queremos MINIMIZAR (costos, tiempo): Ordenamos de MENOR a MAYOR.
    # - Si queremos MAXIMIZAR (ganancias, valor): Ordenamos de MAYOR a MENOR.
    ordenar_datos_por_criterio_greedy(datos_del_problema)
    
    # 4. BUCLE PRINCIPAL (TOMA DE DECISIONES VORAZ) 🔄
    para cada elemento en datos_del_problema:
        
        # Condición de parada: Si ya alcanzamos la meta global, terminamos.
        si estado_actual == restriccion_global:
            romper bucle
            
        # Evaluar restricciones locales del elemento
        espacio_disponible = restriccion_global - estado_actual
        limite_local_elemento = elemento.maximo - elemento.actual
        
        # Tomar la decisión óptima local (lo máximo posible)
        cantidad_a_tomar = min(espacio_disponible, limite_local_elemento)
        
        # 5. ACTUALIZACIÓN DEL ESTADO 📐
        solucion_final.agregar_o_actualizar(elemento, cantidad_a_tomar)
        estado_actual = estado_actual + cantidad_a_tomar
        metrica_optimizacion = metrica_optimizacion + (cantidad_a_tomar * elemento.valor)
        
    # 6. CONTROL DE VIABILIDAD FINAL ⚠️
    # Verificamos si logramos cumplir con la meta exacta.
    si estado_actual < restriccion_global:
        retornar "Error: No se pudo completar la restriccion global con los límites dados"
        
    # 7. RETORNO DE RESULTADOS
    retornar solucion_final, metrica_optimizacion
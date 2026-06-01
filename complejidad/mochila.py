def reducir_a_mochila(lista_numeros, suma_objetivo_S):
    # Cada número de la lista se convierte en un objeto de la mochila
    elementos_mochila = []
    for numero in lista_numeros:
        # Truco: Hacemos que el valor de cada objeto sea igual a su peso
        objeto = {
            "peso": numero,
            "valor": numero
        }
        elementos_mochila.append(objeto)
        
    # El tope de la mochila es la suma objetivo S
    capacidad_maxima_W = suma_objetivo_S
    
    # El beneficio mínimo esperado también es S
    beneficio_minimo_B = suma_objetivo_S
    
    return elementos_mochila, capacidad_maxima_W, beneficio_minimo_B
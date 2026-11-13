"""
División y conquista: Una empresa registra la satisfacción de un cliente a lo largo de los meses 
mediante etiquetas cualitativas distintas (por ejemplo: A, B, C, D, E, ...), 
donde cada etiqueta representa un nivel distinto y todas son comparables entre sí
 (existe un orden total entre ellas). Se sabe que en el tiempo las calificaciones 
 fueron estrictamente descendiendo y 
que a partir de cierto mes comenzaron a mejorar de forma escrita y continua.
 La empresa quiere determinar en qué mes ocurrió el cambio para entender cuáles de 
 los cambios que fue implementando con
 el tiempo fue el que sirvió. Presentar un algoritmo eficiente para resolver este problema.
"""

def encontrar_mes_cambio(calificaciones):
    izquierda = 0
    derecha = len(calificaciones) - 1
    
    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        
        if calificaciones[medio] > calificaciones[medio + 1]:
            izquierda = medio + 1
        else:
            derecha = medio
            
    return izquierda


def encontrar_mes_cambio_recursivo(calificaciones, inicio, fin):
    if inicio == fin:
        return inicio
    
    medio = (inicio + fin) // 2
    
    if calificaciones[medio] > calificaciones[medio + 1]:
        return encontrar_mes_cambio_recursivo(calificaciones, medio + 1, fin)
    else:
        return encontrar_mes_cambio_recursivo(calificaciones, inicio, medio)



def buscar_cambio(calificaciones):
    if not calificaciones:
        return -1 
    return encontrar_mes_cambio_recursivo(calificaciones, 0, len(calificaciones) - 1)
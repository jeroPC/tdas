""""

 Una encuesta de internet pidió a personas que ordenen un conjunto de “n” películas
comenzando por las que más les gusta a las que menos. Con los resultados quieren
encontrar quienes comparten gustos entre sí. Nos solicitan generar un algoritmo, que
basándose en el concepto de inversión, compare entre pares de personas y determine qué
tan compatibles o incompatibles son. Proponer un algoritmo utilizando división y conquista
que lo resuelva"""


persona1 = {titanic , maracana, interestelar, macri}
persona2 = { maracana, interestelar, macri , titanic}
persona3 = { maracana, macri, titanic, interestelar}


tomamos a la primer persona y a titanic le asignamos 1 , maracana = 2 interestelar =3 macri =4
osea [1 2 3 4]

para la segunda persona la lista va a ser  [2 3 4 1]

para la tercera sera [2 4 1 3 ]

luego comparamos en persona2 , las ivnersiones comparando con el 1, osea 

maracana  esta antes en el vector que  1 (titanic) , si entonces 1 rotacion
interestelaresta antes en el vector que  1 (titanic) , si entonces 1 rotacion
macri esta antes en el vector que  1 (titanic) , si entonces 1 rotacion 
total rotaciones para persona2 = 3


si tuviera 0 inversiones, es que tiene el mismo top de peliculas

maximo de inversion es [n (n -1 )] / 2 


def calcular_compatibilidad_usuarios(lista_personas):
    # Tomamos a la Persona 1 como referencia base
    persona_referencia = lista_personas[0]

    # Armamos el hash/diccionario de posiciones (O(n))
    posiciones_referencia = Hash()
    para i desde 0 hasta len(persona_referencia) - 1:
        pelicula = persona_referencia[i]
        posiciones_referencia[pelicula] = i  # Guardamos el índice como su "puntuación"

    resultados_compatibilidad = Diccionario()

    para cada persona en lista_personas[1:]:

        arreglo_numerico = []
            para cada pelicula en persona.peliculas:
                arreglo_numerico.append(posiciones_referencia[pelicula])

        arreglo_ordenado, total_inversiones = contar_inversiones_rec(arreglo_numerico)

        resultados_compatibilidad[persona.nombre] = total_inversiones

    return resultados_compatibilidad


def contar_inversiones_rec(arreglo):
    si len(arreglo) <= 1:
        return arreglo, 0
    

    mitad = len(arreglo) // 2
    izq = arreglo[:mitad]
    der = arreglo[mitad:]

    izq_ordenada, inv_izq = contar_inversiones_rec(izq)
    der_ordenada, inv_der = contar_inversiones_rec(der)

    arreglo_combinado, inv_mezcla = mezclar_y_contar(izq_ordenada, der_ordenada)

    total_inversiones = inv_izq + inv_der + inv_mezcla

    return arreglo_combinado, total_inversiones

def mezclar_y_contar(izq, der):
    i = 0  
    j = 0  
    inversiones_mezcla = 0
    resultado = []

    mientras i < len(izq) y j < len(der):
        si izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        sino:
            # encontramos una inversión El de la derecha es más chico.
            resultado.append(der[j])
            
            inversiones_mezcla += (len(izq) - i)
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])

    return resultado, inversiones_mezcla
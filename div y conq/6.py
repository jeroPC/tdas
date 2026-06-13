"""


Contamos con una lista ordenada de “n” coordenadas satelitales (latitud-longitud) que
conforman un área con forma poligonal convexa. Queremos mostrar ese sector del mapa
con el mayor tamaño posible en nuestra pantalla rectangular de la computadora. El
programa que muestra el mapa acepta como
parámetros 2 coordenadas para construir el
rectángulo a mostrar: los correspondientes a los
límites inferior izquierdo y superior derecho.
Construya un algoritmo eficiente que resuelva el
problema con complejidad O(logn). ¿Existe una
solución de fuerza bruta que para “n” pequeños sea
más eficiente? ¿para qué tamaño de n esto cambia?
"""


un poligonon convexo es como si fuera una montania , una vez que sube y llega a su pico maximo , no vuelve a subir 

es como si fuera una 🏔️ 

def buscar_maximo (lote, inicio , fin ):
    if inicio == fin :
        return lote[inicio]

    mitad = (inicio + fin) // 2

    if lote[mitad] > lote[mitad - 1] and lote[mitad] > lote[mitad + 1]:
        return lote[mitad]
    elif lote[mitad] > lote[mitad - 1]:
        return buscar_maximo(lote, mitad + 1, fin)
    else:
        return buscar_maximo(lote, inicio, mitad - 1)



def buscar_minimo(lote, inicio, fin ):
    if inicio ==fin :return

    mitad = (inicio + fin) // 2

    if lote[mitad] < lote[mitad - 1] and lote[mitad] < lote[mitad + 1]:
        return lote[mitad]
    elif lote[mitad] < lote[mitad -1 ]:
        return buscar_minimo(lote, mitad+1 , fin)
    else:
        return buscar_minimo(lote, inicio, mitad -1)

def mayor_tamanio_pantalla(lote):
    longitud = len(lote)
    
    min_X_izq = buscar_minimo(lote, 0, longitud - 1)
    min_Y_izq = buscar_minimo(lote, 0, longitud - 1)

    max_X_der = buscar_maximo(lote, 0, longitud - 1)
    max_Y_der = buscar_maximo(lote, 0, longitud - 1)

    inferior_izq = [ min_X_izq[0] , min_Y_izq[1]]
    superior_der = [ max_X_der[0] , max_Y_der[1]  ]

    return inferior_izq , superior_der


teorema maestro = t(n) = a * t(n/b) + o(n^c )

donde a cantidad lllamada recursivas = 1 
b , division del subproblema = 2 
c = costo combinar y dividir

por lo tanto si log b (a) = c ==> log(n^c log b (a)) ===> O(log n)


por fuerza bruta por fuerza bruta la complejidad es O(N) es recorrer y por cada iteracion  agarrar el valor más chico más grande en X e Y  y luego retornar eso combinar 
y retornar,  ahora la complejidad va a cambiar mucho cuando tenga un lote muy grande porque espacialemnte y temporalmente es más costoso recorrer 1 millón de elementos pero al dividir el problema logarítmicas 
 veces va a ser mucho mejor usar la versión de la búsqueda binaria además que la complejidad es menor



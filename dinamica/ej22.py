"""
Se proyectó la construcción de una línea de tensión eléctrica. En su trayecto pasa cerca de
“n” ciudades que tienen diferentes demandas de consumo eléctrico. Para la interconexión
entre la línea y una central se debe construir una nexo. Por cuestiones regulatorias y
constructivas no se pueden construir nexos a menos de “x” kilómetros entre sí. Contamos
con el listado de las ciudades. Para cada ciudad nos informan su población y la ubicación en
la línea del nexo a construir. Mediante programación dinámica proponga una solución que
permita seleccionar qué ciudades conectar para maximizar la cantidad total de población
cubierta por esta línea.
"""


"""

datos : linea de tension 
----  pasa por n ciudades (con dif demandas de consumo)
----    no se pueden crear nexos a menos de 'x' km entre si 
----Contamos  listado de las ciudades. Para cada ciudad nos informan su población y la ubicación en
la línea del nexo a construir. 


objetivo : 

---- Mediante programación dinámica proponga una solución que
permita seleccionar qué ciudades conectar para maximizar la cantidad total de población
cubierta por esta línea.

# recurrencia : OPT = MAX {OPT(i -1), gi + opt(previo_copmpatible(i))}


"""

class Ciudad:
    def __init__(self, nombre, km, poblacion):
        self.nombre = nombre
        self.km = km
        self.poblacion = poblacion

def calcular_compatibles(ciudades, x): 
    n = len(ciudades)
    compatible = [0] * (n + 1)
    
    j = 0  
    for i in range(n):
        while j < i and ciudades[i].km - ciudades[j].km >= x:
            j += 1
       
        compatible[i + 1] = j

    return compatible


def red_electrica(ciudades):

    compatibles = compatibles(ciudades)
    OPT = [0] * len(ciudades)

    for i in range(1, len(ciudades) +1):
        no_opt = OPT(i -1)
        mejor_opt = ciudades[i].ganancia + opt(compatibles[i])

        OPT[i] = max(mejor_opt, no_opt)
    
    return opt[n], compatibles

def reconstruccion(ciudades, opt, compatibles):
    ciudades-elegidas[]
    i = len(ciudades) 
    while i > 0:
        if opt[i] != opt[i-1]:
            ciudades-elegidas.add(ciudades[i])
            i = compatible[i]
        else:
            i -= 1

    return ciudades


#ambas complejidades o(n)
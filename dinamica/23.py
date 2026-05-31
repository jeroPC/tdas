"""
El dueño de una cosechadora está teniendo una demanda muy elevada en los próximos 7
meses. Desde “n” campos lo quieren contratar para que preste sus servicios.
5 Teoría de Algoritmos: Ejercicios Greedy - Ing Víctor Podberezski
Lamentablemente no puede hacer todos los contratos puesto que varios de ellos se
superponen en sus tiempos. Cuenta con un listado de los pedidos donde para cada uno de
ellos se consigna: fecha de inicio, fecha de finalización, monto a ganar por realizarlo. Su idea
es seleccionar la mayor cantidad de trabajos posibles. Mostrarle que esta solución puede no
ser la óptima. Proponer una solución utilizando programación dinámica que nos otorgue el
resultado óptimo (que trabajos elegir y cuanto se puede ganar).

"""
"""
El enfoque Greedy (codicioso) de elegir la mayor cantidad de trabajos falla rotundamente porque ignora el peso económico. Un solo trabajo 
largo podría pagar 1.000.000, mientras que tres trabajos cortos que se superponen con ese grande pagan 10 cada uno.
 Maximizar la cantidad nos daría 30, mientras que maximizar la ganancia nos da el millón.

"""

# recurrencia = opt[0] = 0. opt[i] = max{ opt(i-1), vi + opt(compatible[i]) }
def compatibles_con_for(contratos):
    n = len(contratos)
    compatible = [0] * (n + 1)

    # i representa el contrato actual (1-indexed para la DP)
    for i in range(1, n + 1):
        # Buscamos hacia atrás desde el contrato anterior (i-2) hasta el principio (0)
        # contratos[i-1] es el contrato actual en el array indexado en 0
        ultimo_compatible = 0
        
        for j in range(i - 1, 0, -1):
            # Recordá: el fin de J tiene que ser menor o igual al inicio de I
            if contratos[j - 1].finalizacion <= contratos[i - 1].inicio:
                ultimo_compatible = j
                break # ¡Frenamos! Ya encontramos el más cercano que es compatible
                
        compatible[i] = ultimo_compatible
        
    return compatible
 


def maximizar_ganancia(contratos):
    n = len(contratos)
    contratos = mergesort(por fecha de finalizacion) #de menor a mayor

    compatible = compatibles(contratos)
    OPT = [0] * len(contratos)
    OPT[0] = 0 

    for i= 0 hasta n+1:
        no_actualizo = opt(i -1)
        actualizo = contratos[i].ganancia + opt(contratos[i])
    
        OPT[i] = max(no_actualizo,actualizo)
    
    return OPT[n],compatibles

def reconstruccion(contratos, OPT, compatible):
    contratos_elegidos = []
    i = len(contratos) 
    
    while i > 0:
        actualizo = contratos[i - 1].ganancia + OPT[compatible[i]]
        
        if OPT[i] == actualizo:
            contratos_elegidos.append(contratos[i - 1])
            i = compatible[i]
        else:
            i -= 1
            
    return contratos_elegidos[::-1]
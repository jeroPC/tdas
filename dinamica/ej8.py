"""Contamos con una carretera de longitud M km que tiene distribuidos varios carteles
publicitarios. Cada cartel ”i” está ubicado en un “ki” kilómetro determinado (pueden ubicarse
en cualquier posición o fracción de kilómetro) y a quien lo utiliza le asegura una ganancia
“gi”. Por una regulación no se puede contratar más de 1 cartel a 5km de otros. Queremos
determinar qué carteles conviene contratar de tal forma de maximizar la ganancia a obtener."""

# recurrencia : OPT = MAX {OPT(i -1), gi + opt(previo_copmpatible(i))}

# caos base opt (0) = 0 


def previo_compatible(carteles):
    #los carteles ya estan ordenado de menor a mayor por km
    compatible = [0] * (n +1)
    j= 1;

    for i in range(len(compatible)):
        while j < i and carteles[i].km - carteles[j].km >= 5:
            j+= 1
        
        compatible[i] = j -1



def maxima_ganancia(carteles):
    #len carteles =  M
    #ordeno de menor a mayor a carretera por km  o(nlog n)

    compatible = previo_compatible(carteles)
    OPT = [0] * (n + 1)
    
    for i in range(1, n +1):
        opcion_no_contratar = OPT[i-1]

        indice_compatible = compatible[i]
        opcion_contratar = carteles[i].maxima_ganancia + OPT(previo_compatible[i])

        OPT[i] = max(opcion_no_contratar, opcion_contratar) 



def reconstruccion(carteles, compatible, OPT):
    carteles_elegidos = []
    i = len(carteles)
    while i > 0:
        if OPT[i] != OPT(i-1):
            carteles_elegidos.add(carteles[i])
            i = compatible[i]
        else:
            i = i - 1

    return carteles_elegidos




"""complejidad  temporal = o(nlogn)
    espacial = o(n)

"""
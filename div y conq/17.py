""". Sea S un conjunto de n puntos en el plano. Definimos que un punto p=(x,y) ∈ S es un
punto máximo en S si no existe otro punto p’=(x’,y’) ∈ S tal que x ≤x’ e y≤y’. Queremos
obtener todos los puntos de S que sean máximos. Plantear un algoritmo de división y
conquista para que lo resuelva. Analizar su complejidad computacional. (HINT: De ser
requerido puede realizar un preorden del conjunto)"""


def BuscarMaximos(S):

    #ordeno por merge sort al conjunto S , las x de menor a mayor
    Si |S| == 1: 
        Devolver S
    
    mitad = len(s) / 2
    izq = s[:midad]
    der = s[mitad:]

    M_izq = BuscarMaximos(S_izq)
    M_der = BuscarMaximos(S_der)

    Y_max_der = -Infinito

    for punto in M_der:
        Si punto.y > Y_max_der:
            Y_max_der = punto.y
    

    Filtrados_Izq = []
    for punto in M_izq:
        Si punto.y > Y_max_der:
            Filtrados_Izq.add(punto)
        

    return Filtrados_Izq + M_der



t(n) = a * t(n/b) + o(n^c )

a = 2 b = 2 c = 1 --> o(n)

nlog n 
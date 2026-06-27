"""La sala de guardia de un hospital tiene que tener al menos un médico en todos los
feriados y en los fines de semana largos de feriados. Cada profesional indica sus
posibilidades: por ejemplo alguien puede estar de guardia en cualquier momento del fin de
semana largo del 9 de julio (p. ej. disponibilidad de A para el 9 de julio = (Jueves 9/7, Viernes
10/7, Sábado 11/7, Domingo 12/7)), también puede suceder que alguien pueda sólo en parte
(por ejemplo, disponibilidad de B para 9 de julio = (Jueves 9/7, Sábado 11/7, Domingo 12/7)).
Aunque los profesionales tengan múltiples posibilidades, a cada uno se lo puede convocar
para un solo día (se puede disponer de B sólo en uno de los tres días que indicó). Para
ayudar a la sala de guardia a planificar cómo se cubren los feriados durante todo el año
debemos resolver el problema de las guardias: Existen k períodos de feriados (por ejemplo, 9
de julio es un período de jueves 9/7 a domingo 12/7, en 2019 Día del Trabajador fue un
período de 1 día: miércoles 1 de mayo, etc.). Dj es el conjunto de fechas que se incluyen en el
período de feriado j-ésimo. Todos los días feriados son los que resultan de la unión de todos
los Dj. Hay n médicos y cada médico i tiene asociado un conjunto Si de días feriados en los
que puede trabajar (por ejemplo B tiene asociado los días Jueves 9/7, Sábado 11/7, Domingo
12/7, entre otros).
Proponer un algoritmo polinomial (usando flujo en redes) que toma esta información ydevuelve qué profesional se asigna a cada día feriado (o informa que no es posible resolver
el problema) sujeto a las restricciones:
○ Ningún profesional trabajará más de F días feriados (F es un dato), y sólo en días en
los que haya informado su disponibilidad.
○ A ningún profesional se le asignará más de un feriado dentro de cada período Dj."""



modelado del grafo:

s = fuente t = sumidero

nodo medico Mi = un nodo para cada uno de los n medicos

nodo medico periodo Mi , Dj Esta es la clave. Necesitamos un nodo que represente la participación del médico i en el período de feriado j
Nodos Día Feriado (d): Un nodo por cada fecha feriada individual de la unión de todos los Dj

2) aristas y capacidades :
    conectamos  S a cada medico Mi con capacidad F 

Conectamos M_i ===> M_i, D_j si el médico i tiene disponibilidad en al menos un día del período D_j.

Capacidad = 1: Esto es lo que resuelve la segunda restricción. Como la capacidad es 1, el médico i solo podrá aportar como máximo 1 unidad de flujo a todo ese período D_j

De los Períodos a los Días Feriados:Conectamos el nodo (M_i, D_j) ==> d para cada día d e D_j en el cual el médico i explícitamente indicó que está disponible es decir, d e S_i
capacidad 1 , un medico por dia

De los Días Feriados al Sumidero:Conectamos cada nodo de día feriado d ===> t.
Capacidad = 1: Porque la sala de guardia necesita al menos un médico por feriado (buscamos cubrir exactamente 1 por día).



def actualizar_grafo_residual(grafo_residual, u, v, botella):
    # Arista hacia adelante (u -> v): pierde capacidad
    peso_ant = grafo_residual.peso(u, v)
    if peso_ant == botella:
        grafo_residual.remover_arista(u, v)
    else:
        grafo_residual.cambiar_peso(u, v, peso_ant - botella)
    
    if not grafo_residual.hay_arista(v, u):
        grafo_residual.agregar_arista(v, u, botella)
    else:
        peso_retorno_ant = grafo_residual.peso(v, u)
        grafo_residual.cambiar_peso(v, u, peso_retorno_ant + botella)


def ford_fulkerson(grafo, s, t):
    flujo = {}
    flujo_total = 0  

    for v in grafo:
        for w in grafo.ady(v):
            flujo[(v, w)] = 0

    grafo_residual = copiar(grafo)

    while (camino := buscar_camino_bfs(grafo_residual, s, t)): 
        botella = min_peso(grafo_residual, camino)
        flujo_total += botella  

        for i in range(1, len(camino)):
            u = camino[i - 1]
            v = camino[i]

            if grafo.hay_arista(u, v):
                flujo[(u, v)] += botella
            else:
                flujo[(v, u)] -= botella
            
            actualizar_grafo_residual(grafo_residual, u, v, botella)
            
    return flujo_total, flujo, grafo_residual


def planificar_guardias(medicos, periodos_feriados, F):
    grafo, s, t, dias_totales = construir_red_flujo(medicos, periodos_feriados, F)
    
    flujo_max, asignaciones, _ = ford_fulkerson(grafo, s, t)
    
    if flujo_max == len(dias_totales):
        cronograma = {arista: f for arista, f in asignaciones.items() if f == 1}
        return True, cronograma
    
    return False, None
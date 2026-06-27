"""
Un servidor de videojuegos se alquila por horas. El contrato dura un tiempo fijo y
permite utilizar en forma exclusiva el mismo por una cantidad continua de horas una vez por
semana. Por cada contrato que el dueño del servidor establece, se lleva un monto fijo de
dinero. Al dueño del servidor le interesa tener la mayor cantidad de contratos posibles (sin
importar la duración en horas de los mismos). El servidor funciona las 24hs. Recibe un
conjunto de ofertas de contrato y debe seleccionar cuales aceptar. Cada contrato tiene un
día y hora de inicio y un día y hora de fin. Durante ese lapso tendrán la exclusividad del
servidor. Ese tiempo contiguo no puede durar más de 1 semana (un contrato podría pedir
por ejemplo 3 días completos pero nunca superar la semana).. Y esa fecha se repite todas las
semanas. Los contratos aceptados no deben superponerse. Proponer una solución greedy
que solucione el problema de forma óptima. Tenga en cuenta que es posible contratos que
empiecen al finalizar la semana y terminen horas después del inicio de la misma."""


server alquila por hs
contrato fijo , permite usar de forma exclusiva el mismo por una cantidad de horas continuas de hroas
una vez por semana


obj = mayor cantidad contratos posibles

cada contraro tiene. dia hora inicio y dia horario fin 


def elegir_contratos(lista_de_ofertas):

    for contrato in lista_de_ofertas:
        contrato['inicio_lineal'] = (contrato['dia_inicio'] * 24) + contrato['hora_inicio']
        contrato['fin_lineal'] = (contrato['dia_fin'] * 24) + contrato['hora_fin']
        
        if contrato['inicio_lineal'] > contrato['fin_lineal']:
            contrato['fin_lineal'] = contrato['fin_lineal'] + 168

    lista_ordenada = mergesort(lista_de_ofertas, clave='fin_lineal')
    
    max_contratos_global = 0

    for i in range(len(lista_ordenada)):
        contrato_ancla = lista_ordenada[i]
        
        cantidad_de_esta_vuelta = 1
        ultimo_fin_valido = contrato_ancla['fin_lineal']
        
        for j in range(i + 1, len(lista_ordenada)):
            contrato_posible = lista_ordenada[j]
            
            if contrato_posible['inicio_lineal'] >= ultimo_fin_valido:
                cantidad_de_esta_vuelta = cantidad_de_esta_vuelta + 1
                
                ultimo_fin_valido = contrato_posible['fin_lineal']
                
        if cantidad_de_esta_vuelta > max_contratos_global:
            max_contratos_global = cantidad_de_esta_vuelta

    return max_contratos_global


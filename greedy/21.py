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
    n = len(lista_de_ofertas)
    if n == 0:
        return 0

    # Pasamos todo a horas de la semana (0 a 168)
    for c in lista_de_ofertas:
        c['inicio'] = c['dia_inicio'] * 24 + c['hora_inicio']
        c['fin'] = c['dia_fin'] * 24 + c['hora_fin']
        if c['inicio'] >= c['fin']:
            c['fin'] += 168

    # Ordenamos por fin ascendente: O(n log n)
    lista_ordenada = mergesort(lista_de_ofertas, clave='fin')
    max_contratos = 0

    # Probamos cada contrato como ancla: O(n)
    for i in range(n):
        ancla = lista_ordenada[i]
        
        # Armamos la linea de tiempo desde el ancla hacia adelante
        # y al final clavamos la copia del ancla con tu marca 9999
        cola = []
        for offset in range(1, n):
            c = lista_ordenada[(i + offset) % n].copy()
            if c['inicio'] < ancla['inicio']:
                c['inicio'] += 168
                c['fin'] += 168
            cola.append(c)

        # Tu marca 9999 en la copia del ancla para detectar la vuelta completa
        copia_ancla = {
            'inicio': ancla['inicio'] + 168,
            'fin': ancla['fin'] + 168,
            'marca': 9999
        }
        cola.append(copia_ancla)

        cantidad = 1
        ultimo_fin = ancla['fin']

        # Recorremos secuencialmente hasta entrar en el rango del 9999
        for candidato in cola:
            # Si este candidato se pisa con el 9999 (o es el 9999), ya dimos toda la vuelta
            if candidato['fin'] > copia_ancla['inicio'] or candidato.get('marca') == 9999:
                break

            if candidato['inicio'] >= ultimo_fin:
                cantidad += 1
                ultimo_fin = candidato['fin']

        if cantidad > max_contratos:
            max_contratos = cantidad

    return max_contratos
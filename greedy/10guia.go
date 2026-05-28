0. Un fabricante de perfumes está intentando crear una nueva fragancia. Y desea que la
misma sea del menor costo posible. El perfumista le indicó un listado de ingredientes. Por
cada uno de ellos determinó una cantidad mínima (puede ser cero) y una máxima que debe
contar en la fórmula final. Cada ingrediente tiene asociado un costo por milímetros cúbicos.
Sabiendo que en la presentación final es de X milímetros cúbicos. Presentar una solución
utilizando metodología greedy que resuelva el problema

ingredientes= [ingrediente.minimo, ingrediente.maximo, ingrediente.costo]
fucn crear-perfume(lista_ingredientes,costo ) :

	ordenar_por_mergesort(lista_ingredientes, costo)	x = VOLUMEN FINAL DESEADO (VA A IR RESTANDOSE INTERNAMNET )

	resultado =[]
	volumen-actual= 0
	costo-total = 0

	para cada ingrediente en lista_ingredientes:
		cantidad_asignada = ingrediente.minimo
		volumen_actual = volumen_actual + cantidad_asignada
		resultado[ingrediente] = cantidad_asignada
		costo_total = costo_total + (cantidad_asignada * ingrediente.costo)

	si volumen > x:	retorno error 

	para cada ingrediente en lista_ingredientes:
		si volumen_actual == X:
            break
	
		espacio_libre = x - volumen_actual
		limite_ingredientes = ingrediente.maximo ingrediente.minimo

		# Elegimos el menor entre lo que falta para llenarlo o el máximo del ingrediente
        cantidad_extra = min(espacio_libre, limite_ingrediente)

		# Actualizamos la fórmula
        resultado[ingrediente] = resultado[ingrediente] + cantidad_extra
        volumen_actual = volumen_actual + cantidad_extra
        costo_total = costo_total + (cantidad_extra * ingrediente.costo)

	si volumen_actual < X:
        retornar "Error: No se puede alcanzar el volumen X con los máximos permitidos"
        
    retornar resultado, costo_total


	complejidad , la de mergesort 
	espacial o(n) la de crear lista_ingredientes




	


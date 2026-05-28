Programación dinámica: Juan desea comprar perfumes para revender entre sus conocidos. 
Puede llevar "k" kilos antes de superar el límite de su bolso. 
Por cada uno de los "n" perfumes que le interesan conoce el PRECIO  DE COMPRA y el de REVENTA.
 Todos los perfumes cuentan con un peso unitario y stock ilimitado. Ayudar a Juan a maximizar 
 la ganancia a obtener. Solucione el problema utilizando programación dinámica.

RECURRENCIA = opt(i,p) = max { opt(i -1 , p ) , vi + opt( i, p - ci)}
ci es el peso de cada objeto 


ganancia NETA = PRECIO DE VENTA - COMPRA 

Gi = PVi - Ci

func max_perfume(k,n , pesos, compras, reventas):
	ganancia_max = array inicializado en cero con k =1 elementos

	ganancia_max[0] = 0

	para C = 1 hasta k:
		ganancia_act = -infinito

		para i desde 1 hasta n: 
			si pesos[i] <= C :

				ganancia_neta = reventas[i] - compras[i]

				//recurrencia
				ganancia_posible = ganancia_neta + ganancia_max(c - pesos[i])

				si ganancia_posible > ganancia_act:
					ganancia_act = ganancia_posible
					perfume_elegido = i

		ganancia_max[c] = ganancia_act
		eleccion[c] = perfume_elegido

	return ganancia_max, perfume_elegido


	
#TEBNEMOS UIN GRAFO
#CADA ARISTA TIENE UN PESO, LA CAPACIDAD MAXIMA DE AUTOS QUE PERMITE PASAR POR ELLA

1RE CONDICON = SE DEBEN DESPLAZAR N AUTOS DESDE UNA CIUDAD S A OTRA T 

OBJETIVO = VER SI ES POSIBLE EL TRALADO EN CASO DE NO , QUE RUTAS DEBEMOS REFORZAR

DATO = SON 2 LOS CONJUTNOS DISJUNTOS  DE RUTAS QUE PUEDEN COLAPSAR EL TRANSITO OTRO DICE Q ES SOLO 1 

NOS PIDEN NEGAR UNA AFRIMACION DE LAS DOS SI ES POSIBLE



func cuello_de_botella(flujo, camino, capacidad):
	return min(capacidad[u,v]) - flujo[u,v] para cada (u,v) en camino


func grafo_residual(grafo , flujo , capacidad):
residual = crear grafo vacio

para cada arista (u,v ) en grafo:
	si capacidad(u,v ) - flujo[u,v ] > 0:
		agregar en residual (u,v) con capacidad[(u,v)] - flujo[(u,v)]
	si flujo[(u,v)] > 0:
		agrego en residual (v,u) el peso de flujo[(v,u)]

retorno residual

func aumentar_flujo(flujo , camino,capacidad):
	botella = cuello_de_botella(flujo , camino, capacidad)

	para cada arista  (u,v) en camino:
		si (u,v) es arista hacia adelante:
			flujo[(u,v)] += botella
		sino:
			flujo[(v,u)] -= botella 
		
	retornar botella


func flujo_maximo(grafo , capacidad, s, t):
	flujo[(u,v)] = 0 para todas las aristas del grafo
	flujo_total = 0

	mientras exista un camino de s a t en grafo_residual(grafo, flujo , capacidad):
		flujo_total += aumentar_flujo(flujo, camino , capacidad)

	retorno flujo_total

def corte_minimo(grafo, flujo, capacidad, s):
    # grafo residual final (ya no hay caminos aumentantes)
    residual = grafo_residual(grafo, flujo, capacidad)
    
    # BFS para ver qué nodos siguen siendo alcanzables desde fuente
    alcanzables = BFS(residual, s)
    
    zonas_debiles = []
    para cada arista (u, v) en grafo original:
        si u está en alcanzables Y v NO está en alcanzables:
            zonas_debiles.agregar((u, v))   # arista saturada = zona débil
    
    retornar zonas_debiles

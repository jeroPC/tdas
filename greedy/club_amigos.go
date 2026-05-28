

func ClubAmigos(grafo):

	// G tiene un conjunto de Vértices V y Lista de Adyacencia
    n = cantidad_de_vertices(V)

	para cada Vertice en v:
		calculo grado de cada vertice y lo guardo en un diccionario grado_vertices[vertice] = grado(vertice)
	
	activo = array de n elementos inicializado en True
	cola = crear_cola()

	para cada vertice en V:
		if grado_vertices[vertice] < 4:
			cola.encolar(vertice)
	
	mientras !cola.esta_vacia():
		vertice_actual = cola.desencolar()
		activo[vertice_actual] = False

		para cada vecino en grafo.adyacentes(vertice_actual):
			if vecino is activo:
				grado[vecino] =- 1

				if grado[vecino] < 4:
					cola.encolar(vecino)
					activo[vecino] = False


	invitacion_final = []

	for vertice en V: 
		if activo[vertice]:
			invitacion_final.agregar[vertice]

	return invitacion_final



	Complejidad o( n + m )
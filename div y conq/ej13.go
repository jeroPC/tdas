Un conjunto de “n” personas votó de forma anónima entre un conjunto de “o” opciones
(con o<<n). El resultado de la votación lo tenemos en un vector de n posiciones ordenado
por opción seleccionada. Queremos determinar cuántos votos tuvo cada una de las
opciones. Podemos hacerlo simplemente recorriendo el vector en O(n). Sin embargo,
utilizando división y conquista se puede lograr en un tiempo inferior. Presentar y analizar
una solución utilizando división y conquista que logre lo solicitado.


func  contarVotos (v ,n):

	Función contarVotos(V, n)
    resultados = CrearDiccionario() // Guardará pares del tipo {opcion: cantidad}
    
    // Llamamos a la función recursiva pasándole los extremos del vector
    contarVotosRec(V, 0, n - 1, resultados)
    
    Devolver resultados
FinFunción

func contarVotosRec(v , inicio , fin ,resultados) :

	Si V[ini] == V[fin] Entonces
			cantidad Votos = fin - ini + 1
			opcionActual = V[ini]

			Si V[ini] == V[fin] Entonces
				cantidad Votos = fin - ini + 1
				opcionActual = V[ini]


	mitad = incio +fin / 2
	contarVotosRec(v , inicio , mitad -1 ,resultados)

	contarVotosRec(v , mitad , fin ,resultados)







	
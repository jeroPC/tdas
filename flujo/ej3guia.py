. La compañía eléctrica de un país nos contrata para que le ayudemos a ver si su red de
transporte desde su nueva generadora hidroeléctrica hasta su ciudad capital es robusta. Nos
otorgan un plano con la red eléctrica completa: todas las subestaciones de distribución y red
de cableados de alta tensión. Lo que quieren que le digamos es: cuantas secciones de su red
se pueden interrumpir antes que la ciudad capital deje de recibir la producción de la
generadora? (Sugerencia: investigue sobre el Teorema de Menger) Puede informar cual es el
subconjunto de ejes cuya falla provoca este problema

``


def actualizar_grafo_residual(grado_residual,u,v , valor):
    peso_ant= grado_residual.peso(u,v)

    if paso_anterior == botella :
        grafo_residual.remover_arista(u,v)
    else:
        grado_residual.cambiar_peso(u,v,pseo_anterior)
    
    if not grafo_residual.hay_arista(v,u):
        grado_residual.agregar_arista(v,u,valor)
    else:
        grado_residual.cambiar_peso(v,u,grado_residual)


def ford_fulkerson(grafo,s,t):
    flujo={}

    for v in grafo:
        for w in grafo.ady(v):
            flujo[(v,w)] = 0

    grafo_residual = copiar(grafo)

    while haya un camino de s a t: 
        #da el cuello de botella, osea le flujo minimo de cada camino 
        botella = min_peso(grafo_residual, camino)

        for i in range(len(camino)):
            u = camino[i -1]
            v = camino[i]

            if grafo.hay_arista(u,v):
                flujo[(u,v)] += botella
            else:
                flujo[(v,u)] -= botella
            
            actualizar_grafo_residual(grafo_residual,u,v,botella)



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


    
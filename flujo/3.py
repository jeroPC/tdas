""". La compañía eléctrica de un país nos contrata para que le ayudemos a ver si su red de
transporte desde su nueva generadora hidroeléctrica hasta su ciudad capital es robusta. Nos
otorgan un plano con la red eléctrica completa: todas las subestaciones de distribución y red
de cableados de alta tensión. Lo que quieren que le digamos es: cuantas secciones de su red
se pueden interrumpir antes que la ciudad capital deje de recibir la producción de la
generadora? (Sugerencia: investigue sobre el Teorema de Menger) Puede informar cual es el
subconjunto de ejes cuya falla provoca este problema?"""


	"""
================================================================================
ANÁLISIS Y RESOLUCIÓN DEL PROBLEMA: RED DE TRANSPORTE ELÉCTRICO
================================================================================

1. MODELADO DEL GRAFO Y CONSIDERACIONES TEÓRICAS (TEOREMA DE MENGER)
--------------------------------------------------------------------------------
Para determinar la robustez de la red de transporte desde la generadora hasta 
la capital, modelamos el sistema como un grafo dirigido G = (V, E).
- Fuente (S): Primera subestación, nodo origen por donde sale la energía.
- Sumidero (T): Ciudad capital, destino final que recibe la producción.
- Nodos Intermedios: Subestaciones de distribución de la red (ET1, ET2, ...).
- Capacidades: Basándonos en el Teorema de Menger para conectividad de aristas,
  como el enunciado pide la cantidad de secciones físicas a interrumpir, se
  asume que TODAS las aristas tienen capacidad igual a 1 (un cable de alta tensión).

2. ALGORITMO DE FORD-FULKERSON (EDMONDS-KARP)
--------------------------------------------------------------------------------
Se busca el flujo máximo mediante caminos aumentantes utilizando BFS:
- Se inicializa el flujo en cero y se crea el grafo residual.
- En cada iteración se busca un camino S -> T y se halla su cuello de botella 
  (que al ser capacidades unitarias, siempre sumará de a 1).
- Se actualiza el grafo residual: se reduce la capacidad hacia adelante y se 
  crean/incrementan las aristas de retorno para permitir la redistribución.
- El algoritmo termina cuando no hay más caminos en el residual. El flujo total 
  acumulado es el Flujo Máximo que, por Max-Flow Min-Cut, equivale al VALOR del 
  corte mínimo.

3. OBTENCIÓN DEL CORTE MÍNIMO (ZONAS CRÍTICAS)
--------------------------------------------------------------------------------
Para identificar qué cables cortan el suministro si fallan en simultáneo:
1. Hacemos un BFS/DFS final en el grafo residual partiendo desde la fuente (S). 
   Guardamos los nodos alcanzables en un set/vector ('alcanzables').
2. Iteramos sobre las aristas del GRAFO ORIGINAL.
3. Si una arista (u, v) del grafo original cumple que 'u' está en alcanzables 
   pero 'v' NO está, esa conexión está saturada y pertenece al CORTE MÍNIMO.

4. ANÁLISIS DE COMPLEJIDAD TEMPORAL
--------------------------------------------------------------------------------
- Flujo Máximo: O(|E| * |V| * f), donde |E| son aristas, |V| vértices y 'f' el 
  flujo máximo (acotado por el grado al ser capacidades unitarias).
- Cálculo del Corte Mínimo: El BFS final toma O(|V| + |E|). La posterior 
  iteración por las aristas del grafo original toma O(|E|), ya que la consulta 
  en el set de alcanzables es O(1).
- COMPLEJIDAD TOTAL: O(|E| * |V| * f). Las operaciones del corte mínimo no 
  empeoran la complejidad general de Ford-Fulkerson.

5. RESPUESTAS AL CLIENTE
--------------------------------------------------------------------------------
- ¿Cuántas secciones se pueden interrumpir?: Al valer cada arista 1, coincide 
  exactamente con el valor del Flujo Máximo (y con el len() de 'zonas_debiles').
- ¿Cuál es el subconjunto de ejes?: Las aristas del grafo original que conectan 
  un nodo alcanzable con uno inalcanzable del residual.
- Capacidad de transporte: El flujo máximo representa la capacidad tope actual 
  de la red en condiciones óptimas.
================================================================================
"""



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



def corte_minimo(grafo, flujo, capacidad, s):
    residual = grafo_residual(grafo, flujo, capacidad)
    
    # BFS para ver qué nodos siguen siendo alcanzables desde fuente
    alcanzables = BFS(residual, s)
    
    zonas_debiles = []
    para cada arista (u, v) en grafo original:
        si u está en alcanzables Y v NO está en alcanzables:
            zonas_debiles.agregar((u, v))  
    retornar zonas_debiles
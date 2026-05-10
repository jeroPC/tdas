
Instancia: e, p capitanes, n inscriptos, m, listas de compatibilidad
Certificado: una asignación propuesta → lista de m capitanes elegidos y a qué capitán va cada inscripto
func certificador(solucion, capitanes_elegidos, asignaciones):

	si capitanes_elegidos > m:
		FALSO
	
	para cada i en asignaciones:
		capitan_asignado = asignaciones[i]

		si capitan_asignado no esta en capitanes_elegidos:
			FALSO
		
		si i no esta en lista_aceptados:
			FALSO
		si capitan_asignado[i] no esta en lista_capitanes[i]
			FALSO
		si len[capitan_asignado] > e:
			FALSO

	return TRUE

Complejidad: O(n × p) en el peor caso → polinomial 

ahora demostramos por que este problema comparandolo con vertex cover puede ser en el mejor de los casos
nph sabiendo que vertex cover  e a los nph


digo que y = vertex cover , x = porblema de asingacion de incriptos a capitanes respetando las condiciones del problema

planteo que Y <=p X	 si puedo demostrar que tengo uin algoritmo que resuelve hackaton y que lo puedo usar para resolver vertex cover

equivalencias 
vertex cover = puedo elegir k vertices tal que todas las aristas sean cubieras por estos vertices? 

hack = si las aristas son MIS incriptos	, Y MIS vertices los capitanes, puedo aceptar a todas las aristas 
viendo los nodos que aceptan a estas arista (u,v) , satisfaciendo las condiciones ? 

Observamos que el problema de Hackatón es al menos tan difícil como Vertex Cover, ya que una instancia de Vertex Cover puede transformarse en una instancia de Hackatón: cada vértice se corresponde con un capitán, y cada arista representa un inscripto compatible con sus dos extremos. Resolver Hackatón sobre esta instancia equivale a resolver Vertex Cover sobre el grafo original. Por lo tanto Vertex Cover ≤ₚ Hackatón, lo que implica que Hackatón es NPH."




func T(grafo , k):
	para cada vertice v en V:
		crear capitan c_v
	
	para cada arista (u,v ) en E:
		crear_inscripto i(u,v)
		lista_aceptado[c_u] añado a i(u,v)
		lista_aceptado[c_v] añado a i(u,v)
		lista_capitanes(i(u,v)) = {c_u , c_v}

	m= K
	e= tamaño del equipo

	return (lista_capitanes, incriptos, m, e )

	complejidad o(v+e ) 


Caja negra
Recibe la instancia de Hackatón y devuelve capitanes_elegidos

func T2(capitanes_elegidos):
	SOLUCION = {}
	PARA CADA CAPITAN C EN CAPITANES_ELEGIDOS :
		AGREGO VERTICE V_S A s
	
	RETORNO s

COMPLEJIDAD O(V)



Instancia Vertex Cover
(G=(V,E), k)
        ↓
       T1
(traduzco a Hackatón)
        ↓
Instancia Hackatón
(capitanes, inscriptos, m)
        ↓
   CAJA NEGRA
(resuelve Hackatón)
        ↓
Solución Hackatón
(lista de capitanes elegidos)
        ↓
       T2
(traduzco de vuelta)
        ↓
Solución Vertex Cover
(conjunto S de vértices)



T1 NO asigna nada
T1 solo construye el problema. Crea los capitanes, crea los inscriptos, define quién es compatible con quién. Es como armar el enunciado del problema de Hackatón a partir del grafo.
No asigna. No decide. Solo traduce la estructura.

T2 NO verifica nada
T2 solo traduce la solución que ya dio la caja negra.
La caja negra ya resolvió todo. Ya verificó. Ya eligió. T2 solo dice "ese capitán era este vértice".



"La complejidad de resolver Vertex Cover usando esta reducción es la complejidad de Hackatón más un overhead
 polinomial de T1 y T2. Por lo tanto Vertex Cover ≤ₚ Hackatón
, lo que implica que Hackatón es al menos tan difícil como Vertex Cover, y por ende es NPH."


Si transformo una instancia de Vertex Cover en Hackatón con T1, y la caja negra encuentra solución en Hackatón, entonces con T2 obtengo una solución válida de Vertex Cover. Y viceversa




Y INSTANCIA VERTEX ---> T1 TRANSFORMO Y EN INSTANCIA DE HACK ----> X ---METO X EN CAJA NEGRA ---OBTENGO REPSUESTA T2 SOLUCION 
                                                                                                       VALIDA DE VERTEX COVER POR LO QUE ES VALIDA PARA Y Y X 



																									   Justificación de que funciona para cualquier instancia

Por cada vértice v en V se crea exactamente un capitán c_v → hay correspondencia 1 a 1
Por cada arista (u,v) en E se crea exactamente un inscripto i_(u,v) compatible solo con c_u y c_v → si alguno de esos capitanes es elegido, el inscripto queda cubierto, igual que la arista en Vertex Cover
Si existe un Vertex Cover de tamaño k → esos k vértices como capitanes cubren todos los inscriptos con m=k
Si Hackatón encuentra m capitanes que cubren todos los inscriptos → esos capitanes como vértices forman un Vertex Cover de tamaño k=m

La solución de uno implica solución del otro en ambos sentidos.


Como el problema es NP y es NPH, se concluye que el problema de Hackatón es NPC.

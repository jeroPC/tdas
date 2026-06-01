# Problemas Clásicos

- **Camino Hamiltoniano**: Buscás un camino que pase por todos los nodos del grafo exactamente una vez.

- **Ciclo Hamiltoniano**: Es lo mismo que el camino, pero con una condición extra: el último nodo del recorrido tiene que estar conectado con el primero, formando un ciclo cerrado que pasa por todos los nodos una vez.

- **Clique (o CFI)**: Buscás un subgrupo de $k$ nodos donde todos están conectados con todos, es decir, un subgrafo completo o "todos amigos entre sí".

- **Conjunto Independiente (CI)**: Todo lo contrario a Clique. Buscás un subgrupo de $k$ nodos donde ninguno está conectado con ninguno, es decir, completamente aislados.

- **Vertex Cover (VC - Cobertura de Vértices)**: Buscás un subgrupo de hasta $k$ nodos que "toquen" o cubran todas las aristas del grafo. No puede quedar ninguna arista sin al menos uno de sus extremos en tu subgrupo.

- **Mochila (Knapsack)**: Te dan objetos con pesos y valores, y un tope de peso $W$. Buscás un subgrupo de objetos que no supere el peso total $W$ y maximice el valor.
 
- ** En CFI (Conjunto Fuertemente Independiente), la restricción es más estricta: buscás un grupo de nodos $S$ tal que, para cualquier par de nodos $u, v \in S$, no solo no puede haber una arista directa entre ellos, sino que tampoco pueden compartir un vecino en común. Es decir, la distancia en pasos entre cualquier par de nodos elegidos en el grafo debe ser mayor a 2.


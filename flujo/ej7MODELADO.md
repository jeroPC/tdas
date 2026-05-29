# Resolución de Asignación de Custodia Policial mediante Redes de Flujo

Este módulo presenta la resolución teórica y el modelado algorítmico para el problema de asignación de custodia de comisarías a centros de actividades para eventos deportivos internacionales. La solución utiliza el algoritmo de **Flujo Máximo (Ford-Fulkerson / Edmonds-Karp)** sobre grafos bipartitos.

## 📋 Problema Base: 1 Centro = 1 Comisaría

### Modelado del Grafo
Para determinar si es posible realizar la asignación de forma que todos los centros estén custodiados, construimos una red de flujo dirigida y bipartita $G = (V, E)$:

* **Vértices ($V$):**
    * Un nodo fuente $S$ y un nodo sumidero $T$.
    * Un conjunto de $n$ nodos que representan a las **comisarías**.
    * Un conjunto de $m$ nodos que representan a los **centros de actividades**.
* **Aristas ($E$) y Capacidades ($C$):**
    * **Conexión de Entrada:** Se añade una arista desde $S$ hacia cada comisaría con **capacidad 1**. Esto modela que cada comisaría es un recurso único (puede custodiar a lo sumo un centro).
    * **Conexión Intermedia:** Se añade una arista dirigida desde una comisaría hacia un centro **sí y solo sí la distancia entre ambos es $\le d$**. Su capacidad se fija en **1**. Si la distancia supera el umbral $d$, la arista directamente no existe en el grafo.
    * **Conexión de Salida:** Se añade una arista desde cada centro hacia el sumidero $T$ con **capacidad 1**, indicando que cada centro requiere exactamente una comisaría.



### Semántica del Resultado
1. Al ejecutar el algoritmo de Flujo Máximo, el teorema de **integralidad del flujo** asegura que el flujo final por cada arista será entero (0 o 1). Cada unidad de flujo que viaja de $S$ a $T$ representa un emparejamiento válido.
2. **Criterio de Éxito:** Se calcula el flujo total que llega a $T$. Si el **Flujo Máximo $= m$** (la cantidad de centros), la asignación es **posible**. Si es menor, algún centro quedó sin cobertura debido a las restricciones de distancia.

---

## ── Modificación 1: Demanda Variable por Centro ($m_i$ comisarías)

### Modelado del Grafo
El esquema bipartito demuestra su flexibilidad requiriendo una única modificación en las aristas de salida hacia el sumidero:

* **Aristas de Entrada ($S \rightarrow$ Comisaría):** Mantienen **capacidad 1** (el recurso policial sigue siendo individual).
* **Aristas Intermedas (Comisaría $\rightarrow$ Centro):** Mantienen **capacidad 1** (obliga al algoritmo a seleccionar comisarías *distintas* para un mismo centro).
* **Aristas de Salida (Centro $i \rightarrow T$):** La capacidad de la arista del centro $i$ se define como **$m_i$** (la dotación específica de comisarías que requiere el centro).



### Semántica del Resultado
1. El nodo de cada centro funciona ahora como un acumulador que recibe en paralelo un flujo de 1 desde distintas comisarías habilitadas.
2. **Criterio de Éxito:** Definimos el **Flujo Objetivo** como la sumatoria de todos los requerimientos: $\sum_{i=1}^{m} m_i$. Al finalizar el algoritmo, si el **Flujo Máximo $=$ Flujo Objetivo**, la configuración es válida.

---

## ⚠️ Modificación 2: Restricción de Exclusión Mutua (Conflicto $N_i$ y $N_j$)

Si se añade la restricción de que dos comisarías específicas ($N_i$ y $N_j$) no pueden ser asignadas juntas a un mismo centro $M_i$, el problema cambia drásticamente de naturaleza.

### Impacto en la Resolución
* **Inviabilidad de Redes de Flujo:** Los algoritmos clásicos de Flujo Máximo **no pueden manejar restricciones condicionales entre aristas** (el flujo por una arista no puede alterar dinámicamente la capacidad de otra).
* **Alternativa de Modelado:** El problema debe reformularse mediante **Programación Lineal Entera (ILP)**. Definimos variables binarias $x_{c, com}$ (1 si la comisaría *com* se asigna al centro *c*, 0 si no) y agregamos la restricción:
    $$x_{M_i, N_i} + x_{M_i, N_j} \le 1$$

---

## ⏱️ Análisis de Eficiencia y Casos Críticos

| Escenario | Enfoque Algorítmico | Complejidad Temporal | ¿Cuándo deja de ser eficiente? |
| :--- | :--- | :--- | :--- |
| **Caso Base** | Edmonds-Karp (Flujo Máximo) | $O(V \cdot E^2)$ | Sólo ante un número astronómico de nodos (millones de centros/comisarías), inexistente en ciudades reales. |
| **Modificación 1** | Edmonds-Karp (Flujo Máximo) | $O(V \cdot E^2)$ | Se comporta igual que el caso base; el aumento de capacidades en el sumidero no penaliza el orden polinomial. |
| **Modificación 2** | Programación Lineal Entera (ILP) | Exponencial (NP-Hard) | **Deja de ser eficiente rápidamente** a medida que aumenta el número de comisarías en conflicto, requiriendo en la práctica el uso de heurísticas. |

---

## 🛠️ Implementación de Referencia (Python)

El siguiente código en pseudocódigo de Python ilustra el motor de cálculo y el envoltorio de validación para el **Caso Base**:

```python
def flujo_ford_fulkerson(grafo, s, t):
    """Calcula la red de flujos máximos desde un origen a un destino."""
    flujo = {}
    for v in grafo:
        for w in grafo.adyacentes(v):
            flujo[(v, w)] = 0
            
    grafo_residual = copiar(grafo)
    
    while (camino = obtener_camino(grafo_residual, s, t)) is not None:
        capacidad_residual_camino = min_peso(grafo_residual, camino)
        
        for i in range(1, len(camino)):
            u = camino[i-1]
            v = camino[i]
            
            if grafo.hay_arista(u, v):
                flujo[(u, v)] += capacidad_residual_camino
            else:
                flujo[(v, u)] -= capacidad_residual_camino
            
            actualizar_grafo_residual(grafo_residual, u, v, capacidad_residual_camino)
            
    return flujo

def verificar_custodia_centros(comisarias, centros, d):
    """Envoltorio que construye la red y evalúa la viabilidad del Caso Base."""
    # 1. Construcción del grafo bipartito aplicando el filtro de distancia 'd'
    grafo = armar_grafo_bipartito(comisarias, centros, d, caso=1)
    s, t = "Fuente", "Sumidero"
    
    # 2. Cómputo del flujo
    flujo_resultado = flujo_ford_fulkerson(grafo, s, t) 
    
    # 3. Cálculo del flujo máximo total saliente de la fuente
    flujo_maximo_total = sum(flujo_resultado[(s, vecino)] for vecino in grafo.adyacentes(s))
        
    # 4. Evaluación del flujo objetivo
    if flujo_maximo_total == len(centros):
        return "Es posible realizar la asignación"
    return "No es posible"
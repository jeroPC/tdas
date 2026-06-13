"""A raíz de una nueva regulación industrial un fabricante debe rotular cada lote que
produce según un valor numérico que lo caracteriza. Cada lote está conformado por “n”
piezas. A cada una de ellas se le realiza una medición de volumen. La regulación considera
que el lote es válido si más de la mitad de las piezas tienen el mismo volumen. En ese caso el
rótulo deberá ser ese valor. De lo contrario el lote se descarta. Actualmente cuenta con el
proceso “A” que consiste en para cada pieza del lote contar cuántas de las restantes tienen el
mismo volumen. Si alguna de las piezas corresponde al “elemento mayoritario”, lo rotula. De
lo contrario lo rechaza. Un consultor informático impulsa una solución (proceso “B”) que
considera la más eficiente: ordenar las piezas por volumen y con ello luego reducir el tiempo
de búsqueda del elemento mayoritario. Nos contratan para construir una solución mejor
(proceso “C”). Se pide:
a. Exprese mediante pseudocódigo el proceso “A”.
b. Explique si la sugerencia del consultor (proceso “B”) realmente puede mejorar el
proceso. En caso afirmativo, arme el pseudocódigo que lo ilustre.
c. Proponga el proceso “C” como un algoritmo superador mediante división y
conquista. Explíquelo detalladamente y brinde pseudocódigo"""

def de_2en_2(lote):
    # Caso base por si mandan un lote vacío o de 1
    if len(lote) == 0:
        return None
    if len(lote) == 1:
        return lote[0]
    
    # Creamos tu hash para acumular los puntos
    acumulador = crear_hash()
    
    # Restamos 1 al largo para evitar el error con los impares
    for i in range(0, len(lote) - 1, 2):
        if lote[i] == lote[i + 1]:
            # Sumamos un punto al elemento en el hash
            acumulador.agregar_o_incrementar(lote[i])
            
    # Si el hash quedó vacío, significa que ningún par fue igual
    if acumulador.esta_vacio():
        return None
        
    # Buscamos cuál fue el elemento que más puntos sumó
    ganador = acumulador.obtener_clave_con_maximo_valor()
    puntos = acumulador.obtener_valor(ganador)
    
    mitad = len(lote) // 2
   
    # Tu condición de corte: si los puntos superan la mitad de la mitad
    if puntos > (mitad // 2):
        return ganador  # DEVOLVEMOS EL ELEMENTO (RÓTULO), NO EL HASH
    
    return None


def version_recur(lote, izq, der):
    if izq == der:
        return lote[izq]

    mitad = izq + (der - izq) // 2

    candidato_izq = version_recur(lote, izq, mitad)
    candidato_der = version_recur(lote, mitad + 1, der)


    if candidato_izq == candidato_der:
        return candidato_izq
    
    cant_izq = ContarEnRango(lote, izq, der, cand_izq)
    cant_der =  ContarEnRango(lote, izq, der, cand_der)

    tamano_tramo = der - izq + 1

    if cant_izq > tamano_tramo // 2:
        return cand_izq
    if cant_der > tamano_tramo // 2:
        return cand_der
    
    return None




"""
================================================================================
TRAZA DE EJECUCIÓN (DEBUGGING MANUAL)
Lote de prueba: [20, 20, 20, 30] (Índices: 0 al 3)
Algoritmo: División y Conquista - Elemento Mayoritario
================================================================================

1. FASE DE BAJADA (Dividir hasta llegar a los Casos Base)
--------------------------------------------------------------------------------
El algoritmo calcula el punto medio en cada nivel y abre ramas en el árbol de 
llamadas recursivas sin comparar ningún dato, hasta que el tramo mide 1 (izq == der):

* Lote[0] es 20 (Caso base: izq=0, der=0) -> Retorna: 20
* Lote[1] es 20 (Caso base: izq=1, der=1) -> Retorna: 20
* Lote[2] es 20 (Caso base: izq=2, der=2) -> Retorna: 20
* Lote[3] es 30 (Caso base: izq=3, der=3) -> Retorna: 30


2. PRIMERA RONDA DE VUELTAS (Combinación de los Casos Base - Subtramos de tamaño 2)
--------------------------------------------------------------------------------
Las hojas del árbol empiezan a cerrarse. Se evalúan los tramos intermedios:

A) Subarreglo Izquierdo: [20, 20] (Rango: izq=0, der=1)
   - Recibe de sus hijos base: cand_izq = 20, cand_der = 20
   - Ejecuta: if cand_izq == cand_der: (¿20 == 20?) -> ¡VERDADERO!
   - Acción: Corta camino y retorna 20 hacia el nivel superior.
   - Nota: No gastó tiempo en contar a pata porque hubo acuerdo total.

B) Subarreglo Derecho: [20, 30] (Rango: izq=2, der=3)
   - Recibe de sus hijos base: cand_izq = 20, cand_der = 30
   - Ejecuta: if cand_izq == cand_der: (¿20 == 30?) -> FALSO.
   - Acción de desempate: Llama a contar_en_rango() únicamente en el tramo [20, 30]:
     * cant_izq (Ocurrencias de 20) = 1
     * cant_der (Ocurrencias de 30) = 1
   - Umbral de validación: tamano_tramo = (3 - 2 + 1) = 2. Mitad del tramo = 2 // 2 = 1.
   - Evalúa condiciones:
     * ¿cant_izq > 1? (¿1 > 1?) -> FALSO.
     * ¿cant_der > 1? (¿1 > 1?) -> FALSO.
   - Acción: Al no haber mayoría absoluta en su zona, retorna None hacia arriba.


3. SEGUNDA RONDA DE VUELTAS (Comparación de Niveles Superiores - Tramo Total de tamaño 4)
--------------------------------------------------------------------------------
Llegamos al nodo raíz del árbol (Rango general: izq=0, der=3). 
Acá NO se están comparando elementos del arreglo directamente, sino las respuestas 
filtradas que enviaron los bloques intermedios:

- cand_izq (Lo que devolvió el bloque izquierdo [20, 20]) = 20
- cand_der (Lo que devolvió el bloque derecho [20, 30])  = None

Ejecución del nivel supremo:
1. Ejecuta: if cand_izq == cand_der: (¿20 == None?) -> FALSO.
2. Acción de desempate: Como son distintos, se ve obligado a llamar a 
   contar_en_rango() sobre TODO el lote de punta a punta [20, 20, 20, 30]:
     * cant_izq (Ocurrencias de 20 en todo el lote) = 3
     * cant_der (Ocurrencias de None en todo el lote) = 0
3. Umbral de validación: tamano_tramo = (3 - 0 + 1) = 4. Mitad del tramo = 4 // 2 = 2.
4. Evalúa condiciones con la vara de su propio tamaño (superar los 2 votos):
     * ¿cant_izq > 2? (¿3 > 2?) -> ¡VERDADERO!
5. Resolución: Entra al IF, corta el flujo y ejecuta: return cand_izq

================================================================================
RESULTADO FINAL DE LA RECURSIÓN: El algoritmo retorna el número 20.
================================================================================
"""



Python
def buscar_candidato_parejas(lote):
    if len(lote) == 0:
        return None
    if len(lote) == 1:
        return lote[0]
    
    sobrevivientes = []
    
    # Recorremos de 2 en 2 con un FOR (saltando con el range)
    # n - 1 asegura que si el lote es impar, el último no tire error de rango
    n = len(lote)
    for i in range(0, n - 1, 2):
        if lote[i] == lote[i + 1]:
            sobrevivientes.append(lote[i])
            
    # Si el lote era impar, el último elemento se quedó sin pareja.
    # La regla matemática dice que sobrevive directo para mantener el balance.
    if n % 2 != 0:
        sobrevivientes.append(lote[-1])
        
    # --- CONQUISTA (Una sola llamada recursiva: T(n/2)) ---
    return buscar_candidato_parejas(sobrevivientes)

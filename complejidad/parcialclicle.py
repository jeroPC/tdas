"""
================================================================================
ENUNCIADO DEL PROBLEMA: CLASES DE COMPLEJIDAD
================================================================================
Se realizará un nuevo festival de música y nos contratarán para definir a los 
artistas convocados. Existen "n" posibles artistas. Contamos con un presupuesto 
de "p" pesos. Cada uno de los artistas tiene honorarios de contratación. Entre 
ciertos artistas existen relaciones de amistad. Deseamos contratar "r" artistas 
sin superar el presupuesto y que al menos entre ellos existan "a" relaciones de 
amistad para fomentar las colaboraciones. Demostrar que el problema es NP-C 
(utilizar el problema del Clique).
================================================================================
"""

# ==============================================================================
# BREVE EXPLICACIÓN DE CLIQUE (Problema conocido NP-C)
# ==============================================================================
# El problema del Clique toma como entrada un Grafo G = (V, E) y un entero 'k'.
# Pregunta si existe un subconjunto de 'k' vértices en G tales que estén TODOS
# conectados entre sí (es decir, que formen un grafo completo de tamaño k).
# Un clique de tamaño 'k' contiene exactamente la cantidad máxima de aristas 
# posibles para 'k' nodos, dada por la fórmula: k * (k - 1) / 2.


# ==============================================================================
# 1. DEMOSTRACIÓN DE QUE EL FESTIVAL DE MÚSICA (FM) PERTENECE A NP
# ==============================================================================
# Para demostrar que FM está en NP, definimos un Certificado (la solución propuesta)
# y un Verificador eficiente que corre en tiempo polinomial O(n^2).

def verificador_festival_musica(instancia_FM, certificado_C):
    """
    Instancia_FM: Contiene (n_artistas, grafo_amistades, lista_honorarios, p, r, a)
    Certificado_C: Un subconjunto de artistas propuesto (lista de nombres/IDs)
    """
    # JUSTIFICACIÓN DE PASOS Y COMPLEJIDAD:
    
    # Paso 1: Verificar que se hayan elegido exactamente 'r' artistas.
    # Operación de costo O(1) si conocemos el tamaño del certificado.
    if len(certificado_C) != instancia_FM.r:
        return False
        
    # Paso 2: Verificar que no se supere el presupuesto 'p'.
    # Iteramos sobre los 'r' artistas sumando sus honorarios. Costo: O(r).
    costo_total = 0
    for artista in certificado_C:
        costo_total += instancia_FM.lista_honorarios[artista]
        
    if costo_total > instancia_FM.p:
        return False
        
    # Paso 3: Verificar que existan al menos 'a' relaciones de amistad entre ellos.
    # Evaluamos cada par de artistas dentro del certificado C para contar las aristas.
    # Para 'r' artistas, hay r*(r-1)/2 pares posibles. En el peor caso (r = n), 
    # la complejidad de este doble bucle es O(n^2).
    amistades_internas = 0
    for i in range(len(certificado_C)):
        for j in range(i + 1, len(certificado_C)):
            u = certificado_C[i]
            v = certificado_C[j]
            if instancia_FM.grafo_amistades.existe_arista(u, v):
                amistades_internas += 1
                
    if amistades_internas < instancia_FM.a:
        return False
        
    # Si cumple todas las condiciones en tiempo O(n^2), el certificado es válido.
    return True

# CONCLUSIÓN DEL CERTIFICADOR:
# Como el verificador comprueba el certificado en tiempo polinomial O(n^2) respecto 
# al tamaño de la entrada, queda demostrado que el problema Festival de Música e NP.


# ==============================================================================
# 2. REDUCCIÓN: DEMOSTRAR QUE EL FESTIVAL DE MÚSICA ES NP-HARD (Clique <=p FM)
# ==============================================================================
# Queremos demostrar que si tuviéramos una función mágica de caja negra que resuelve
# nuestro problema del Festival de Música, podríamos resolver Clique en tiempo polinomial.

def resolver_clique_usando_caja_negra(grafo_G, k):
    # 1. Traducimos la planilla de Clique a los datos del Festival
    n_artistas = grafo_G.vertices
    grafo_amistades = copiar_estructura(grafo_G)
    lista_honorarios = {artista: 0 for artista in n_artistas}
    presupuesto_p = 0
    artistas_a_contratar_r = k
    amistades_minimas_a = (k * (k - 1)) // 2
    
    # 2. Le pasamos todos estos datos empaquetados a la CAJA NEGRA
    #    que sabe resolver el problema del Festival de Música
    resultado = caja_negra_festival_musica(
        n_artistas, grafo_amistades, lista_honorarios, 
        presupuesto_p, artistas_a_contratar_r, amistades_minimas_a
    )
    
    # 3. Lo que responda la caja negra (True o False) 
    #    es la respuesta exacta para nuestro problema del Clique
    return resultado

# JUSTIFICACIÓN DE COMPLEJIDAD DE LA REDUCCIÓN:
# Asignar los costos en 0 toma O(|V|) y copiar el grafo toma O(|V| + |E|). 
# Calcular las variables toma O(1). Toda la transformación se ejecuta en 
# tiempo polinomial O(n^2), cumpliendo las reglas de la reducción de Karp.


# ==============================================================================
# 3. JUSTIFICACIÓN DE EQUIVALENCIA (SI Y SOLO SI)
# ==============================================================================
"""
Para que la reducción sea válida, debemos demostrar que la instancia de Clique 
devuelve SÍ si y solo si la instancia construida de FM devuelve SÍ.

Demostración Ida (==>): Si el Grafo G tiene un Clique de tamaño 'k'.
Elegimos esos mismos 'k' vértices como los artistas para nuestro festival (r = k). 
Como todos los artistas cobran $0, el costo total es 0, lo cual no supera el 
presupuesto p = 0. Al formar un clique en G, esos 'k' artistas están todos 
conectados entre sí, sumando exactamente k*(k-1)/2 aristas. Como nuestra condición 
exige 'at menos' a = k*(k-1)/2 amistades, la condición se cumple. FM devuelve SÍ.

Demostración Vuelta (<==): Si el Festival de Música (FM) devuelve SÍ.
Significa que la caja negra encontró un subconjunto de r = k artistas que gastan 
menos de $0 (se cumple trivialmente) y que tienen 'al menos' a = k*(k-1)/2 
relaciones de amistad entre ellos. 
Matemáticamente, un conjunto de 'k' elementos puede tener como MÁXIMO k*(k-1)/2 
aristas en total. Si el enunciado nos dice que tiene 'al menos' esa cantidad, 
la única posibilidad matemática es que tenga EXACTAMENTE esa cantidad, lo que 
significa que todos los artistas seleccionados son amigos entre sí. Por lo tanto, 
esos mismos 'k' vértices forman un Clique en el Grafo G. Clique devuelve SÍ.

================================================================================
CONCLUSIÓN FINAL DEL EXAMEN:
Dado que demostramos que Festival de Música pertenece a la clase NP, y que el 
problema NP-Completo "Clique" se puede reducir en tiempo polinomial a nuestro 
problema (Clique <=p FM), se concluye formalmente que el problema del Festival 
de Música es NP-Completo (NP-C).
================================================================================
"""
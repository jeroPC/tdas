
La elaboración de una flota de “n” minisatélites requiere la integración de 4 componentes
cuyos códigos de identificación son pA, pB, pC y pD. Contamos con “n” piezas de cada uno de
ellos. Un estudio de compatibilidad informa que no cualquier cuadrupla de piezas es viable
para ensamblar el satélite. Nos proveen un listado de las cuadruplas que si pueden
conformarlos. Queremos saber si es posible seleccionar de forma adecuada las piezas para
armar los “n“ satélites. Se pide: Demostrar que el problema es NP-Completo. Sugerencia: Se
puede utilizar 3 Dimensional Matching


VerificarSatélites(Instancia(n, ListadoCompatibles), Certificado C):
    // 1. Verificar el tamaño del certificado
    Si tamaño(C) != n:
        Retornar FALSO

    // Crear conjuntos vacíos para registrar las piezas ya usadas
    Usados_pA = ConjuntoVacío()
    Usados_pB = ConjuntoVacío()
    Usados_pC = ConjuntoVacío()
    Usados_pD = ConjuntoVacío()

    // 2. Verificar cada cuadrúpla del certificado
    Para cada cuadrúple (a, b, c, d) en C:
        
        // Checkear si la combinación es legal según el listado original
        Si (a, b, c, d) no está en ListadoCompatibles:
            Retornar FALSO
        
        // Checkear si alguna pieza ya fue usada en otro satélite
        Si (a en Usados_pA) o (b en Usados_pB) o (c en Usados_pC) o (d en Usados_pD):
            Retornar FALSO
        
        // Registrar las piezas como usadas
        Agregar a a Usados_pA
        Agregar b a Usados_pB
        Agregar c a Usados_pC
        Agregar d a Usados_pD

    // Si pasó todos los controles para las n cuadrúplas
    Retornar VERDADERO

o(n * m)

Si tuviéramos una máquina (oráculo) capaz de resolver nuestro problema de los minisatélites en tiempo polinomial, podríamos usarla para resolver 3DM en tiempo polinomial.


Instancia de 3DM (X, Y, Z, Tripletas T)
        │
        ▼
┌─────────────────────────────────────────┐
│ Algoritmo de Reducción (Transformación) │ ◄── Esto lo diseñamos nosotros en O(polinomial)
└─────────────────────────────────────────┘
        │
        ▼
 Instancia de Satélites (pA, pB, pC, pD, Cuadrúplas C)
        │
        ▼
┌─────────────────────────────────────────┐
│   Solucionador del Problema Satélites   │ ◄── La "Máquina" que resuelve nuestro problema
└─────────────────────────────────────────┘
        │
        ▼
     SÍ / NO  ─────────────────────────────► Mismo resultado para la instancia de 3DM


Algoritmo Reduccion_3DM_a_Satelites(X, Y, Z, T):
    // Entrada: Conjuntos X, Y, Z de tamaño n. Conjunto de tripletas T.
    // Salida: Una instancia (n_sat, pA, pB, pC, pD, ListadoCompatibles)
    
    n_sat = tamaño(X)
    
    // Mapeo directo de componentes
    Componentes_pA = X
    Componentes_pB = Y
    Componentes_pC = Z
    
    // Creación del componente artificial (arandelas comodín)
    Componentes_pD = ConjuntoVacío()
    Para j desde 1 hasta n_sat:
        Crear elemento d_j
        Agregar d_j a Componentes_pD
        
    ListadoCompatibles = ConjuntoVacío()
    
    // Doble bucle: por cada tripleta legal, la combinamos con las n arandelas
    Para cada tripleta (x, y, z) en T:
        Para cada d_j en Componentes_pD:
            // Creamos la cuadrúpla y la sumamos al listado de satélites
            Agregar cuadrúpla (x, y, z, d_j) a ListadoCompatibles
            
    Retornar InstanciaSatelites(n_sat, Componentes_pA, Componentes_pB, Componentes_pC, Componentes_pD, ListadoCompatibles)


3dm < = satélites

3DM es un caso particular (más restringido) de tu problema.

Tu problema (Satélites) es una generalización (más amplia, de 4 dimensiones).

Si tenés una máquina que resuelve el problema difícil de 4 dimensiones, resolver el de 3 dimensiones es una papa: solo tenés que rellenar la cuarta dimensión con el truco de las arandelas comodín y pasárselo a la máquina.

Como 3DM ya es un problema NP-Completo (pesado, difícil de resolver), y demostraste que 3DM se puede transformar en el tuyo, estás probando que tu problema de los Satélites es como mínimo tan difícil como 3DM. Por lo tanto, tu problema también es NP-Completo.


Complejidad de la Reduccion (Transformacion)

Que analiza? 
El tiempo que tarda nuestro codigo en traducir la instancia de 3DM a la de Satelites.

Costo: 
O(|T| * n)

Por que: 
Tenemos un bucle que recorre cada una de las |T| tripletas de 3DM, y adentro un bucle interno que corre n veces para acoplarle las n arandelas comodin (d_1 ... d_n).

Peor caso (n^4): 
En el peor escenario posible, el numero de tripletas es maximo (|T| = n^3). Al multiplicarlo por el bucle interno de tamano n, nos da un techo de O(n^4).

Conclusion: 
Como n^4 es una funcion polinomial, la reduccion es valida y demuestra que el problema es NP-Hard.

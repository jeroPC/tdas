Ejemplo de Traza (Paso a Paso)
Supongamos un lote de 4 piezas con volúmenes: [7, 3, 7, 7].

División: Partimos el lote en [7, 3] y [7, 7].

Recursión (Lado Izquierdo [7, 3]):

Se divide en [7] y [3].

Como son casos base (1 solo elemento), devuelven sus valores.

Al comparar, son distintos. Contamos en el rango [7, 3]: el 7 aparece 1 vez, el 3 aparece 1 vez. Ninguno supera la mitad (que es > 1). Retorna NULO.

Recursión (Lado Derecho [7, 7]):

Se divide en [7] y [7].

Ambos devuelven 7. Como son iguales, el ganador de esta rama es 7.

Combinación Final:Tenemos candidatos: Izquierda = NULO, Derecha = 7.

Contamos cuántas veces aparece el 7 en el lote original [7, 3, 7, 7].

Aparece 3 veces. Como $3 > 4/2$, el resultado final es 7.


Algoritmo ElementoMayoritario(A, inicio, fin)
    // Caso Base: Un solo elemento siempre es mayoritario en su rango
    Si inicio == fin Entonces
        Retornar A[inicio]
    FinSi

    medio = (inicio + fin) / 2

    // DIVISIÓN Y CONQUISTA
    izq = ElementoMayoritario(A, inicio, medio)
    der = ElementoMayoritario(A, medio + 1, fin)

    // COMBINACIÓN
    // Si ambos coinciden, ese es el candidato indiscutido de este rango
    Si izq == der Entonces
        Retornar izq
    FinSi

    // Si son distintos, hay que contar para desempatar
    // Contamos cuántas veces aparece cada candidato en el rango actual
    cantIzq = ContarOcurrencias(A, inicio, fin, izq)
    cantDer = ContarOcurrencias(A, inicio, fin, der)

    // El que gane y supere la mitad del rango actual es el candidato
    tamanoRango = fin - inicio + 1
    Si cantIzq > tamanoRango / 2 Entonces
        Retornar izq
    Sino Si cantDer > tamanoRango / 2 Entonces
        Retornar der
    Sino
        Retornar NULO
    FinSi
FinAlgoritmo






















Algoritmo ElementoMayoritario(A, inicio, fin)
    // Caso Base: Un solo elemento siempre es mayoritario en su rango
    Si inicio == fin Entonces
        Retornar A[inicio]
   

    medio = (inicio + fin) / 2

    // DIVISIÓN Y CONQUISTA
    izq = ElementoMayoritario(A, inicio, medio)
    der = ElementoMayoritario(A, medio + 1, fin)

    // COMBINACIÓN
    // Si ambos coinciden, ese es el candidato indiscutido de este rango
    Si izq == der Entonces
        Retornar izq
  

    // Si son distintos, hay que contar para desempatar
    // Contamos cuántas veces aparece cada candidato en el rango actual
    cantIzq = ContarOcurrencias(A, inicio, fin, izq)
    cantDer = ContarOcurrencias(A, inicio, fin, der)

    // El que gane y supere la mitad del rango actual es el candidato
    tamanoRango = fin - inicio + 1
    Si cantIzq > tamanoRango / 2 Entonces
        Retornar izq
    Sino Si cantDer > tamanoRango / 2 Entonces
        Retornar der
    Sino
        Retornar NULO
    

FinAlgoritmo




Funcion ContarOcurrencias(A, inicio, fin, valor)
    // Si el valor que buscamos es nulo, no perdemos tiempo contando
    Si valor == NULO Entonces
        Retornar 0
    FinSi

    contador = 0
    // Recorremos solo el sub-rango indicado por la recursión
    Desde i = inicio Hasta fin Hacer
        Si A[i] == valor Entonces
            contador = contador + 1
        FinSi
    FinDesde

    Retornar contador
FinFuncion
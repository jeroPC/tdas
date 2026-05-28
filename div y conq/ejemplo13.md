### 3. Ejemplo de Ejecución y Seguimiento

Consideramos el siguiente vector ordenado de $n = 10$ votos y $o = 3$ opciones (`A`, `B`, `C`):

| Índice | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **Voto** | A | A | A | A | B | B | B | C | C | C |

#### Árbol de Ejecución (Pila de Llamadas)

El algoritmo procesa el vector profundizando siempre primero por la rama izquierda. A continuación se detalla el orden cronológico exacto en el que se activan y retornan las funciones:

```text
[Llamada Principal] contarVotosRec(0, 9)  --> V[0]='A', V[9]='C' (Distintos)
│
├──> [Paso 1] Entra a Izquierda: contarVotosRec(0, 4)  --> V[0]='A', V[4]='B' (Distintos)
│    │
│    ├──> [Paso 2] Entra a Izq-Izq: contarVotosRec(0, 2)  --> V[0]='A', V[2]='A'
│    │    └── [Base Hit] ¡Extremos Iguales! -> Registra: 3 votos para 'A' (Retorna)
│    │
│    └──> [Paso 3] Entra a Izq-Der: contarVotosRec(3, 4)  --> V[3]='A', V[4]='B' (Distintos)
│         │
│         ├──> [Paso 4] contarVotosRec(3, 3) --> V[3]='A'
│         │    └── [Base Hit] Caso base elemental -> Registra: 1 voto para 'A' (Retorna)
│         │
│         └──> [Paso 5] contarVotosRec(4, 4) --> V[4]='B'
│              └── [Base Hit] Caso base elemental -> Registra: 1 voto para 'B' (Retorna)
│
└──> [Paso 6] Entra a Derecha: contarVotosRec(5, 9)  --> V[5]='B', V[9]='C' (Distintos)
     │
     ├──> [Paso 7] Entra a Der-Izq: contarVotosRec(5, 7)  --> V[5]='B', V[7]='C' (Distintos)
     │    │
     │    ├──> [Paso 8] contarVotosRec(5, 6)  --> V[5]='B', V[6]='B'
     │    │    └── [Base Hit] ¡Extremos Iguales! -> Registra: 2 votos para 'B' (Retorna)
     │    │
     │    └──> [Paso 9] contarVotosRec(7, 7)  --> V[7]='C'
     │         └── [Base Hit] Caso base elemental -> Registra: 1 voto para 'C' (Retorna)
     │
     └──> [Paso 10] Entra a Der-Der: contarVotosRec(8, 9)  --> V[8]='C', V[9]='C'
          └── [Base Hit] ¡Extremos Iguales! -> Registra: 2 votos para 'C' (Retorna)

[Fin de la Ejecución] Cierra la llamada raíz (0, 9).
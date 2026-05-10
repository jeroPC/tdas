#tablero nxn 
#OBJETIVO = UBICAR MENOR CANTIDAD DE REINAS EN EL TABLERO DE MODO QUE PARA TODA CELDA EXISTA 
AL MENOS UNA REINA  QUE LA ATAQUE O QUE LA CELDA ESTA OCUPADA POR UNA REINA 

OSEA CADA REINA ATACA TODA CELDA QUE ESTA EN LA MISMA FILA, COLUMNA O DIAGONAL

MEJOR_SOLUCION = INFINITO
FUNC TODAS_CUABIERTAS(TABLERO,  ):

	PARA CADA (I,J) EN TABLERO :
		SI TABLERO[I][J] == 0:
			RETORNO FALSO
	RETORNO TRUE

FUNC BYB(TABLERO, CANTIDAD, POSICION_SIG):
	SI TODAS_CUABIERTAS(TABLERO):
		SI CANTIDAD < MEJOR_SOLUCION:
			MEJOR_SOLUCION = CANTIDAD
		return
	
	SI CANTIDAD >= MEJOR_SOLUCION:     //PODA
		RETURN
	
	PARA K DESDE POSICION_SIG HASTA N*N-1:
		PONER REINA EN CELDA K:
		BYB(TABLERO, CANTIDAD+1, K+1 )
		SACAR REINA DE CELDA K


FUNC PONER_REINA(TABLERO, R, C):
PARA I DESDE 0 HASTA N-1:
	PARA J DESDE 0 HASTA N-1:
		SI (I == R) OR (J == C) OR (|I-R| == |J-C|):
			TABLERO[I][J] += 1

FUNC SACAR_REINA(TABLERO, R, C):
    PARA I DESDE 0 HASTA N-1:
        PARA J DESDE 0 HASTA N-1:
            SI (I == R) OR (J == C) OR (|I-R| == |J-C|):
                TABLERO[I][J] -= 1



Sin poda  → O(N^(2·N²))   exponencial
Con poda  → depende del problema, 
            típicamente encuentra solución 
            óptima mucho antes


Entonces solo el stack, ¿cuántos frames apilados?
Cada frame corresponde a una reina colocada. La profundidad máxima es MEJOR_SOLUCION niveles, y en peor caso eso es N² niveles.
Nivel 0: BYB(celdaDesde=0)
Nivel 1: BYB(celdaDesde=k1+1)
Nivel 2: BYB(celdaDesde=k2+1)
...
Cada frame guarda solo: CANTIDAD, POSICION_SIG, K → O(1) por frame.
Entonces:
Espacial = O(N²) frames × O(1) por frame = O(N²)
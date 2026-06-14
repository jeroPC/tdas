"""Se realiza un experimento de conductividad de un nuevo material en aleación con
otro. Se formaron muestras numeradas de 1 a n. A mayor número, mayor concentración del
nuevo material. Además se realizaron “n” mediciones a diferentes temperaturas de
conductividad para cada muestra. Los resultados fueron expresados en una matriz M de
nxn. Se observa que un mismo material cuanto mayor temperatura tiene mayor
conductividad. Además, cuanto mayor concentración a la misma temperatura, también
mayor conductividad. En conclusión podemos, al analizar la matriz, ver dos progresiones.
Cada fila tiene números ordenados de forma creciente y cada columna tiene números
ordenados de forma creciente. Dada la matriz M, los experimentadores quieren encontrar
en qué posición se encuentra un determinado número. Proponga una solución utilizando
división y conquista."""


muestras de 1 a n 

mas cerca de n , mas concentracion del nuevo material
un material cuanto mayor temperatura tiene mayor
conductividad

n mediciones 

resultados = estan en M ==> matriz de nxn

Cada fila tiene números ordenados de forma creciente y cada columna tiene números
ordenados de forma creciente


los experimentadores quieren encontrar
en qué posición se encuentra un determinado número.



"""como resolverlo""". 

dividimos la matriz en 4 submatrices en cada paso 
1) buscamos el elemento que esta en el medio act
2) ####Si X == M[f_{medio}][c_{medio}]: ¡Encontrado! Devolvemos la posición.

####Si X < M[f_{medio}][c_{medio}]: Significa que X es menor que el centro. Por lo tanto, es imposible que 
X esté en el cuadrante inferior derecho (donde todos los números son aún mayores que el centro).El problema se reduce a buscar en los otros 3 cuadrantes restantes
 
#####Si X > M[f_{medio}][c_{medio}]: Significa que X es mayor que el centro. Por lo tanto, es imposible 
 que X esté en el cuadrante superior izquierdo (donde todos los números son menores). El problema se reduce a buscar en los otros 3 cuadrantes restantes.


def buscar_valor_Rec(matriz, fila_inicio, , col_fin, valor):
    if fila_inicio > len(matriz) or col_fin < len(matriz[0]):
        return "no encontrado"

    if matriz[fila_inicio][col_fin] == valor:
        return (fila_inicio, col_fin)
    
    elif matriz[fila_inicio][cola_fin] > valor:
        return buscar_valor_Rec(matriz , fila_inicio, col_fin-1, valor)
    else:
        return buscar_valor_Rec(matriz , fila_inicio+1, col_fin, valor)
    

T(N) = A * T(N/B) + O(N^C)

DONDE ACA A = CANTIDAD LLAMADA RECURSIVAS = 1 POR RECURSION 
B CANTIADAD QUE DIVIDO EL PROBLEMA , UNA FILA O COLUMNA ENTERA N -1 
N^C DONDE ES EL COSTO DE DIVIDIR Y COMBINAR C = 0 , TODO O (1). N ^0 = 1

NO SE PUEDE APLICAR TEOREMA MAESTRO , PORQUE NO DIVIDO EN CIERTA CANTIDAD, LA COMPLEJIDAD ES 
O(N)


version para poder aplicar teorema maestro

def buscar_cuadrantes(M, f_inicio, f_fin, c_inicio, c_fin, X):

    if f_inicio > f_fin or c_inico > c_fin:
        return "no encontrado"

    mitad_f = (f_inicio + f_fin) // 2
    mitad_c = (c_inicio + c_fin) // 2

    if matriz[mitad_f][mitad_c] == X:
        return (mitad_f, mitad_c)
    
    if matriz[mitad_f][mitad_c] > X:
        return buscar_cuadrantes(M, f_inicio, mitad_f -1 , c_inicio, mitad_c -1, X) #1re cuadrante
         buscar_cuadrantes(M, mitad_f, f_fin, c_inicio, mitad_c -1, X) # 3re cuadrante
         buscar_cuadrantes(M, f_inicio, mitad_f -1 , mitad_c, c_fin, X) # 2do cuadrante

    else:
        Retornar buscar_cuadrantes(M, f_medio + 1, f_fin, c_medio + 1, c_fin, X) o \
                 buscar_cuadrantes(M, f_inicio, f_medio, c_medio + 1, c_fin, X) o \
                 buscar_cuadrantes(M, f_medio + 1, f_fin, c_inicio, c_medio, X) 


T(N) = A * T(N/B) + O(N^C)
a = 3
b = 2 
n = 0


log b (a) = log 2 (3) = 1.585   
como 1,585 > c que es 0 , O(n^logb a ) ====> O(n^1,585) 
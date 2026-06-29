"""Un grupo de amigos que conviven están mudándose a un departamento nuevo. Han
juntado sus pertenencias en cajas de diferentes volúmenes que recolectaron en
supermercados y tiendas. Al llegar la compañía de mudanza les informan que por normativa
únicamente transportarán utilizando como contenedores sus recipientes de volumen V. Por
lo tanto, los amigos deben ingresar sus cajas en los contenedores autorizados. En el camión
entran como máximo “r” recipientes. Al llenarse realiza el trayecto para descargar y regresar
a cargar otros contenedores. Antes de proceder quieren saber si podrán acomodar todas
sus cajas de tal forma que puedan realizar menos de k viajes. Demostrar que es un
problema NP-Completo. Sugerencia: Este problema es fácilmente relacionable con Bin
Packing."""

Filas = Viajes del camión (un máximo de k-1 filas).Adentro de cada fila = Contenedores (un máximo de r contenedores por fila).Adentro de cada contenedor = Cajas/Pertenencias (cuyo volumen sumado no supere V).

certificacion: recibo una matriz en la cual las filas son la cantidad de 
viajes(contenedores), y las columnas las pertenencias con distintos volumenes

verificador : 

    si la cantidad de filas de la matriz > k : return false
    si en cada fila(contenedores) hay mas de r contenedores : return false
    si en algun contenedor se supera el volumen V permitido : return false

complejidad de las tres condiciones la mas costosa es la ultima del volumen , la cual
tiene tanto espacial como tmeporal o(N) siendo N el numero total de cajas

por lo tanto puedo afirmar que es e a los problemas np


reduccion :
 debo demostrar que el problema de bin-packing <= p problema de camion

 tomo una instancia generica del problema de bin-packing que es np-h y la traduzco al
 problema del camion que busco saber si es np-c


 bin-packing = /**
 * INSTANCIA DEL PROBLEMA: BIN PACKING (Problema de Decisión Conocido)
 * ------------------------------------------------------------------
 * Define los datos de entrada para el problema clásico de empaquetamiento.
 * * Parámetros:
 * - U : Conjunto de 'n' objetos disponibles. U = {u_1, u_2, ..., u_n}
 * - s : Función de tamaño/peso para cada objeto. s(u_i) -> Entero Positivo
 * - B : Capacidad máxima fija de cada contenedor (Bin). Entero Positivo
 * - K_bp : Cantidad máxima de contenedores permitidos. Entero Positivo
 * * Pregunta:
 * ¿Existe una partición de U en conjuntos disjuntos U_1, U_2, ..., U_m
 * tales que m <= K_bp, donde la suma de s(u) para todo u en U_j sea <= B 
 * para todo j de 1 a m? (Es decir, meter todo en <= K_bp bins sin desbordar B).
 */


 def reduccion_bin_packing_a_camion(lista_objetos, capacidad_bin, max_bins):
    # 1. TRADUCCIÓN (Tiempo polinomial O(n))
    # Las cajas del camión son exactamente los mismos volúmenes de Bin Packing
    cajas_camion = []
    for volumen in lista_objetos:
        cajas_camion.append(volumen)
        
    # Definimos las variables del problema del camión en base a Bin Packing
    V = capacidad_bin   # El volumen del recipiente es la capacidad del bin
    r = 1               # Truco: Entra solo 1 recipiente por viaje (1 Viaje = 1 Bin)
    k = max_bins + 1    # Menos de k viajes equivale a usar como máximo max_bins
    
    exito = caja_negra(cajas_camion, V, r, k)
    
    if exito == True:
        return True
    else:
        return False
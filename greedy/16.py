""". La república soberana de Antillense tiene su territorio en una isla paradisiaca. Los últimos
años sufrió grandes problemas de destrucción de su infraestructura luego del estallido de su
volcán, un terremoto, un maremoto y un ataque de mosquitos mutantes radioactivos. Entre
sus planes de reconstrucción deben unir mediante carreteras sus “n” poblaciones
principales. En un estudio previo conocen el costo de generar caminos desde cada uno de
los poblados hacia los otros. Como no tienen fondos deben solicitar préstamos. Desean
gastar el menor valor posible, construyendo la menor cantidad de rutas y al menor costo
total. Se debe tener en cuenta que únicamente se puede solicitar un préstamo por año para
construir una única ruta. Y que la inflación en el país hace que los costos de construcción
aumenten 100% . Debe indicar que rutas construir y en qué orden para lograr minimizar el
costo total. Presentar una solución greedy que solucione el problema"""


unir n poblaciones mediante carreteras 

conocen el costo de generar caminos desde cad uno de los poblados a otros 

deben solicitar prestamos 

gastar lo menos posible contruyedno menor cantidad de rutas y al menor costo total


[]------[]------[]
 |      |        |
 |      |        |
 \     []        []
  []




rutas_disponibles = [[a-b:500] , [b-c:50], [j-e:1000], [e-o:3]]
def elegir_rutas(rutas_disponibles):
    rutas_elegidas = []
    costo_total = 0
    año = 0
    
    rutas_ordenadas = mergesort_mayor_a_menor(rutas_disponibles)
    
    for ruta in rutas_ordenadas:
        rutas_elegidas.append(ruta)
        
        costo_total += ruta.costo * (2 ** año)
        
        año = año + 1

    return rutas_elegidas, costo_total

complejidad nlogn  , por el mergesort, que es lo cuentas, partir recursivamente, ordenar , y combinar

analisis de optimalidad = 


"""
================================================================================
ANÁLISIS DE LA SOLUCIÓN GREEDY: RECONSTRUCCIÓN DE ANTILLENSE
================================================================================


 EL CRITERIO GOLOSO (GREEDY): ORDENAMIENTO DE MAYOR A MENOR
--------------------------------------------------------------------------------
Una vez seleccionado el conjunto de n-1 rutas del MST, debemos determinar el 
orden cronológico de su construcción (un préstamo para una única ruta por año). 

La inflación en Antillense es del 100% anual, lo que significa que el costo de 
construcción sufre un impacto exponencial con el paso del tiempo. Si una ruta 
con costo base 'C' se construye en el año 't', su costo final indexado será:
    
    Costo_Final = C * (2^t)

La variable del tiempo (t) actúa como un exponente. Para minimizar el costo 
total acumulado, nuestra estrategia golosa dicta:
"Ordenar las rutas elegidas de MAYOR a MENOR costo base, absorbiendo los montos 
más altos en los primeros años (t bajos) cuando el impacto inflacionario es 
mínimo o nulo (2^0, 2^1), postergando las rutas baratas para los años tardíos."

"Mi estrategia Greedy es óptima porque se saca de encima las rutas más caras al principio. Si hiciera lo opuesto (empezar por lo barato),
 a mitad de camino la inflación del 100% anual habría duplicado tantas veces los precios que las rutas caras del final se volverían impagables,
disparando el costo total".
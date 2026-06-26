""". Una de las parejas más ricas del mundo está pasando por un proceso de divorcio. Entre
sus bienes cuentan con propiedades, autos, motos, estampillas raras y otros coleccionables.
Como no se ponen de acuerdo en la manera de dividirlos, el juez ha dictaminado que un
tasador ponga valor a cada bien y luego se haga una partición por valores iguales (el
problema abstracto se conoce como 2-partition) El juez nos pide que elaboremos un
algoritmo que en forma eficiente haga este trabajo. Demuestre que la solución pedida en
NP-completa. Sugerencia: Pruebe con “subset sum”."""

propiedades, autos, motos , estapillas, coleccionables

problema a plantear 2-partition

subset sum = existe algun subgrupo de numeros en la bolsa, que al sumarlos den el valor exacto de T

certificacion : recibo un subgrupo de con la posible division de bienes (C) una lista que dice
que se queda cada uno y ademas el informe del tasador

validacion : 
    ver la lista y determinar si la lista y el informe coinciden (bucle comparando): sino return false 
    Sumar todo, calcular la mitad y ver si el subconjunto suma exactamente eso.

def Verificar_Particion(Lista_Tasador, Subconjunto_C):
    Suma_Total = 0
    Suma_C = 0
    
    Para cada bien en Lista_Tasador:
        Suma_Total = Suma_Total + bien.valor
        
    Para cada objeto en Subconjunto_C:
        Si objeto no está en Lista_Tasador:
            Retornar FALSE 
        Suma_C = Suma_C + objeto.valor
        
    Mitad_Exacta = Suma_Total / 2
    Si Suma_C == Mitad_Exacta:
        Retornar TRUE
    Sino:
        Retornar FALSE

la complejidad de esto (comparar es o(n)) por lo tanto el problema de 2 partition pertenece a 
np



reduccion: 

    quiero determinar si subset-sum <= p 2-partition
def Reduccion_SS_a_2P(Lista_Original, Objetivo_T):
    S = 0
    Para cada numero en Lista_Original:
        S = S + numero
        
    X = S - (2 * Objetivo_T)
    
    Lista_Modificada = Copiar(Lista_Original)
    Agregar_Al_Final(Lista_Modificada, X)
    
    Resultado = Caja_Negra_2Partition(Lista_Modificada)
    
    Retornar Resultado

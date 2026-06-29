""". Para determinar si un número es primo existen varios algoritmos propuestos. Entre ellos
el test de Fermat. Este es un algoritmo randomizado que opera de la siguiente manera: Dado
un número entero “n”, seleccionar de forma aleatoria un número entero “a” coprimo a n.
Calcular an-1 módulo n. Si el resultado es diferente a 1, entonces el número “n” es
compuesto. La parte central de esta operatoria es la potenciación. Podríamos
algorítmicamente realizarla de la siguiente manera:
pot = 1
Desde i=1 a n-1
pot = pot * a
En este caso se realizan o(n) multiplicaciones. Proponga un método usando división y
conquista que resuelva la potenciación con menor complejidad temporal."""

me dan un numero n , seleccionar si un numero entero a 

def es_primo(a, n ):
    if n == 0 :
        return 1
    
    subproblema = es_primo(a, n/2)

    if n es par :
        return = subproblema * subproblema
    else:
        return = subproblema * subproblem * a


    


def potencia_modular(base, exp, mod):
    # Caso base: cualquier número elevado a 0 es 1
    if exp == 0:
        return 1
    
    # Paso de División y Conquista: resolvemos para la mitad del exponente
    subproblema = potencia_modular(base, exp // 2, mod)
    
    # Elevar al cuadrado el resultado del subproblema aplicando el módulo
    resultado = (subproblema * subproblema) % mod
    
    # Si el exponente era impar, multiplicamos una vez más por la base
    if exp % 2 != 0:
        resultado = (resultado * base) % mod
        
    return resultado



complejidad = O(log n)


teorema maestro = t(n) = a * t(n/b) + o(n^c )

donde a cantidad lllamada recursivas = 1 
b , division del subproblema = 2 
c = costo combinar y dividir, n^0 = 1 , c = 0


por lo tanto si log b (a) = log(n^c log b (a)) ===> O(log n)
n productos---> cada producto i tiene  tamaño= si valor_envio = vi 

tenemos k contenedores identicos ---cada uno --> capacidad = c


condicion =  Un producto debe asignarse a lo sumo a un contenedor (puede decidir no enviarlo)
condicion = La suma de los tamaños de los productos dentro de un mismo contenedor no puede superar su capacidad
condicion = despacho de un contenedor con espacio vacío es penalizado económicamente mediante un factor “a” 
            (valor por unidad de espacio no utilizado)
condicion = La penalización se aplica únicamente sobre los contenedores que contienen al menos un producto.


objetivo = Nos solicitan maximizar el valor total enviado (ganancia por los productos enviados menos la penalización de los espacios libres en los contenedores utilizados).


 ------------ Variables globales -------------------------
Elementos: lista de n productos ordenados por valor/tamaño DESC
K: cantidad de contenedores
C: capacidad de cada contenedor
A: penalización por unidad de espacio libre

mejorGanancia    = -infinito
mejorAsignacion  = {}
asignacionActual = {}


 ─── Estado inicial -------------------------────
espacioLibre[1..K] = C para todo contenedor
contenedoresUsados = {}

Resolver(nro=1, gananciaActual=0, espacioLibre, contenedoresUsados)


-------------------------──────────────────────
Resolver(nro, gananciaActual, espacioLibre, contenedoresUsados):

    // PODA: si la mejor ganancia posible desde aquí no supera
    //       la mejor encontrada hasta ahora, abandonar esta rama
    Si cotaSuperior(nro, gananciaActual, espacioLibre) <= mejorGanancia:
        retornar

    // CASO BASE: ya se decidió sobre todos los productos
    Si nro == n+1:
        Si gananciaActual > mejorGanancia:
            mejorGanancia   = gananciaActual
            mejorAsignacion = copia de asignacionActual
        retornar

    productoActual = Elementos[nro]

    // ── RAMA "no enviar": el producto actual se descarta ──
    Resolver(nro+1, gananciaActual, espacioLibre, contenedoresUsados)

    // ── RAMAS "asignar": una por cada contenedor ──
    Para cada contenedor c en 1..K:
        Si productoActual.tamaño <= espacioLibre[c]:

            // calcular cómo cambia la ganancia al meter este producto en c
            espacioAntesDeC     = espacioLibre[c]
            cUsadoAntes         = (c está en contenedoresUsados)

            nuevaGanancia       = gananciaActual + productoActual.valor

            Si c ya estaba usado:
                // el espacio libre de c ya penalizaba, ahora penaliza menos
                nuevaGanancia = nuevaGanancia + espacioAntesDeC * A - (espacioAntesDeC - productoActual.tamaño) * A
            Sino:
                // c pasa a usarse: aparece penalización por su espacio libre restante
                nuevaGanancia = nuevaGanancia - (espacioAntesDeC - productoActual.tamaño) * A

            
            Registrar productoActual → c en asignacionActual
            espacioLibre[c]    = espacioAntesDeC - productoActual.tamaño
            Agregar c a contenedoresUsados

            Resolver(nro+1, nuevaGanancia, espacioLibre, contenedoresUsados)

            // deshacer cambios 
            Quitar productoActual de asignacionActual
            espacioLibre[c] = espacioAntesDeC
            Si c no estaba usado antes: quitarlo de contenedoresUsados





-------------------------
cotaSuperior(nro, gananciaActual, espacioLibre):

    // Estimación optimista: productos restantes se reparten
    // se fracciona en todo el espacio libre, penalización = 0

    Sea espacioDisponible la suma del espacioLibre de todos los contenedores
    Sea cota igual a gananciaActual

    Recorrer productos no decididos desde nro hasta n:
        Si el producto cabe completo en espacioDisponible:
            Sumar su valor completo a cota
            Descontar su tamaño de espacioDisponible
        
    retornar cota


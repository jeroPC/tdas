ArmarRedResidual(G, f, c):
  Gf = grafo vacío con los mismos vértices de G
  
  PARA CADA arista (u,v) en G:
    SI c(u,v) - f(u,v) > 0:
      agregar arista (u→v) con capacidad c(u,v) - f(u,v)
    SI f(u,v) > 0:
      agregar arista (v→u) con capacidad f(u,v)
  
  RETORNAR Gf


FordFulkerson(Gf, s, t):
  flujo_total = 0

  MIENTRAS exista camino P de s a t en Gf:  // DFS/BFS
    bottleneck = mínima capacidad en P
    flujo_total += bottleneck
    
    PARA CADA arista (u,v) en P:
      Gf(u,v) -= bottleneck   // reducís hacia adelante
      Gf(v,u) += bottleneck   // aumentás hacia atrás
  
  RETORNAR flujo_total, Gf



ActualizarFlujo(G, f, c, u, v, c_nueva, s, t):

  // Armamos la red residual con el flujo actual
  Gf = ArmarRedResidual(G, f, c)

  // CASO A: capacidad aumenta
  SI c_nueva > c(u,v):
    Gf(u,v) += c_nueva - c(u,v)    // actualizamos capacidad residual
    FordFulkerson(Gf, s, t)         // buscamos nuevos caminos s→t

  // CASO B: capacidad disminuye
  SINO SI c_nueva < c(u,v):
    
    // Subcaso B1: el flujo sigue siendo válido
    SI f(u,v) <= c_nueva:
      Gf(u,v) -= c(u,v) - c_nueva  // solo ajustamos el residual
    
    // Subcaso B2: el flujo excede la nueva capacidad
    SINO:
      exceso = f(u,v) - c_nueva
      f(u,v) = c_nueva              // forzamos flujo al nuevo máximo

      // Paso 1: devolver exceso de u hacia s
      camino_u = buscarCamino(Gf, u, s)
      empujar exceso por camino_u
      actualizar Gf

      // Paso 2: reequilibrar v desde t
      camino_v = buscarCamino(Gf, t, v)
      empujar exceso por camino_v
      actualizar Gf

      // Paso 3: recuperar flujo máximo
      FordFulkerson(Gf, s, t)

  RETORNAR Gf
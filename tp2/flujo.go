Función ACTUALIZAR_SERVIDOR(G, G_f, f, F_total, id_servidor, c_nueva, bandas, plataformas, banda_servidor, servidor_plataforma):
    u = "S_in_" + id_servidor
    v = "S_out_" + id_servidor
    c_ant = Capacidad original de la arista (u, v) en G
    f_actual = f[(u, v)]

    G.cambiar_peso(u, v, c_nueva)

    // CASO 1: AUMENTO DE CAPACIDAD:
    Si c_nueva >= c_ant:
        delta = c_nueva - c_ant
        Si G_f.hay_arista(u, v):
            G_f.cambiar_peso(u, v, G_f.peso(u, v) + delta)
        Sino:
            G_f.agregar_arista(u, v, delta)

    // CASO 2: DISMINUCIÓN DE CAPACIDAD
    Sino:
        Si f_actual > c_nueva:
            exceso = f_actual - c_nueva

            // Cancelar exceso hacia la fuente (retroceder flujo entrante)
            rem_fuente = exceso
            Mientras rem_fuente > 0:
                cancelado = CANCELAR_FLUJO_CAMINO(G_f, f, origen=S, destino=u, rem_fuente)
                rem_fuente = rem_fuente - cancelado

            // Cancelar exceso hacia el sumidero (descontar flujo saliente)
            rem_sumidero = exceso
            Mientras rem_sumidero > 0:
                cancelado = CANCELAR_FLUJO_CAMINO(G_f, f, origen=v, destino=T, rem_sumidero)
                rem_sumidero = rem_sumidero - cancelado

            // Ajustar el flujo de la arista crítica y el total
            f[(u, v)] = f[(u, v)] - exceso
            F_total = F_total - exceso

            // Actualizar la arista de retorno en G_f
            peso_retorno = G_f.peso(v, u)
            Si peso_retorno == exceso:
                G_f.remover_arista(v, u)
            Sino:
                G_f.cambiar_peso(v, u, peso_retorno - exceso)

        Sino:
            // Subcaso donde el flujo no supera la nueva cota
            delta = c_ant - c_nueva
            peso_res = G_f.peso(u, v)
            Si peso_res == delta:
                G_f.remover_arista(u, v)
            Sino:
                G_f.cambiar_peso(u, v, peso_res - delta)

    //(Búsqueda de caminos de aumento
    Mientras exista camino p = BFS(G_f, S, T):
        botella = MIN_PESO(G_f, p)
        F_total = F_total + botella
        AUMENTAR_CAMINO(G, G_f, f, p, botella)

    demanda_total = SUMATORIA(bx para cada (_, bx) en bandas)
    posible = (F_total == demanda_total)
    asignacion = RECONSTRUIR_ASIGNACION(f, bandas, plataformas, banda_servidor, servidor_plataforma)

    Retornar (posible, F_total, asignacion)
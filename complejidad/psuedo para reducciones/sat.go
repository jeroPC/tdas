certificador_SAT(formula, evidencia_variables):
    # Recorremos todas las cláusulas de la fórmula
    for clausula in formula.clausulas:
        clausula_satisfecha = False
        
        # Evaluamos los literales de la cláusula
        for literal in clausula:
            valor_actual = evidencia_variables[literal.variable]
            # Si el literal está negado, invertimos su valor
            if literal.esta_negado:
                valor_actual = not valor_actual
                
            if valor_actual == True:
                clausula_satisfecha = True
                break # Con un solo True, la cláusula entera es True
                
        # Si revisamos la cláusula y ningún literal fue True:
        if clausula_satisfecha == False:
            return "Fórmula no satisfecha" # [33]
            
    return "Fórmula satisfecha" # Complejidad O(n*k) [36]
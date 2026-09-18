# Joaco
"""
Módulo para evaluar si un cliente aplica o no a un préstamo
según las reglas establecidas.
"""
def evaluar_prestamo(salario, monto, plazo):
    if salario < 8000:
        return False, "Rechazado: El salario mínimo debe ser de C$ 8,000."
    
    elif monto > (salario * 5):
        return False, f"Rechazado: El monto máximo permitido para tu salario es de C${salario * 5:,.2f}."
    
    elif plazo != 12 and plazo != 24 and plazo != 36:
        return False, "Rechazado: El plazo debe ser de 12, 24 o 36 meses."
    
    else:
        return True, "Aprobado: Cumples con todos los criterios para el préstamo."
def calcular_intereses(monto, plazo):
    tasa = 0.10
    años = plazo / 12

    interes = monto * tasa * años

    return interes


def calcular_total(monto, interes):
    total = monto + interes

    return total


def calcular_cuota(total, plazo):
    cuota = total / plazo

    return cuota
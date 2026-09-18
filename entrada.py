# Kenneth
def ingresar_datos():

    nombre = input("Ingrese el nombre del solicitante: ")

    while True:
        try:
            salario = float(input("Ingrese el salario mensual: "))

            if salario > 0:
                break
            else:
                print("El salario debe ser mayor que 0.")

        except ValueError:
            print("Debe ingresar un número válido.")


    while True:
        try:
            monto = float(input("Ingrese el monto del préstamo: "))

            if monto > 0:
                break
            else:
                print("El monto debe ser mayor que 0.")

        except ValueError:
            print("Debe ingresar un número válido.")


    while True:
        try:
            plazo = int(input("Ingrese el plazo (12, 24 o 36 meses): "))

            if plazo == 12 or plazo == 24 or plazo == 36:
                break
            else:
                print("El plazo debe ser de 12, 24 o 36 meses.")

        except ValueError:
            print("Debe ingresar un número entero.")


    return nombre, salario, monto, plazo
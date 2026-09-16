def obtener_nombre():
    nombre = input("Ingrese el nombre del solicitante: ")
    return nombre

def obtener_salario():
    while True:
        try:
            salario = float(input("Ingrese el salario mensual: "))

            if salario > 0:
                return salario
            else:
                print("Error: el salario debe ser mayor que 0.")

        except ValueError:
            print("Error: debe ingresar un número válido.")
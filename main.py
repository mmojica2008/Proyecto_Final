# Marcelo Mcrea

# ===============================================
# SISTEMA DE PRÉSTAMOS - COOPERATIVA
# Archivo principal: main.py
# ===============================================

#Importamos las funciones de los otros módulos
from entrada import ingresar_datos
from calculos import calcular_intereses, calcular_total, calcular_cuota
from evaluacion import evaluar_prestamo

def main():
    
    print("======================================")
    print("      COOPERATIVA- PRÉSTAMOS")
    print("======================================")
    print("EVALUACIÓN INICIAL DE SOLICITUD DE PRÉSTAMO")
    print()
    
    
    try: 
        # ---------------------------------
        # 1. Ingreso de datos
        # ---------------------------------
        nombre, salario, monto, plazo = ingresar_datos()
        
        
        # --------------------------------
        # 2. Realizar cálculos
        # --------------------------------
        interes = calcular_intereses(monto, plazo)
        total_pagar = calcular_total(monto, interes)
        cuota = calcular_cuota(total_pagar, plazo)
        
        
        # -------------------------------
        # 3. Evaluar solicitud
        # -------------------------------
        aprobado, resultado = evaluar_prestamo(salario, monto, plazo)
        
        
        # --------------------------------
        # 4. Mostrar resultados
        # --------------------------------
        print()
        print("======================================")
        print("        Resultado de la solicitud")
        print("======================================")
        
        print(f"Solicitante: {nombre}")
        print(f"Salario mensual: C$ {salario:.2f}")
        print(f"Monto solicitado: C$ {monto:.2f}")
        print(f"Plazo: {plazo} meses")
        print(f"Intereses: C$ {interes:.2f}")
        print(f"Total a pagar: C$ {total_pagar:.2f}")
        print(f"Cuota estimada: C$ {cuota:.2f}")
        
        print("-------------------------------------")
        print(f"Evaluación: {resultado}")
        print("======================================")
        
    except ValueError:
        print()
        print("Error: se ingresó un valor incorrecto.")
        
    except Exception as error:
        print()
        print(f"Ocurrió un error: {error}")
        
        
    finally:
        print()
        print("Fin de la evaluación.")
        
        
# =============================================
# Inicio del programa
# =============================================
        
if __name__ == "__main__":
    main()
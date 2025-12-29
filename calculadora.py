# pide al usuario una operacion (suma, resta, multiplicacion, division) y dos números
operacion = input("Ingrese la operacion: ")
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
# muestra el resultado
# debe repetirse hasta que el usuario escriba "salir" como operacion
while operacion != "salir":
    if operacion == "suma":
        resultado = numero1 + numero2
    elif operacion == "resta":
        resultado = numero1 - numero2
    elif operacion == "multiplicacion":
        resultado = numero1 * numero2
    elif operacion == "division":
        if numero2 == 0:
            print("Error: No se puede dividir por cero")
            operacion = input("Ingrese la operacion: ")
            continue
        resultado = numero1 / numero2
    print("El resultado es:", resultado)
    operacion = input("Ingrese la operacion: ")
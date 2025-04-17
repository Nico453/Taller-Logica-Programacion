def operacion(simbolo, valor1, valor2):
    total = 0
    match simbolo:
        case "+":
            total = valor1 + valor2
        case "-":
            total = valor1 - valor2
        case "*":
            total = valor1 * valor2
        case "/":
            total = valor1 / valor2
        case _:
            print("Operación no válida")
            return 0
    return total

simbolo = input("Introduce la operacion a realizar: ")
valor1 = int(input("ingrese primer valor: "))
valor2 = int(input("ingrese segundo valor: "))

total = operacion(simbolo, valor1, valor2)
print("El total a pagar es: ", total)


#probando git
#probando git 2
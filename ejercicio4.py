
''''
def propina(monto, seleccion):
    if seleccion == 1:
        propina = monto * 0.10
    elif seleccion == 2:
        propina = monto * 0.15
    elif seleccion == 3:
        propina = monto * 0.20
    elif seleccion == 4:
        propina = int(input("Introduce el porcentaje de propina: ")) / 100 * monto
    else:
        print("Opción no válida")
        propina = 0
    return propina
'''
def propina(monto, seleccion):
    match seleccion:
        case 1:
            propina = monto * 0.10
        case 2:
            propina = monto * 0.15
        case 3:
            propina = monto * 0.20
        case 4:
            propina = int(input("Introduce el porcentaje de propina: ")) / 100 * monto
        case _:
            print("Opción no válida")
    return propina

monto = int(input("Introduce el monto a pagar: "))
seleccion = int(input("Selecciona la propina:\n1. 10%\n2. 15%\n3. 20%\n4. Otro\n"))
total = propina(monto, seleccion)
print("El total a pagar es: ", monto + total)
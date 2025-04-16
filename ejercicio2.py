import random

number = random.randint(1, 10)
x = int(input("Introduce un número entre 1 y 10: "))

intentos = 0
while number != x :
    if number > x:
        print("El número es mayor")
    else:
        print("El número es menor")
    x = int(input("Introduce otro número entre 1 y 10: "))
else:
    print("Numero correcto")

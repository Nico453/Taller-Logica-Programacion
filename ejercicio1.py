
a= int(input("Introduce un número: "))
b= int(input("Introduce otro número: "))
c= int(input("Introduce otro número: "))

if a > b and a > c:
    print(f"El número mayor es: {a}")
elif b > a and b > c:
    print(f"El número mayor es: {b}")
elif c > a and c > b:
    print(f"El número mayor es: {c}")
else:
    print("Hay números iguales")
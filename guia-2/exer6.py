# a) Escribir en papel un programa que pida al usuario dos números, y que muestre en
# pantalla al mayor de ambos. Luego hacer 3 corridas de escritorio, luego pasarlo a
# Python y por último correr el programa con los valores iniciales de las corridas y
# vericar que funciona como se esperaba.
# b) Ídem anterior pero para encontrar el menor

a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print("A es el mayor")
    if b < c:
        print("B es el menor")
    else:
        print("C es el menor")
elif b > a and b > c:
    print("B es el mayor")
    if a < c:
        print("A es el menor")
    else:
        print("C es el menor")
else:
    if a < b:
        print("A es el menor")
    else:
        print("B es el menor")
    print("C es el mayor")
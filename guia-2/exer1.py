"""
Hacer en papel y luego en Python un programa que pida un entero entre 1 y 10, utilizando el
mensaje Adiviná en qué número estoy pensando!, y muestre Adivinaste si el usuario ingresa
el número 7.
"""

print("===> Adivina en que numero estoy pensando... <===")
print("===> Ingresa un numero entero del 0 al 10")
x = int(input())

if(x == 7):
    print("Correcto")
else:
    print("Incorrecto")

print("Gracias por participar")

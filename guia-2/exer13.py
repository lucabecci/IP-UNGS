# Escribir un programa que pida al usuario dos enteros y que luego muestre si el primero es
# mayor que el segundo o viceversa.

a = int(input())
b = int(input())

if a < 0 or b < 0:
    print("Por favor ingrese enteros = N")

if a > b:
    print("A es mayor que B")
elif b > a:
    print("B es mayor que A")

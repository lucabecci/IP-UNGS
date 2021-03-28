# Se desea escribir un programa que pida al usuario tres números y luego muestre el mayor de
# ellos. Escribir el programa en papel, realizar 3 pruebas de escritorio y luego pasarlo a Python y
# vericar los resutlados.

a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print("A es el mayor")
elif b > a and b > c:
    print("B es el mayor")
else:
    print("C es el mayor")

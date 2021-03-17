"""
Este programa chequea una serie de condiciones para los tres valores ingresados por el usuario.
Correrlo tal cual está en Python. Luego reemplazar donde dice True por una expresión lógica
que sea True o False según corresponda, en lugar de siempre True como ahora.
"""

a = int(input("Ingrese un numero entero"))
b = int(input("Ingrese un numero entero"))
c = int(input("Ingrese un numero entero"))
print("Usted ingresó los valores: ", a, b, c)
if (a > b):
    print(a, "es mayor que", b)

if (a == b):
    print(a, "y", b, "son iguales")

if (a > b and a > c):
    print(a, "es el mayor de todos")

if (b < a and b < c):
    print(b, "es el menor de todos")

if (a > b or a > c):
    print(a, "mayor que alguno de los otros dos")
elif (a <= b or a <= c):
    print(a, "es menor o igual que alguno de los otros dos")

if(a == b and a == c and b == c):
    print("Los tres numeros son iguales")
elif(a != b and b != c and c != a):
    print("Los tres numeros son distintos")

if(a % 2 == 0):
    print(a, "es par")

if(a % 2 != 0 and b % 2 != 0 and c % 2 != 0):
    print("Ninguno es par")

if(a % 2 == 0 and b % 2 == 0 and c % 2 == 0):
    print("Todos son pares")

if (a % 3 == 0):
    print(a, "es multiplo de 3")

if (a % 3 == 0 and a % 5 == 0):
    print(a, "es multiplo de 3 y 5")

if (a % 3 == 0 and a / 2 == 0):
    print(a, "es multiplo de 3 y par")

if(a - b > 0):
    print(a, "-", b, "da un numero positivo")


if((a - b) % 2 > 0):
    print(a, "-", b, "da un numero par positivo")
# //to change
# print(a, "es mayor que", b, True)
# print(a, "y", b, "son iguales", True)
# print(a, "es el mayor de todos", True)
# print(b, "es el menor de todos", True)
# print(a, "es mayor que alguno de los otros dos", True)
# print(a, "es menor o igual que alguno de los otros dos", True)
# print("Los tres numeros son iguales", True)
# print("Los tres numeros son distintos", True)
# print(a, "es par", True)
# print("alguno es par", True)
# print("ninguno es par", True)
# print("todos son pares", True)
# print(a, "es multiplo de 3", True)
# print(a, "es multiplo de 3 y de 5", True)
# print(a, "es multiplo de 3 y par", True)
# print(a, "-", b, "da un numero positivo", True)
# print(a, "-", b, "da un numero par positivo", True)

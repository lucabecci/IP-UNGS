# Escribir en papel un programa que tome un número entero positivo ingresado por el usuario
# y muestre por pantalla Usted ingresó un número de una sola cifra o Usted ingresó un número
# de más de una cifra según corresponda. Realizar 4 corridas de escritorio, escribirlo en Python
# y luego correrlo en la computadora con los valores iniciales de las corridas y vericar que hayan
# dado como se esperaba.

n = int(input())

if n < 0:
    print("Por favor ingrese un numero entero")
else:
    if n < 10 and n >= 0:
        print("Usted ingreso un numero de una sola cifra")
    else:
        print("Usted un numero de mas de una cifra")

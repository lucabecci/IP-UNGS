#Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla la cantidad de divisores de n.

print("===> Ingrese N:")
n = int(input())

count = 0

for x in range(1, n+1):
    if n % x == 0:
        count = count + 1

print("===>", count)

#Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla la suma de los divisores de n.

n = int(input("===> Ingrese N:"))
sum = 0
for x in range(1, n+1):
    if n % x == 0:
        sum = sum + x

print(sum)

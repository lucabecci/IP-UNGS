#Hacer un programa que permita al usuario elegir un 
#número positivo n y luego
#muestre en pantalla todos los divisores de n.

print("===> Ingrese N:")
n = int(input())
i = 1

while i <= n :
    if n % i == 0:
        print(i)
    i = i + 1


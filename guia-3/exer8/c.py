#) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
#potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27
#256.

print("===> Ingrese N:")
n = int(input())
i = 1
while i <= n:
    print(i ** i)
    i = i + 1


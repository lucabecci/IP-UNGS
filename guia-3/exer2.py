# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el
# 7 (4, 5, 6 y 7).
# b) Hacer un programa que permita al usuario elegir un número m y un n y luego
# muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n). ¾Qué pasa
# si n es menor que m?

print("===> Ingrese su M numero: ")
m = int(input())
print("===> Ingrese su N numero: ")
n = int(input())

if n < m:
    print("Por favor ingrese un N mayor que M para el ciclo")
else:
    for i in range(m+1, n):
        print(i)

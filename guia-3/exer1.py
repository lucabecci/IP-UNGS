# a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales
# (1, 2, 3, 4 y 5).
# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# primeros n números naturales (1, 2, · · · , n).

print("===> Ingrese un numero para el alcance maximo a mostrar: ")
n = int(input())

for i in range(0, n+1):
    print("===>", i)

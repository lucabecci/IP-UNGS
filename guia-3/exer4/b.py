# ) Hacer un programa que permita al usuario elegir un número m y un n y luego
# muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el
# usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar
# 2, 5, 8, 11, 14

print("==> Inserte N para inicio del ciclo:")
n = int(input())
print("===> Inserte M para el fin del ciclo:")
m = int(input())

for x in range(n, m+1, 3):
    print(x)

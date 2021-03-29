# Hacer un programa que permita al usuario elegir un número n, un m y un p y
# luego muestre todos los naturales entre m y n, pero salteando de a p números. Por
# ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
# el programa deberá mostrar 2, 6, 10, 14

print("==> Inserte N para inicio del ciclo:")
n = int(input())
print("===> Inserte M para el fin del ciclo:")
m = int(input())
print("===> Inserte P para el numero de saltos del ciclo:")
p = int(input())

if m < n:
    print("M debe ser mayor que N, intente otra vez con valores corretos.")
else:
    for x in range(n, (m+1), p):
        print("===>", x)

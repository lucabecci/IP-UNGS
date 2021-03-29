# Hacer un programa que permita al usuario elegir un número n y un número c, y
# luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).


print("== = > Ingrese su numero N para el control inicial del ciclo:")
n = int(input())
print("== = > Ingrese su numero C para el control final del ciclo:")
c = int(input())

for i in range(n+1, (n+c)+1):
    print("===>", i)

# Escribir un programa que pida al usuario dos enteros y los guarde en dos variables. Si el
# primero de los valores fuera menor que el segundo, el programa deberá además intercambiar los
# valores de las variables y mostrarlos de mayor a menor.
a = int(input())
b = int(input())
aux = a
if a < 0 or b < 0:
    print("Por favor ingrese enteros = N")

if a < b:
    a = b
    b = aux

print("Mayor ==>", a)
print("Menor ==>", b)

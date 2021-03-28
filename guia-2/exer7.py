# Escribir en papel un programa que pida al usuario dos números de punto otante y muestre
# su promedio. Además, si el promedio es mayor que 7 el programa debe mostrar en pantalla
# Aprobado y si no, debe mostrar Desaprobado. Después de hacerlo en papel, pasarlo a Python.

a = float(input())
b = float(input())

prom = (a+b)/2

if prom > 7:
    print("APROBADO")
else:
    print("DESAPROBADO")

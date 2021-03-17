"""
Escribir en papel un programa que pida una nota y que en el caso de que sea menor a cuatro
muestre "Debe recuperar". Luego pasarlo a Python.
"""

print("===> Ingrese la nota a evaluar")
n = int(input())

if (n < 4):
    print("Debe recuperar")
else:
    print("Aprobado")

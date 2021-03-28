# Se tiene la siguiente lista con DNIs de personas.
# 30612453
# 23763290
# 21448503
# 34582048
# 15364857
# Dado otro número de DNI cualquiera, se desea construir un programa que determine si es alguno
# de los existentes en el listado. Escribir el programa en papel y luego pasarlo a Python.

n1 = 30612453
n2 = 23763290
n3 = 21448503
n4 = 34582048
n5 = 15364857

value = int(input())

if value == n1 or value == n2 or value == n3 or value == n4 or value == n5:
    print("Su DNI se encuentra en la base de datos.")
else:
    print("Su DNI no se encuentra en la base de datos.")

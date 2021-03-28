# Un profesor clasica las notas de sus alumnos de la siguiente manera:
# 1-3 Reprobado
# 4-6 Debe rendir examen nal
# 7-10 Eximido
# a) Escribir un programa que indique la clasicación de una nota.
# b) Escribir un programa que pida 3 notas, calcule el promedio e indique la clasicación
# del mismo.

n1 = float(input())
n2 = float(input())
n3 = float(input())

if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
    print("ENVIE NOTAS VALIDAS")
else:
    value = (n1+n2+n3)/3

    if value <= 3 and value >= 1:
        print("Reprobado")
    elif value >= 4 and value <= 6:
        print("Debe rendir final")
    elif value >= 7 and value <= 10:
        print("Eximido")
    else:
        print("Error de calculo por numero altos o otro problema")

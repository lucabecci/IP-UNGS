"""
Una empresa telefónica desea un programa para calcular el importe de sus clientes. Sabiendo que el
costo por comunicación es de $3 y por cada segundo se cobra $0, 25 hacer dicho programa. Se deben
ingresar la cantidad de llamadas realizadas y el tiempo total de comunicación, el programa debe devolver
el precio a cobrar.
"""
costo_comunicacion = 3
costo_segundo = 0.25

print("===> Ingrese la cantidad de llamadas realizadas:")
cant_llamadas = int(input())
print("===> Ingrese el tiempo total de comunicacion en horas:")
cant_comunicacion = float(input())

result = (cant_comunicacion/36000 * costo_segundo) + \
    (cant_llamadas * costo_comunicacion)

print("===> Precio a cobrar:", result)

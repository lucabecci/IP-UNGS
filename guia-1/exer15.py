"""
Un vendedor recibe un sueldo base de $7000 más un 10 % extra del total de sus ventas, el vendedor
desea saber cuánto dinero obtendrá en total en el mes si ha logrado realizar 3 ventas este mes. Tenga en
cuenta el sueldo básico y la comisión por las ventas. Hacer un programa que solicite el monto de cada
una de las ventas del mes e indique cuál será el sueldo final del vendedor
"""

sueldo = 7000
extra_venta = 0.10
ventas_mes = 3

print("===> Ingrese el valor de la primer venta")
venta1 = int(input())

print("===> Ingrese el valor de la segunda venta")
venta2 = int(input())

print("===> Ingrese el valor de la tercer venta")
venta3 = int(input())

venta1 = venta1 * extra_venta
venta2 = venta2 * extra_venta
venta3 = venta3 * extra_venta

final = (sueldo + (venta1+venta2+venta3))

print("===> Su sueldo del mes es:", final)

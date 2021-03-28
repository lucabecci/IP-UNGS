# Hacer en pseudocodigo y luego un programa que calcule el importe que se le facturará a un
# cliente por consumo de electricidad sabiendo que la compañía que se la provee cobra una tarifa
# ja de 20 pesos que incluye los primeros 200 KW consumidos y los KW excedentes se los cobra
# a 0,5 pesos el KW, además se agregan $7, 8 de impuestos. Se leen los valores del medidor al
# comienzo y al n del período

print("==> Ingrese el valor inicial de KW del cliente")
comienzo = float(input())
print("==> Ingrese el valor final de KW del cliente")
final = float(input())

kw_iniciales = 200
kw_iniciales_valor = 20
impuestos = 7.8
exedido = 0.5

kw_final = final + comienzo
valor_final = 0

if kw_final <= kw_iniciales:
    valor_final = kw_iniciales_valor + impuestos
    print("El cliente debe de pagar:", valor_final)
else:
    kw_final = kw_final - kw_iniciales
    print("El cliente debe de pagar:", kw_final *
          exedido+kw_iniciales_valor+impuestos)

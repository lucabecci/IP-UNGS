"""
Un ciudadano argentino está exento de votar en estos casos:
Tiene más de 70 años
Tiene entre 18 y 70 años pero se encuentra a más de 500 km del centro de votación.
Suponiendo que las variables edad y distancia representan la edad y la distancia del ciudadano, escribir la expresión lógica que representa esta situación.
"""

print("===> VOTACION <===")
print("===> Ingrese su edad")
age = int(input())
print("===> Ingrese su distancia(KM)")
km = int(input())

if(age <= 70):
    if(km <= 500):
        print("Usted puede votar")
    else:
        print("Usted esta excento de votar por su distancia")
else:
    print("Usted esta excento de votar por ser mayor de 70")

# Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
# El programa deberá luego hacer que en la variable a quede el menor de los valores recibidos, en
# b el intermedio y en c el mayor (es decir, ordenará los valores).

a = int(input())
b = int(input())
c = int(input())

aux = a

if a > b and a > c:
    aux = c
    c = a
    if aux > b:
        a = b
        b = aux
    else:
        a = aux
elif b > a and b > c:
#     aux = c
#     c = a
#     if aux > c:
#         a = c
#         b = aux
# # elif c > a and c > b:

print(a)
print(b)
print(c)

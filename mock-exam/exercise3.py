import random

name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")

pass_hashed = ""

count = 0
for i in name:
    if count < 1:
        pass_hashed = pass_hashed + i
        count = count + 1
    else:
        continue
count = 0
pass_hashed = pass_hashed + str(random.randint(100, 1000))
for x in lastname:
    if count >= len(lastname) - 2:
        pass_hashed = pass_hashed + x
    else: 
        count = count + 1
        continue

print(pass_hashed)


n = int(input("Inserte N: "))

result = 1
multiply = 3
for x in range(2, n+1):
    if x != 2:
        multiply = multiply * 3
    if x % 2 == 0:
        result = result - x/multiply
    else: 
        result = result + x/multiply

print(result)

def perfectNumber(n):
    c = 0
    for x in range(1, n):
        if n % x == 0:
            c = c + x
    if  c == n:
        return(n, "es un numero perfecto")
    else:
        return(n, "no es un numero perfecto")

print(perfectNumber(5))
print(perfectNumber(15))
print(perfectNumber(6))
print(perfectNumber(28))
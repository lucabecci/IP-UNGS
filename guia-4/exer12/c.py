def abundantNumber(n):
    c = 0
    for x in range(1, n):
        if n % x == 0:
            c = c + x
    print(c)
    if  c > n:
        return(n, "es un numero abundante")
    else:
        return(n, "no es un numero abundante")

print(abundantNumber(5))
print(abundantNumber(12))
print(abundantNumber(6))
print(abundantNumber(28))
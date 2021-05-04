def isPrime(n):
    result = True
    for x in range(2, n):
        if n % x == 0:
            result = False
    
    return result

print(isPrime(11))
print(isPrime(5))
print(isPrime(67))
print(isPrime(97))
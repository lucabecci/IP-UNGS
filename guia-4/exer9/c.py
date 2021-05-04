def inpurePrime(n):
    count = 0
    for i in range(2, n+1):
        for x in range(2, n+1):
            if i % x == 0:
                count = count + 1
        if count == 1:
            print(i)
        count = 0
inpurePrime(20)
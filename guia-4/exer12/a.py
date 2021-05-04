def addedDivider(n):
    count = 0 
    for x in range(1, n+1):
        if n % x == 0:
            print(x)
            count = count + n
    return count

print(addedDivider(36))
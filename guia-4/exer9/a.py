def count(n):
    result = 0
    if(n < 1):
        return("Please send a valid number")
    for x in range(1, n+1):
        if n % x == 0:
            result = result + 1
        else:
            continue
    
    return(result)

print(count(20))
print(count(35))
print(count(8))
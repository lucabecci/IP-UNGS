def twoOver(x, y):
    if x > y:
        return x
    else: 
        return y

print(twoOver(2, 23))
print(twoOver(20, 10))

def threeOver(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

print(threeOver(10, 2, 44))
print(threeOver(10, 22, 4))
print(threeOver(120, 2, 4))
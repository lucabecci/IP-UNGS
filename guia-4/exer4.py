def printString(str):
    print(str)

def loopPrint(n, str):
    for x in range(1, n+1):
        printString(str)

loopPrint(3, "LOOP")
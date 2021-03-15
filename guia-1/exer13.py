"""
Suponga que una persona desea invertir su capital en un banco y quiere saber cuánto dinero tendrá en
su cuenta si el banco incrementa el 6 % mensual(no acumulativo). Se le debe pedir al usuario el capital
a invertir y la cantidad de meses.
"""

print("Insert the capital to invert")
capital = int(input())
print("Insert the months to invert:")
months = int(input())


result = capital+((capital*0.06)*months)

print("Earned:", result)

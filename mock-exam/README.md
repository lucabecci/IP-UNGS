


# Ejercicio 1: (2 puntos)
## Responder las siguientes preguntas, justificando claramente las respuestas.
- a)	Si letra2=”i”, letra1=”u”. ¿Qué rama ejecuta el siguiente condicional? 
  if (letra1+letra2 == ”ui” or letra1+letra2 == “u”)
>  La rama que ejecuts el condicional es letra1+letra2 == “ui

- b)	Si la variable a es un entero y la guarda del if es  a>4 or a<3 ¿Cuánto debe valer a  para que no se cumpla la guarda? 
> Para que no se cumpla a debe ser 2
> 
- c) ¿Cuántas iteraciones realiza el siguiente ciclo? 
```
k=4
while(k<5):
   print (“Valor de k es:”, k)
```
> Realiza infinitas iteraciones ya que la variable auxiliar del while no se incrementa en ningún momento.

- d) ¿Qué imprime este programa? ¿Qué valor tiene la variable cant al finalizar la ejecución del programa? 
```
cant = 0
for i in range (0,20,4):
	print (“Hola \n Hola”)
	cant = cant + 1
print(cant*2)
```
> Al final la ejecución cant valdrá 130

# Ejercicio 2: (2 puntos)
```
1	# PRIMOS MEJORADO
2
3	n=int(input("Ingrese numero natural mayor a 1"))
4
5	if(n<=1):
6	    print("debe ingresar un numero mayor a 1")
7	else:
8
9    	i=2
10	    tieneMasDiv=False
11	    while(i<=n//2 and not tieneMasDiv):
12	        if(n%i==0):
13	            tieneMasDiv=True
14	        i=i+1
15	    if(not tieneMasDiv):
16	        print(n,"----------")
17	    else:
18	        print(n,"----------")
```
- a)¿Qué tipo de variables es tieneMasDiv? , ¿Qué valores puede tomar?
> Es de valor booleana, puede tomar True o False.
- b)  ¿se podría hacer este programa utilizando un ciclo For (justifique la respuesta)
- c) completar  el print de líneas 16 y 18…
- d) si el n ingresado fuera 3, cuál es el valor de i al finalizar el programa

# Ejercicio 3: (3 puntos)
- Hacer un programa que genere una clave provisoria a partir del nombre y apellido (que ingresa el usuario). La clave estará formada por la primera letra (en mayúscula) del nombre, un numero de 3 cifras generado al azar y la 2 últimas letras del apellido (en minúsculas). Ejemplo: Luis Perez === >> L287ez
	
# Ejercicio 4: (3 puntos)
- Escribir un programa que calcule la siguiente serie, teniendo en cuenta que n es un número entero introducido por teclado. Si n=5 la serie sería:
> s = 1 - 2/3 + 3/9 - 4/27 + 5/81

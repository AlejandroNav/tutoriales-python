def factorial(num):     # imprimir un factorial
    suma = 1
    for x in range(num): # por cada numero hasta llegar al numero dado
        suma +=suma*x      # suma al contador la multiplicacion del numero * el contador
    return suma

print(factorial(7))
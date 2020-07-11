def factorial(num):     # imprimir un factorial
    suma = 1
    for x in range(num): # por cada numero hasta llegar al numero dado
        suma +=suma*x      # suma al contador la multiplicacion del numero * el contador
    return suma


def compound_interest(inversion, termino, interes, periodos): # in teres compuesto a 2 decimales
    ans = inversion * (1 + interes / periodos) ** (periodos * termino)
    return round(ans, 2)


print(factorial(7))
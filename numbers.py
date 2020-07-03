from math import *

numero = 34
print(2)
print(numero * 4 + 5)
print(str(numero) + " es mi numero de la suerte ")
print(pow(5, 5))
print(floor(4.75))
print(sqrt(456))
i = 1
while i <= 5:
    print(str(i) + " potencia")
    print(11 ** i)
    i += 1
def elevar(base,potencia):
    resultado = 1
    for i in range(potencia):
        resultado = resultado * base;
    return resultado
print(elevar(11,5))
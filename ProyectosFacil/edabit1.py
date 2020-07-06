def rango_lista(nums):  # La funcion regresa la resta del minimo y el mayr de una lista cualquiera
    return max(nums) - min(nums)


def profitable_gamble(prob, prize,
                      pay):  # la funcion es la probabilidad de que ganar una apuesta sea mas barto que la entrada
    return prob * prize > pay


def primer_elemento(lista):
    return lista[0]


def ultimo_elemento(lista):
    return lista[len(lista) - 1]


def is_empty(s):  # chea si el estring esta vacio
    if s:      # if el objeto contiene algo  "return not s" hace lo mismo que tod.o el if
        return False
    else:
        return True


l6 = [-3, 4, -9, -1, -2, 15]
l5 = ["DAS", "apt", "asdas", "234", "Javier"]

print(ultimo_elemento(l6))
print(primer_elemento(l6))
print(rango_lista(l6))
print(profitable_gamble(.3, 40, 4))

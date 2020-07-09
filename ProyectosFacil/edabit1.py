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
    if s:  # if el objeto contiene algo  "return not s" hace lo mismo que tod.o el if
        return False
    else:
        return True


def get_drink_by_profession(param):
    test = param.lower()
    empleos = ["jabroni", "school Counselor", "programmer", "bike gang member", "politician", "rapper"]
    bebidas = ["Anything with Alcohol", "Hipster Craft Beer", "Moonshine", "Your tax dollars", "Cristal", "Beer"]
    i = 0
    for x in test:
        print(x)
        print(bebidas[i])


def get_drink_by_profession(param):
    test = param.lower()
    empleos = {
        "jabroni": "Patron Tequila", "school counselor": "Anything with Alcohol", "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine", "politician": "Your tax dollars", "rapper": "Cristal"
    }
    for llave in empleos:
        print(llave)
        if llave==test:
            return empleos[llave]
    return "Beer"


l6 = [-3, 4, -9, -1, -2, 15]
l5 = ["DAS", "Politician", "asdas", "234", "Javier"]

print(ultimo_elemento(l6))
print(primer_elemento(l6))
print(rango_lista(l6))
# print(profitable_gamble(.3, 40, 4))
print("asfsadgadfgdsfgsdfhsdfgedg")
print(get_drink_by_profession(l5[1]))

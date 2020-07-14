def factorial(num):  # imprimir un factorial
    suma = 1
    for x in range(num):  # por cada numero hasta llegar al numero dado
        suma += suma * x  # suma al contador la multiplicacion del numero * el contador
    return suma


def compound_interest(inversion, termino, interes, periodos):  # interes compuesto a 2 decimales
    ans = inversion * (1 + interes / periodos) ** (periodos * termino)
    return round(ans, 2) # el numero y los decimales a redondear


def first_last(name):  # regresa el primer y ultimo caracter de un string concatenacion
    return name[0] + name[-1]  # para acceder al ultimo elemneto se usa index negativo


def oddeven(lst):  # decide si una lista tiene ams negativos o mas positivos
    pares = 0
    impares = 0
    for numero in lst:  # por cada numeros aumentas el contador
        if not numero % 2:
            pares += 1
        else:
            impares += 1
    return pares < impares  # evalua si hay mas pares que impares regresa Bool


def mapping(letters):  # crea un diccioanrio con lo que le entra
    dictionary = {}
    for letter in letters:
        dictionary[
            letter] = letter.upper()  # en este casi la llave es la minuscula y el cntenido la mayuscula que creamos
    return dictionary


def correct_stream(user, correct):
    ans = []
    for u in user:
        if u in correct:
            ans.append(1)
        else:
            ans.append(-1)
    return ans


def integer_boolean(n):  # le das un numero de ceros uno y regresa Trues y falso en un arreglo lista
    lista=[]
    for numero in n:
        if numero == "1":       # si es 1 refresa falso
            lista.append(False)
        else:
            lista.append(True)
    return lista


print(integer_boolean("101011"))

print(correct_stream(
    ["it", "is", "find"],
    ["it", "is", "fine"]
))
print("------------------")
print(mapping(["p", "s", "r", "w"]))
l1 = [1, 2, 9, 9, 5, 9, 7, 9, 9]
l2 = [4, 2, 4, 4, 5, 4, 7, 4, 2]
print(oddeven(l1))
print(first_last("Hola cabeza"))
print(factorial(7))

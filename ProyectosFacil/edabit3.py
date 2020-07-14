from math import ceil


def unique_sort(lst):  # recibe una lista
    my_set = set()  # crea uns et vacio, los sets no admiten valores repetidos
    for element in lst:
        my_set.add(element)  # agrega uno por uno los valores de la lista al set
    ans = list(sorted(my_set))  # sorting del set y regresa el set como lista
    return ans


def unique_sort2(lst):  # en una sola linea trabajando directamente sobre la lsita
    return sorted(set(lst))


frase = "Hola"


def remove_vowels(txt):
    ans = ""
    for letter in txt:
        if letter not in "aeiouAEIOU":
            ans += letter
    return ans  # return ''.join(char for char in txt if not char in "aeiouAEIOU")


def reverse(txt): # toma un string
    x = txt.swapcase() # cambia los cases
    return x[::-1]  # lo pone al inverso el index de sus componentes con un slice que trabaja con indice negativo


def cars_needed(n):
    return ceil((n/5))

print(cars_needed(17))

print(reverse("Hola mundo Como Estas JUAN"))

print(remove_vowels(frase))

print(unique_sort2([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))

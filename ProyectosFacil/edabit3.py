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

def reversestring(txt): # toma un string
    x = txt.swapcase() # cambia los cases
    return x[::-1]  # lo pone al inverso el index de sus componentes con un slice que trabaja con indice negativo

def cars_needed(n):
    return ceil((n/5))


def alphanumeric_restriction(s):
    return s.isalpha() or s.isdigit()


def get_student_names(students):
    #return sorted(students.values()) / solo sortea el resultado de los valores
    return sorted((value, key)for (key, value) in students.items()) #sorte de valores y llaves usando list comprehension


def is_in_order(arg):
   return list(arg) == sorted(arg) # que si un string estan en orden sus elemntos


def reverse(arg):
    if  isinstance(arg,bool):
        return not arg
    else:
        return "boolean expected"


def name_shuffle(txt):
    divided = txt.split() # takes the string and splits it into a list
    reverslist= reversed(divided)  #  returns an iterator that accesses the list in the reverse order
    listfinished = list(reverslist) # creates a  new list in that order
    return " ".join(listfinished)      # returns that list as a String


def factorial(n):  # regresa un factorial
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n - 1);  # de manera revursiva multiplicamos nuestros numeros que forman el factorial


def nth_smallest(lst, n):
    if len(lst) < n:
        return "none"
    else:
        ans=sorted(lst)
        return ans[n-1]


print(nth_smallest([1, 5, 3, 7], 1))

print(factorial(6))

print(name_shuffle("Javier Mariana Raul"))

print(reverse(True))

print(is_in_order("edabit"))

print(get_student_names({"Student 1" : "Steve",  "Student 2" : "Becky",  "Student 3" : "Alexohn"}))

print(alphanumeric_restriction("Bold"))

print(cars_needed(17))

print(reversestring("Hola mundo Como Estas JUAN"))

print(remove_vowels(frase))

print(unique_sort2([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))

def mean(num):  # se promedian los digitos que entran como entero
    listnum = [int(x) for x in str(num)]
    return sum(listnum) / len(listnum)


def steps_to_convert(txt):    # regresa el menor numero de pasos para convertir a mayuscuals o minusculas
    major = minor = 0  #declara dos variabels en cero
    for c in txt:
        if c.isupper():     #si el character es mayuscula se suma major 1 else minor 1
            major += 1
        else:
            minor += 1
    return min(minor, major)    # regresa el menor de los contadores


def sum_numbers(n): # suma natural usando recursividad
    if n <= 1:      #si n es 1 termina el programa y regresa la sumatoria
        return n
    return n + sum_numbers(n - 1)


def remove_enemies(names, enemies):
    return [name for name in names if name not in enemies]


print(remove_enemies(["Adam", "Emmy", "Tanya", "Emmy"], ["Emmy"]))

print(sum_numbers(12))

print(steps_to_convert("sdgsFGSEdDdsfSD"))

print(mean(12345))

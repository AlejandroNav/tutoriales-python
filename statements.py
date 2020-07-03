def maximo(x,y,z):
    if x >= y and x >= z:
        print("El mas grande es ")
        return x
    elif y >= x and y >= z:
        print("El mas grande es ")
        return y
    else:
        print("El mas grande es ")
        return z
print(maximo(444,55,45))
es_hombre = True
is_tall = False

if es_hombre and is_tall:
    print("Eres hombre alto")
elif es_hombre and not(is_tall):
    print("Eres un chaparro")
elif not(es_hombre) and is_tall:
    print("Eres una mujer alta")
else:
    print("Eres mujer chaparra")


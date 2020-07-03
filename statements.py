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
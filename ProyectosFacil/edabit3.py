def unique_sort(lst):  # recibe una lista
    my_set = set()   #crea uns et vacio, los sets no admiten valores repetidos
    for element in lst:
        my_set.add(element)  # agrega uno por uno los valores de la lista al set
    ans= list(sorted(my_set))       # sorting del set y regresa el set como lista
    return ans

def unique_sort2(lst):  # en una sola linea trabajando directamente sobre la lsita
  return sorted(set(lst))

print(unique_sort2([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))

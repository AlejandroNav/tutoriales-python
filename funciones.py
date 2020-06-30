friends = ["albert","jebus","integrales","asdasd"]
lucky = [3,5,7,2,3,345]
friends[3]="Raul"
#friends.extend(lucky) # esto le agrega la lista completa
friends.append("Mi amighito")  # agrega elemento al final de la lista
friends.insert(1,"Javier") # agrega en  un lugar en especifico
friends.remove("jebus") # remueve uno en especifico
print(len(friends)) # numero de lementos en la lista
print(friends)
friends.pop() #elimina el ultimo elemento
print(friends)
friends.sort() # sorting
print(friends)
print(str(friends.index("Javier")) + " es el lugar de mi amigo javier en esta lista")
# index el lugar de ese elemnto o primera instancia
friends2 = friends.copy()
print("esto limpia toda la lista clear")
friends.clear()
print(friends)
print(friends2)

# @@@ Tuples son contenedores donde puedes guardar informacion, las diferencias son
# no pueden pueden ser cambiadas o modificadas

coordenas = (45,34)
print(coordenas)
print(coordenas[1])

def say_hi(nombre,age):
    print("Hello user " + nombre + str(age))
say_hi("mike",70)

def cubo(numero):
    numero = pow(numero,3)
    return numero
print(cubo(5))
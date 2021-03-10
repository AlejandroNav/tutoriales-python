print("Hello World")
print("Bonjour la terre")
nombre = "Juan Rofrigo marcano"
edad = 45
is_adulto = False

nombre = input("Dame tu nombre ")

print("hola " + nombre.upper() + " como estas hoy? " )
print("tu nombre esta en minusculas: " +  str(nombre.islower()))
print("el largo de tu nombre: " + str(len(nombre)))  #largo del string
print("la cuarta letra en tu nombre " + nombre[3])
if is_adulto:
    print('si lo es ' + nombre)
else:
    print("no lo es " + nombre)
'''
color = input("dame un color ")
sustantivo = input("dame un sustantivo ")
celebridad = input("dame una celebridad ")

print("Las rosas son " + color)
print( sustantivo + " son azules")
print("amo a " + celebridad)'''

amigos = ["Alejandro","rodrigo","Mariano","javier"]
print(amigos[1])

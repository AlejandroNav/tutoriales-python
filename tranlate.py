def traducir(frase):
    resultado = " "
    for letra in frase:
        if letra.lower() in "pbjvfmnxzys":
            if letra.isupper():
                resultado = resultado + "F"
            else:
                resultado = resultado + "f"
        else:
            resultado = resultado + letra
    return resultado

print(traducir("hola como estas"))
print(traducir(input(" dame tu frase ")))
#comentarios son para introducir informacion solo en codigo
try:
    #value = 10/0
    number = int(input("dame un numero "))
    print(number)
except ZeroDivisionError as err:
    print("err" + str(err))
except ValueError as err:
    print("entrada invalida " + str(err))

archivo_empleados = open("empleados.txt","r+")
print(archivo_empleados.readable())  # te dice si es leible el archivo
#print(archivo_empleados.read()) # te dice to do lo que hay dentro
#print(archivo_empleados.readline()) # te da una linea
empleados = archivo_empleados.readlines() # te da una linea
print(empleados)
archivo_empleados.write("\nDAniela - Chofera")

for empledo in empleados:
    print(str(empledo)+ " y trabaja desde hace")

archivo_empleados.close()

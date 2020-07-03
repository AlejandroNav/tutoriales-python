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
    value = 10/0
    number = int(input("dame un numero "))
    print(number)
except ZeroDivisionError as err:
    print("err" + str(err))
except ValueError as err:
    print("entrada invalida " + str(err))
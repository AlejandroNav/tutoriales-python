print("Hola bienvenido al programa de numeros primos")
numero_final = int(input("Dame numero"))


def checa_numero(numero_checar):
    if numero_final >= 2:
        return True
    else:
        print("Error numero menor que dos")
        return False


def divisores(dividendo):
    for numero in range(1, numero_final + 1):
        if numero_final % numero == 0:
            print(str(numero) + " es un numero divisor de " + str(numero_final))

def divisores(dividendo):
    for numero in range(1, numero_final + 1):
        if numero_final % numero == 0:
            print(str(numero) + " es un numero divisor de " + str(numero_final))

def esPrimo(primo_checar):
    for numero in range(2, numero_final):
        if numero_final % numero == 0:
            print(str(numero_final) + " no es un numero primo")
            return False
    else:
        print(str(numero_final) + " es un numero primo")
        return True

if checa_numero(numero_final):
    divisores(numero_final)
    if esPrimo(numero_final):
        print("si es verdad")
    else:
        print("no es verda")
    print("Los numeros primos hasta ese rango")

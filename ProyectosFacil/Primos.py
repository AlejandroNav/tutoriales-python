print("Hola bienvenido al programa de numeros primos")
numero_final = int(input("Dame numero: "))
print("\n")


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


def es_primo(primo_checar):
    for numero in range(2, primo_checar):
        if primo_checar % numero == 0:
            return False
    return True


def numeros_primos(rango_checar):
    for numero_prueba in range(2, rango_checar):
        if es_primo(numero_prueba):
            print(str(numero_prueba) + " es un numero primo dentro del rango " + str(rango_checar) )


if checa_numero(numero_final):
    divisores(numero_final)
    if es_primo(numero_final):
        print(str(numero_final) + " es un numero primo")
    else:
        print(str(numero_final) + " no es un numero primo")
    print("\nLos numeros primos hasta ese rango: \n ")
    numeros_primos(numero_final)

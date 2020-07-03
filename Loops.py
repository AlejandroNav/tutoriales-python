print("hello ")
i=1
while i<=3:
    print(i)
    i += 1
print("termina el loop ")

secret_word = "CUATRO"
guess = ""
intentos = 0
limite = 3
perdio = False
while guess != secret_word and not(perdio):
    if intentos < limite:
        guess = input("dame un numero al 10 ").upper()
        intentos += 1
    else:
        perdio = True
if perdio:
    print("perdiste")
else:
    print("si el nuemro correcto era " + guess)




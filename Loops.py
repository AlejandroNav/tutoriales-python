for letter in "Hola que tal ":
    print(letter)
numeros=["inicio",4,5,6,7,"final"]

for x in numeros:
    print(x)
print("====================================")
for x in range(len(numeros)):
    print(numeros[x])

print("====================================")
i=1
while i<=3:
    print(str(i) + " del loop ")
    i += 1
print("termina el loop aqui")
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




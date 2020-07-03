diccionario = {
    "suma":"+",    "Suma":"+",    "resta": "-",    "multi": "*",    "divi": "/",    "division": "/",
    "+":"+",    "sumatoria":"+",    "-": "-",    "*": "*",    "/": "/",    "/": "/"
}
print(diccionario["suma"])
num1 = float(input("numero 1: "))
num2 = float(input("numero 2: "))
operacion = diccionario.get(input("+ - / * Dame un operando: "))
if operacion =="+":
    print(num1+num2)
elif operacion =="-":
    print(num1-num2)
elif operacion =="/":
    print(num1/num2)
elif operacion =="*":
    print(num1*num2)
else:
    print("operador invalido")

import math
import random
myName = "joven"

print('What is your age?')  # ask for their age

myAge = input()

if int(myAge) >= 70:
    print("The future is now old man")
    myName = "miedad"
print(myName)

frutero = ['apple', 'banana', 'cherry']
for frutas in frutero:
    print(frutas)


total = 0
for numeros in range(101):
    total = total + numeros
print(total)


i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print(random.randint(1, 999))


def AgePlus(x):
    return x + 18


print('Hello', ' your age is ', AgePlus(int(myAge)))


def divBy10(divisor):
    try:
        return 10/divisor
    except ZeroDivisionError:
        return "no cero"

print(divBy10(12))
print(divBy10(10))
print(divBy10(7))
print(divBy10(5))
print(divBy10(0))
print(divBy10(120))
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

print(random.randint(1,999))


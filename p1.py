myName = "joven"
print('What is your age?')    # ask for their age
myAge = input()
if int(myAge) >= 70:
    print("The future is now old man")
    myName = "miedad"
print(myName)


frutero = ['apple', 'banana', 'cherry']
for frutas in frutero:
    print(frutas)

i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

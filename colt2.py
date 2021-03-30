print("Hola")

tasks = ["Instalatr","Estudiar","descnasar",4.5,7,56]
print(tasks)
x=0
for item in tasks:
    x+=1
    print(item)
    tasks.pop(x)

print('lista despues del ciclo de pop ; ')
print(tasks)

import modules
import docx

print(docx.__version__)
suma = 0
for x in range(5):
    temp = int(modules.roll_dice(20))
    suma = suma + temp
    print(temp)
    print("Suma parcial es: " + str(suma))
print(suma)
print(suma/x)
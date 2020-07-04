from clases import Student
from clases import Cuestionario

estudiante1 = Student("juan", "Matematicas", 7.7, True)
estudiante2 = Student("Maria", "Historia", 4.7, False)
print(estudiante1)
print(estudiante2.nombre)

preguntas = [
    "\nQue color es mas fuerte\n A) Azul\n B) Verde\n C) Naranja\n",
    "\nDonde esta La Paz\n A) Jamaica\n B) Bolivia\n C) Chile\n",
    "\nQue tan alto es el Everest\n A) 4000m\n B) 566m\n C) 8850m\n",
    "\nQue es 5 + 5 \n A) 4000\n B) 5\n C) 10\n",
    "\nQue tan alto eres\n A) 1.5\n B) 1,6\n C) 1,8\n",

]

tabla1 = [
    Cuestionario(preguntas[0], "A"),
    Cuestionario(preguntas[1], "B"),
    Cuestionario(preguntas[2], "C")
]
tabla2 = [
    Cuestionario(preguntas[4],"C"),
    Cuestionario(preguntas[3], "C"),
    Cuestionario(preguntas[2], "C"),
]


def examen(tabla_entrada):
    calificacion = 0
    for preguntas in tabla_entrada:
        respuesta_usuario = input(preguntas.respuesta)
        if respuesta_usuario == preguntas.respuesta_correcta:
            calificacion += 1
    print("Felicidades sacaste " + str(calificacion) + " de " + str(len(tabla_entrada)))


examen(tabla2)

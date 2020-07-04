class Student:

    def __init__(self, nombre, carrera, promedio, is_regular):
        self.nombre = nombre
        self.carrera = carrera
        self.promedio = promedio
        self.is_regular = is_regular


class Cuestionario:

    def __init__(self, respuesta, respuesta_correcta):
        self.respuesta = respuesta
        self.respuesta_correcta = respuesta_correcta

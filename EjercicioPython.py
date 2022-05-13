from random import seed
from random import randint

class Alumno():

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"Nombre: {self.nombre} , Nota: {self.nota}"

    def resultado(self):
        print("El alumno " + self.nombre + " con nota " + str(self.nota), end="")
        if self.nota >= 5:
            print(" ha aprobado")
        else:
            print(" ha suspendido")
        

if __name__ == "__main__":
    num_alumnos = 10
    nombres = ["Alvaro", "Miguel", "Paco", "Fermin", "Maria", "Marta", "Nacho", "Joaquin", "Silvia", "Lourdes"]
    alumnos = []
    seed(1)

    for i in range(num_alumnos):
        alumnos.append(Alumno(nombres[i], randint(0,10)))

    for al in alumnos:
        print(al)
    
    for al in alumnos:
        al.resultado()
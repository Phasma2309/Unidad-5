class Estudiante:
    def __init__(self, matricula, nombre):
        self.matricula = matricula
        self.nombre = nombre

class TablaHash:
    def __init__(self):
        self.tabla = {}

    def agregar_estudiante(self, estudiante):
        self.tabla[estudiante.matricula] = estudiante.nombre

    def buscar_estudiante(self, matricula):
        return self.tabla.get(matricula, "Estudiante no encontrado")

estudiantes = [
    Estudiante("A001", "Juan Perez"),
    Estudiante("A002", "Ana Gomez"),
    Estudiante("A003", "Carlos Sanchez")
]

tabla_hash = TablaHash()

for estudiante in estudiantes:
    tabla_hash.agregar_estudiante(estudiante)

matricula_a_buscar = "A002"
resultado = tabla_hash.buscar_estudiante(matricula_a_buscar)
print(f"Resultado de la búsqueda: {resultado}")

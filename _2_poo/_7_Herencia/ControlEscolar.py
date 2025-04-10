class ListaDatos:
    def __init__(self, matricula: str, estudiante: str, asignatura: str):
        self.matricula = matricula
        self.estudiate = estudiante
        self.asignatura = asignatura


class ControlEscolar(ListaDatos):
    def __init__(self):
        self.lista = []

    def addEstudiante(self, matricula, estudiante, asignatura):
        self.lista.append(ListaDatos(matricula, estudiante, asignatura))

    def show(self):
        for estudiante in self.lista:
            print(f"Matrícula: {estudiante.matricula}, Estudiante: {estudiante.estudiate}, Asignatura: {estudiante.asignatura}")


if __name__ == '__main__':
    escolar = ControlEscolar()
    escolar.addEstudiante("123456", "Paloma Suarez", "Estructura de datos")
    escolar.addEstudiante("654321", "Juan Perez", "Matemáticas")
    escolar.show()
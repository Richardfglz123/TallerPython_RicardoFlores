class ListaDatos:
    def __init__(self,matricula:str, estudiante:str, asignatura:str):
     self.matricula=matricula
     self.estudiate=estudiante
     self.asignatura=asignatura

if __name__ == '__main__':
    lista=[]
    lista.append(ListaDatos("12345","Tenoch Huerta","POO"))
    lista.append(ListaDatos("12346","Emianeso Hernandez","Estructura"))
    lista.append(ListaDatos("12347","Abraham Garcia","Base de datos"))
    lista.append(ListaDatos("12348","Josexo ","Si"))

    for obj in lista:
        print(f"Matricula:{obj.matricula}")
        print(f"Estudiante:{obj.estudiate}")
        print(f"Asignatura:{obj.asignatura}")
        print("----------------------------")

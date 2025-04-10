class Hospital:
    def __init__(self):
        self.__NombrePaciente: str = ""
        self.__nss = int = 1258
        self.__enfermedad: str = ""

    def __getNombrePaciente(self) -> str:
        return self.__NombrePaciente

    def getNss(self) -> int:
        return self.__nss

    @property  # Convierte el metodo en na propiedad de
    def getEnfermedad(self) -> str:
        return self.__enfermedad

    def setNombrePaciente(self, nombre: str):
        self.getNombrePaciente = nombre

    def fetNss(self, nss: int):
        self.nss = nss

    def setEnfermedad(self, enfermedad: str):
        self.enfermedad = enfermedad


if __name__ == '__main__':
    hospital = Hospital()

    hospital.__NombrePaciente = "Juan"

    print(hospital.getNombrePaciente)

    hospital.setEnfermedad("gripe")
    e = hospital.getEnfermedad
    print(e)

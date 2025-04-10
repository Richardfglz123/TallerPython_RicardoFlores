class Datos:
    def __init__(self,nombre,correo,whatsapp):
        self.nombre = nombre
        self.correo = correo
        self.whatsapp = whatsapp

    def __set_name__(self,nombre:str):
        self.nombre=nombre

if __name__ == '__main__':
    datos = Datos('Si','uwu@gmail.com','2481335004')

    print(datos.nombre)
    datos.setNombre("Juan")
    print(datos.nombre)
    datos.nombre="Gabriela"
    print(datos.nombre)
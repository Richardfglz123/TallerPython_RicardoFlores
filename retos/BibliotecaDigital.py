# Desarrolla un programa en Python que utilice la POO para registrar un libro
# (ISBN,TITULO Y AUTOR), los atributos debe estar en privado, debes tener un constructor
# para el registro, debes tener solo getters de cada atributo
# En otra clase debera regitrar una coleccion de libros, en esta clase debes tener add, delete y show

class Libro:
    def __init__(self, isbn, titulo, autor):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor

    def get_isbn(self):
        return self.__isbn

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor


class ColeccionLibros:
    def __init__(self):
        self.libros = []

    def add_libro(self, libro):
        if isinstance(libro, Libro):
            self.libros.append(libro)
            print(f"Libro '{libro.get_titulo()}' agregado con exito")
        else:
            print("Solo se pueden agregar instancias de la clase Libro")
    def delete_libro(self, isbn):
        for libro in self.libros:
            if libro.get_isbn() == isbn:
                self.libros.remove(libro)
                print(f"Libro con ISBN {isbn} eliminado")
                return
        print(f"No se encontró ningún libro con ISBN {isbn}")

    def show_libros(self):
        if not self.libros:
            print("La colección de libros no tiene contenido")
        else:
            print("Colección de libros:")
            for libro in self.libros:
                print(f"ISBN: {libro.get_isbn()}, Título: {libro.get_titulo()}, Autor: {libro.get_autor()}")


if __name__ == "__main__":
    coleccion = ColeccionLibros()

    libro1 = Libro("978-3-16-148410-0", "El Principito", "Antoine de Saint-Exupéry")
    libro2 = Libro("978-0-7432-7356-5", "Los Juegos del Hambre", "Suzanne Collins")

    coleccion.add_libro(libro1)
    coleccion.add_libro(libro2)
    coleccion.show_libros()

    coleccion.delete_libro("978-3-16-148410-0")
    coleccion.show_libros()

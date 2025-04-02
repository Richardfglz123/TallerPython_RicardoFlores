if __name__ == "__main__":
    biblioteca = []
    usuarios = {}

    def agregar_libro(titulo, autor, genero, copias):
        libro = {"titulo": titulo, "autor": autor, "genero": genero, "copias": copias}
        biblioteca.append(libro)
        print(f"Libro '{titulo}' agregado correctamente")

    def buscar_libro(filtro, valor):
        resultados = [libro for libro in biblioteca if libro[filtro].lower() == valor.lower()]
        if resultados:
            for libro in resultados:
                print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}, Copias: {libro['copias']}")
        else:
            print("No se encontraron libros que coincidan con la búsqueda")

    def prestar_libro(usuario, titulo):
        for libro in biblioteca:
            if libro["titulo"].lower() == titulo.lower():
                if libro["copias"] > 0:
                    libro["copias"] -= 1
                    if usuario not in usuarios:
                        usuarios[usuario] = []
                    usuarios[usuario].append(titulo)
                    print(f"El libro '{titulo}' se ha prestado a {usuario}.")
                else:
                    print("No hay copias disponibles para este libro")
                return
        print("El libro no existe en la biblioteca")

    def devolver_libro(usuario, titulo):
        if usuario in usuarios and titulo in usuarios[usuario]:
            for libro in biblioteca:
                if libro["titulo"].lower() == titulo.lower():
                    libro["copias"] += 1
                    usuarios[usuario].remove(titulo)
                    print(f"El libro '{titulo}' ha sido devuelto por {usuario}")
                    return
        print("El usuario no tiene este libro prestado")

    def mostrar_libros_disponibles():
        print("Libros disponibles en la biblioteca: ")
        for libro in biblioteca:
            if libro["copias"] > 0:
                print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}, Copias: {libro['copias']}")

    def filtrar_libros(filtro, valor):
        for libro in biblioteca:
            if libro[filtro].lower() == valor.lower():
                yield libro

    def menu():
        while True:
            print("Sistema de Gestión de Biblioteca")
            print("1 Agregar libro")
            print("2 Buscar libro")
            print("3 Prestar libro")
            print("4 Devolver libro")
            print("5 Mostrar libros disponibles")
            print("6 Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                genero = input("Género: ")
                copias = int(input("Número de copias: "))
                agregar_libro(titulo, autor, genero, copias)

            elif opcion == "2":
                print("Buscar por: 1. Título  2. Autor  3. Género")
                tipo_busqueda = input("Selecciona un criterio: ")
                filtro = "titulo" if tipo_busqueda == "1" else "autor" if tipo_busqueda == "2" else "genero"
                valor = input(f"Ingrese el {filtro}: ")
                buscar_libro(filtro, valor)

            elif opcion == "3":
                usuario = input("Nombre del usuario: ")
                titulo = input("Título del libro a prestar: ")
                prestar_libro(usuario, titulo)

            elif opcion == "4":
                usuario = input("Nombre del usuario: ")
                titulo = input("Título del libro a devolver: ")
                devolver_libro(usuario, titulo)

            elif opcion == "5":
                mostrar_libros_disponibles()

            elif opcion == "6":
                print("Gracias por utilizar el sistema de bibliotec")
                break

            else:
                print("Opción no válida. Intenta de nuevo")
    menu()
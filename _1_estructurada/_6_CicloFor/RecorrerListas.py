if __name__ == '__main__':
    print("----------")
    lista = [1, 2, 3, "Lunes", 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    lista.append(200)
    lista.append("Viernes")
    lista.append(False)
    lista.append(2.69)

    lista2 = [17, 18, 19, 20]
    lista.extend(lista2)

    for elemento in lista:
        print(elemento)

    nombre:str
    nombre= "Luis"
    nombre +="Gutierrez"
    nombre.join("Gutierrez")
    print(nombre)

    lista3 = ["Alfonso", "Iker", "Juan"]
    cadena: str= " - ".join(lista3)
    print(cadena)

    separado=cadena.split()
    for dato in separado:
        print(dato)

        if __name__ == '__main__':
            cantidad = int(input("¿Cuántos nombres quieres introducir? "))
            nombres = []

            # Recolectamos los nombres
            for _ in range(cantidad):
                nombre = input("Introduce un nombre: ")
                nombres.append(nombre)

            # Inicializamos contadores por rango de letras (1-4, 5-8, 9+)
            rangos = {"1-4": 0, "5-8": 0, "9+": 0}

            # Contamos las letras en cada nombre y clasificamos
            for nombre in nombres:
                largo = len(nombre)
                if 1 <= largo <= 4:
                    rangos["1-4"] += 1
                elif 5 <= largo <= 8:
                    rangos["5-8"] += 1
                else:
                    rangos["9+"] += 1

            # Mostramos los resultados
            print("\nResultados:")
            print(f"Nombres de 1 a 4 letras: {rangos['1-4']}")
            print(f"Nombres de 5 a 8 letras: {rangos['5-8']}")
            print(f"Nombres de 9 o más letras: {rangos['9+']}")

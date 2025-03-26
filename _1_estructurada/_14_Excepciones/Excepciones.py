if __name__ == '__main__':
    try:
        # Código que puede causar una excepción
        numero = int(input("Introduce un numero: "))
        resultado = 10 / numero
    except ValueError:
        # Manejo de la excepción si se introduce un valor no válido
        print("¡Error! Debes introducir un numero entero.")
    except ZeroDivisionError:
        print("¡Error! No se puede dividir entre cero.")
    else:
        # Se ejecuta si no hubo excepciones
        print("El resultado es", resultado)
    finally:
        # Se ejecuta siempre, haya o no habido excepciones
        print("Fin del programa.")

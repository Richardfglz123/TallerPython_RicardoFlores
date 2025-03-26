    #Funcion que recibe una tupla y la desempaqueta
def calcular_area(rectangulo: tuple[int, int]) -> int:
        largo, ancho =rectangulo
        return largo * ancho

def cuadrado(rectangulo: tuple[int, int]) -> tuple[int, int]:
    largo, ancho = rectangulo
    largo=largo*largo
    ancho=ancho*ancho
    return(largo, ancho)

if __name__ == '__main__':
    #crear tupla
    dimenciones = (10, 5)

    #llamar  a la funcion con la tupla
    area = calcular_area(dimenciones)
    print(f"El area del rectangulo es: {area} mts cuadrados")

    largo, ancho=cuadrado((5,3))

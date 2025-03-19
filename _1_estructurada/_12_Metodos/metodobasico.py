import statistics as mate

def suma(a:int, b:int):
    print(f"la suma de {a} + {b} es {a+b}")
def suma(a: int, b: int = 0, c: int = None):
    if b == 0 and c is None:
        print(f"El resultado es {a}")
    elif c is None:
        print(f"La suma de {a} + {b} es {a + b}")
    else:
        print(f"La suma de {a}, {b} y {c} es {a + b + c}")

def promedioArreglo(lista):
    lista.append(5)
    lista.append(45)
    lista.append(56)
    p=mate.mean(lista)
    print(f"El promedio es {p}")


if __name__ == '__main__':
    suma(10)
    suma(23, 47)
    suma(12)

    lista2=[1,2,3,4,5]
    # lista2=lista1
    promedioArreglo(lista2)
    #La lista saldra del metodo alterado
    print(lista2)
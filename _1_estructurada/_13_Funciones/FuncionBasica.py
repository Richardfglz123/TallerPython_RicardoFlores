def suma(a: int, b: int) -> int:
    return a + b

def suma_arreglo(lista: list) -> int:
    return sum(lista)

if __name__ == '__main__':
    print(f"La suma es {suma(15, 22)}")
    lista = [1, 2, 3, 4, 5]
    print(f"La suma del arreglo es {suma_arreglo(lista)}")

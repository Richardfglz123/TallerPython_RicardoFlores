if __name__ == '__main__':
    x=int(input("Ingresa un numero: "))
    y=int(input("Ingresa la multiplicacion: "))

    i: int =1;
    pot:int=0;

    while y>0:
        pot+=x;
        y-=1;

    print(f"multiplicacion de {x} * {y} = {pot}")

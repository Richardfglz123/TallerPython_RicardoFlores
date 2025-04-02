import json
import sys


RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def extrae():
    with open("EdadesBD.json", "r", encoding="utf-8") as archivo:
        EdadesBD = json.load(archivo)

    i = 1
    for elemento in EdadesBD["tabla"]:
        match i:
            case 1:
                sys.stdout.write(RED)
            case 2:
                sys.stdout.write(GREEN)
            case 3:
                sys.stdout.write(YELLOW)
            case _:
                sys.stdout.write(RESET)

        yield (elemento["id"], elemento["Nombre"], elemento["Edad"], elemento["RFC"])


if __name__ == '__main__':
    for id, nombre, edad, rfc in extrae():
        print("---------------------------")
        print(f"id: {id}")
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"RFC: {rfc}")

        if isinstance(edad, int):
            if edad >= 18:
                print(f"{GREEN}Status: Mayor de edad{RESET}")
            else:
                print(f"{RED}Status: Menor de edad{RESET}")
        else:
            print(f"{YELLOW}Status: Edad no válida o no especificada{RESET}")

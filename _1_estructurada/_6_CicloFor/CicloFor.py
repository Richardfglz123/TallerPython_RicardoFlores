import sys
if __name__ == '__main__':

    print("Rango de 0 a 9")
    for i in range(10):
        print(f"{i}")

        print("Rango de 6 a 11")
        for i in range(6,12):
            print(f"{i}")

    print("Rango de 6 a 11 pero con incrementos de 3")
    for i in range(6, 12, 3):
        print(f"{i}", end=" ")

sys.stdout.write("Teto sin salto de linea")


if __name__ == '__main__':
    palabra: str = "%s"

    lista: list = ["nombre", "apellido_paterno", "apellido_materno", "edad","correo_electronico", "contrasennia"]

    print(palabra)
    # palabra = palabra * 5
    print(palabra)

    t = len(lista)
    print(t)
    palabra = palabra * len(lista)
    print(palabra)

    campos = " , ".join(lista)
    print(campos)

    querrySQL=f"INSERT INTO tabla ({campos} VALUES (%s,%s,%s) "
    print(querrySQL)


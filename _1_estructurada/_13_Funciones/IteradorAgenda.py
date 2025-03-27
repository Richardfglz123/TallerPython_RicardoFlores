def extrae(agenda: list):
    i: int = 0
    while i < len(agenda):
        nombre, correo, tel = agenda[i]
        i += 1
        yield nombre, correo, tel

if __name__ == '__main__':
    agenda = []
    agenda.append(("Juann ", "juan0@gmail.com", "248123450"))
    agenda.append(("Juann2 ", "juan1@gmail.com", "248123451"))
    agenda.append(("Juann3 ", "juan2@gmail.com", "248123452"))
    agenda.append(("Juann4 ", "juan3@gmail.com", "248123453"))
    agenda.append(("Juann5 ", "juan4@gmail.com", "248123454"))
    agenda.append(("Juann6 ", "juan5@gmail.com", "248123455"))
    agenda.append(("Juann7 ", "juan6@gmail.com", "248123456"))
    agenda.append(("Juann8 ", "juan7@gmail.com", "248123457"))
    agenda.append(("Juann9 ", "juan8@gmail.com", "248123458"))
    agenda.append(("Juann9 ", "juan9@gmail.com", "248123459"))

    for a, b, c in extrae(agenda):
        print(f"Nombre: {a}, Correo: {b}, Teléfono: {c}")
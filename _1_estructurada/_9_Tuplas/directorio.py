if __name__ == '__main__':
    agenta = {}

    agenta["GOAT800717"] = ("Tomas Gonzalez", "csctomasgonzalez@gmail.com", "22280")
    agenta["GOAT800718"] = ("Iker Gonzalez", "Ikergon@gmail.com", "22281")
    agenta["GOAT800719"] = ("Alfonso", "Alfonsouwu@gmail.com", "22282")
    agenta["GOAT800720"] = ("Si uwu", "Alfonsouwu@gmail.com", "22282")

    nombre, correo, numero = agenta["GOAT800717"]
    print(f"Name: {nombre}, Email: {correo}, Number: {numero}")

    nombre, correo, numero = agenta["GOAT800718"]
    print(f"Name: {nombre}, Email: {correo}, Number: {numero}")

    nombre, correo, numero = agenta["GOAT800719"]
    print(f"Name: {nombre}, Email: {correo}, Number: {numero}")

    nombre, correo, numero = agenta["GOAT800720"]
    print(f"Name: {nombre}, Email: {correo}, Number: {numero}")

    print("Agenda")
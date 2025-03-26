if __name__ == '__main__':
    #Usar una tupla como clave en un diccionario '
#diccionario = {
   # ("id", "int"): '2',
  #  'nombre' : 'Juan',
 #   'apellido' : 'Gutierrez'
#    } RFC, tupla: nombre comleto y telefono
    diccionario={}
    #Agregar tupla como clave
    diccionario[("Ana", 25)] = "Estudiante"
    diccionario[("Luis", 25)] = "Ingeniero"
    diccionario[("Carlos", 25)] = "Abogado"

    #Agregar a los valores del diccionario usando la tupla
    ocupacion_ana = diccionario[("Ana", 25)]
    ocupacion_luis = diccionario[("Luis", 25)]

    print(f"Ana es: {ocupacion_ana}")
    print(f"Luis es: {ocupacion_luis}")

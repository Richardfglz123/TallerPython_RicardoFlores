import json

if __name__ == '__main__':
    #Version corta dea brir un archivo Json
    # Abre el archivo JSON en modo lectura y with se encarga de cerrar
    with open("datos.json","r", encoding="utf-8") as archivo:
        datos = json.load(archivo) #Carga el contenido del archivo JSON

        #Muestra el contenido del JSON
        for persona in datos["Personas"]:
            print("Nombre:", persona["Nombre"])
            print("Edad:", persona["edad"])
            print("Ciudad:", persona["ciudad"])
            print("Estado:", persona["estado"])
            print("---------------------------")#Para seaprar

import configparser
import sys

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    #Verifica que las secciones y claves existan
    if ('Maximus' in config and 'basedatos' in config['Maximus'] and 'usuario' in config ['Maximus'] and 'contrasennia' in config ['Maximus']):
        bd = config ['Maximus']['Basedatos']
        user = config['Maximus']['Usuario']
        password = config['Maximus']['contrasennia']
        print(bd,user, password)

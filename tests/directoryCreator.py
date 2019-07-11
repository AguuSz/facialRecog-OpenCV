import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)

    except OSError:
        print("Error: Error creando el directorio en " + directory)

# Creacion de la carpeta
path = os.path.join('Ascensor para gente ciega', 'Personas')
createFolder(path)

print("Creada con exito!")

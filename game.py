# Juego de adivinar la palabara utilizando la voz

import speech_recognition as sr
import random
import time

# Inicializando el microfono
r = sr.Recognizer()
mic = sr.Microphone()
print("Cargando lo necesario...")


#Creando la lista de palabras a utilizar
palabras = ["apple", "orange", "banana", "watermelon", "kiwi"]
palabra_random = palabras[random.randint(0,5)]
print("La palabra aleatoria se ha generado! Intente adivinar si es Apple, Orange, Banana, Watermelon o kiwis.")
print("Buena suerte!")

while True:
    with mic as source:
        print("/nHable")
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio)
        print(texto)

        if texto == palabra_random:
            print("Felicitaciones! Haz acertado!!")
            time.sleep(2)
            print("Ahora se procedera a cerrar el programa")
            break
        elif texto == "stop":
            print("Haz dicho stop, por lo que se cerrara el programa. Gracias por jugar!")
            print("Cerrando...")
        elif texto == "what's the word":
            print(palabra_random)
        else:
            print("Palabra equivocada! Sigue intentando")
    except sr.UnknownValueError:
        print("No se ha entendido lo que haz dicho, intentalo de nuevo!")

    except sr.RequestError:
        print("No dispones de una conexion a internet. Intentalo de nuevo cuando estes conectado!")
        print("Cerrando...")
        break



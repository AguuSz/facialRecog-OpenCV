# Archivo encargado del reconocimiento de voz V1.0 || Solo funciona en ingles por el momento

import speech_recognition as sr

r = sr.Recognizer()

# Creando la instancia de microfono
mic = sr.Microphone()

while True:
    with mic as source:
        # Quitar comentario de la linea de abajo cuando se este trabajando en un ambiente muy ruidoso
        print("Espere un segundo")
        r.adjust_for_ambient_noise(source)
        print("Hable")
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio, language="es-ES")
        print("Dijiste: " + texto)
        if texto == "cerrar programa":
            print("Cerrando...")
            break
    except sr.UnknownValueError:
        print("No se entendio")
    except sr.RequestError:
        print("No se pudo acceder a una conexion de internet... Verifica tu conexion e intentalo de nuevo!")

# Archivo encargado del reconocimiento de voz V1.0 || Solo funciona en ingles por el momento

import speech_recognition as sr

r = sr.Recognizer()

# Creando la instancia de microfono
mic = sr.Microphone()

GOOGLE_CLOUD_SPEECH_CREDENTIALS = "../Ascensor para ciegos-f943c0d8d19e.json"

while True:
    with mic as source:
        # Quitar comentario de la linea de abajo cuando se este trabajando en un ambiente muy ruidoso
        print("Hable")
        audio = r.listen(source)

    try:
        texto = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
        print("Dijiste: " + texto)
        if texto == "cerrar programa":
            print("Cerrando...")
            break
    except sr.UnknownValueError:
        print("No se entendio")
    except sr.RequestError:
        print("No se pudo acceder a una conexion de internet... Verifica tu conexion e intentalo de nuevo!")

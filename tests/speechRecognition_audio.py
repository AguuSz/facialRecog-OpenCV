import speech_recognition as sr

# Creando el objeto reconocedor
r = sr.Recognizer()


harvard = sr.AudioFile("speech_recog_files/harvard.wav")
with harvard as source:
    audio = r.record(source)

# Se va a abrir el archivo y guardar su contenido, guardando la data en una instancia de archivo de audio llamada source (en este caso). Luego el metodo record() graba la data del archivo dentro de una instancia AudioDat

texto_interpretado = r.recognize_google(audio)
print(texto_interpretado)

import speech_recognition as sr

r = sr.Recognizer()

# Creando la instancia de microfono
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

texto = r.recognize_google(audio)

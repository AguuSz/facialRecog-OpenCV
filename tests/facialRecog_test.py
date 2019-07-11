import face_recognition
import cv2
import numpy as np
import os

# Empezar a capturar video de la camara web 0 (la que viene)
video_capture = cv2.VideoCapture(0)

# Que revise cuantos archivos hay dentro de la carpeta
cantidadImagenes = len(os.listdir("./data_img"))
nombreArchivos = os.listdir('./data_img')

for i in cantidadImagenes:
    cont = 0
    archivo = nombreArchivos[cont]

    contFace = face_recognition.load_image_file(archivo)
    contFace_encoding = face_recognition.face_encoding(contFace)[0]
    cont =+ 1

# Cargue otra imagen de entrenamiento y que aprenda a reconocerla
chad = face_recognition.load_image_file('./data_img/chad.jpeg')
chad_encoding = face_recognition.face_encodings(chad)[0]

# Cargue otra imagen de entrenamiento y que aprenda a reconocerla
will = face_recognition.load_image_file('./data_img/will.jpeg')
will_encoding = face_recognition.face_encodings(will)[0]

# Cargue otra imagen de entrenamiento y que aprenda a reconocerla
marcos = face_recognition.load_image_file('./data_img/marcos.jpeg')
marcos_encoding = face_recognition.face_encodings(marcos)[0]

# Cargue otra imagen de entrenamiento y que aprenda a reconocerla
valen = face_recognition.load_image_file('./data_img/valen.jpeg')
valen_encoding = face_recognition.face_encodings(valen)[0]


# Crear una array con los encodings de las caras y sus nombres
known_face_encodings = [
    chad_encoding,
    will_encoding,
    marcos_encoding,
    valen_encoding
]
known_face_names = [
    "Chad",
    "Will",
    "Marcos",
    "Valen"
]

# Inicializar algunas variables (aunque no es muy necesario, lo hago para ver que variables voy a usar)
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Toma un solo frame de video
    ret, frame = video_capture.read()

    # Cambia el tamaño del frame a 1/4 para que el procesamiento sea mas rapido
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Convierte la imagen de un perfil BGR a RGB (que face_recognition usa)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Solo procesa cada otro frame del video para ahorrar tiempo
    if process_this_frame:
        # Encuentra todas las caras y los encodings del frame actual del video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Mira si el rostro hace match con alguna de los rostros conocidos, sino le da el nombre de "Desconocido"
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Desconocido"

            # Usa el rostro conocico y le da el nombre correspondiente
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            # Funcion IF donde se le aplica el accionamiento al reconocer el rostro
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Que muestre los resultados
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Volver a resolucion original el frame, ya que el que detectamos estaba a 1/4
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2

        # Dibujar una caja alrededor de la cara
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Dibujar un campo de texto con el nombre de la persona abajo
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 145), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.7, (255, 255, 255), 1)

    # Que muestre la imagen final
    cv2.imshow('Video', frame)

    # Apretar Q para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

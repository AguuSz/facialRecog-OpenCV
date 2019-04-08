import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {}
with open("labels.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v: k for k, v in og_labels.items()}

cap = cv2.VideoCapture(0)

while (True):
    # Que capture el frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Para reconocer necesitamos un modelo de prediccion /keras /tensorflor /pytorch / sickit-learn
        id_, conf = recognizer.predict(roi_gray)
        if conf >= 45:  # and conf <= 85:
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_gray)

        color = (255, 0, 0)  # El color esta en BGR
        grosor = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, grosor)

    # Muestre el frame resultado
    cv2.imshow("Frame", frame)

    # Si apretamos la Q en el frame, va a exitear
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Cuando este todo terminado, que lanze la captura
cap.release()
cv2.destroyAllWindows()

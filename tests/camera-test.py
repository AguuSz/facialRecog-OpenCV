import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    # Que capture el frame-by-frame
    ret, frame = cap.read()

    # Muestre el frame resultado
    cv2.imshow("Frame", frame)

    # Si apretamos la Q en el frame, va a exitear
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Cuando este todo terminado, que lanze la captura
cap.release()
cv2.destroyAllWindows()

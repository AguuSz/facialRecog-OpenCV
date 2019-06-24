import urllib
import cv2
import numpy as np
import time

#Importando la url
url = "http://192.168.1.37:8080/"

while True:

    #Usar urlLib para capturar la imagen y convertirla en un formato legible para cv2

    imgResp = urllib.urlopen
    (url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)

    #Mostrar imagen
    cv2.imshow("Camara del celular", img)

    #Darle menos presion al procesador
    #time.sleep(0.1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

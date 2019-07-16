import face_recognition as fr
import cv2
import sys
import _pickle as pk

'''
command line args: imgfile, name_of_person_in_image
'''

s, img, name = sys.argv

if img == "cam":
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        cv2.imshow('Presiona A para guardar su rostro', frame)
        if cv2.waitKey(10) & 0xFF == ord('a'):
            cv2.imwrite(name + '.jpg', frame)
            cv2.destroyAllWindows()
            break



    
cap.release()
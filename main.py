import cv2
from PIL import Image
import numpy as np
from resource import get_limits
#color detection

yellow=[0,255,255] #yellow en rgb
camera= cv2.VideoCapture(0)
while True:#creo bucle para la camara
    ret, frame =camera.read()
    #con esto paso a un sis. de color vectorizado
    hsv_image =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #con esto selecciono el rango de color que quiero tomar
    lowerLimit,upperLimit = get_limits( color=yellow )
    mask =cv2.inRange(hsv_image,lowerLimit ,upperLimit)

    #proceso para crear una caja
    #convertir de un arreglo numpy en pillow (solo cambio el formato)
    mask_= Image.fromarray(mask)
    box = mask_.getbbox()
    #para dibujar la caja
    if box is not None:
        x1,y1,x2,y2 = box
        frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),8)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release() #libero la memoria de la camara
cv2.destroyAllWindows()


import cv2 as cv
import numpy as np

cap = cv2.VideoCapture(0)  # Inicio de captura
cont=0
while 1:
    _, frame = cap.read()  # Almacenamiento del frame
    height, width = frame.shape[:2]  # Captura de las dimensiones
    segImg1 = np.zeros(frame.shape, np.uint8)  # Creacion de la imagen vacia para la segmentacion 1
    segImg2 = np.zeros((height, width), np.uint8)# Creacion de la imagen vacia para la segmentacion 2
    conv = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)# Se convierte el frame de entrada a YCrCb

    lower  = np.array([0, 210, 50],np.float32)#Limite inferior color rojo
    upper  = np.array([255, 255, 150],np.float32)#Limite superior color rojo
    # Creaion de la mascara con los rangos a segmentar
    mask = cv2.inRange(conv, lower, upper)  

    # Aplicación de la segmentacion de los colores 
    segImg1 = cv2.bitwise_and(conv, conv, mask=mask) 
    imgray = cv2.cvtColor(segImg1,cv2.COLOR_BGR2GRAY) 
    t2, imgbi = cv2.threshold (imgray, 0, 255, cv2.THRESH_BINARY| cv2.THRESH_TRIANGLE) 
    
    for i in range(0, 240):
        for j in range(0, 320):
            if imgbi[i, j] ==255:
                #cont=cont+1
                #if cont==30:
                print("Alto")
                    #break
                break 
    #Visualización de las imagenes
    cv2.imshow('Original', frame)
    cv2.imshow('rojo', segImg1)  
    cv2.imshow('gris',imgbi)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

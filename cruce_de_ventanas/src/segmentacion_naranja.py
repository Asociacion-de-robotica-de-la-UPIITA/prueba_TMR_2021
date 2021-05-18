#!/usr/bin/env python
#importamos la biblioteca de rospy
import rospy
#importamos el tipo de mensaje Image de la biblioteca sensor_msgs.msg
from sensor_msgs.msg import Image
#importamos los puentes necesarios para obtener la imagen desde ros
from cv_bridge import CvBridge, CvBridgeError
#importamos openCV 2
import cv2
class LoadImage(object):

    def __init__(self):
        #renombrar nombre del nodo donde se obtiene la imagen (si es necesario)
        self.image_sub = rospy.Subscriber("/ardrone/image_raw",Image,self.camera_callback)
        #importamos el puente de CV
        self.bridge_object = CvBridge()

    def camera_callback(self,data):
        try:
            # Seleccionamos bgr8 por que es el formato que maneja openCV por defecto
            imagenBRG = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
            #Entonces mi imagen para tratar en tiempo real es imagenBRG
        except CvBridgeError as e:
            #En caso de error, imprime e
            print(e)

        #cambiamos la codificacion de brg a hsv en una nueva imagen 
        cv_image= cv2.cvtColor(imagenBRG, cv2.COLOR_BGR2HSV)

        #definimos umbrales para segmentacion por colores HSV
        umbral_bajo_naranja = (0,100,100)
        umbral_alto_naranja = (25,255,255)
        #creamos la mascara con la imagen en HSV y los umbrales bajo y alto
        mask = cv2.inRange(cv_image, umbral_bajo_naranja, umbral_alto_naranja)
        #creamos una imagen de respuesta de la mascara obtenida con la imagen HSV
        res = cv2.bitwise_and(cv_image, cv_image, mask=mask)
        #convertimos la imagen de respuesta de hsv a bgr
        res_bgr= cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
        #Abrimos una nueva ventana que nos muestre la imagen original tomada en tiempo real 
        cv2.imshow('Imagen BGR',imagenBRG)
        #Abrimos una nueva ventana que nos muestre la imagen en HSV en tiempo teal
        #cv2.imshow('Imagen HSV',cv_image)
        #Abrimos una nueva ventana que nos muestre la mascara en tiempo real
        #cv2.imshow('mascara',mask)
        #Abrimos una nueva ventana que nos muestre la imagen de respuesta en BGR
        cv2.imshow('salida BGR',res_bgr)
        #Abrimos una nueva ventana que nos muestre la imagen de respuesta en HSV
        #cv2.imshow('salida HSV',res)

        cv2.waitKey(1)

def main():
    load_image_object = LoadImage()
    rospy.init_node('imagen_segmentada', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
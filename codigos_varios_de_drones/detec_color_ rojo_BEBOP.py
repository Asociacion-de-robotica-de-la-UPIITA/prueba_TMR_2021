#DETECTAR LUZ ROJA USANDO LA CAMARA DEL BEBOP
#PRIMER PROGRAMA 
import cv2
import numpy as np
import cv_bridge
from std_msgs.msg import Int32
from geometry_msgs.msg import Pose
#----------------------------------------------------

import torch
x = torch.rand(5, 3)
print(x)


def callback(msg):
	pose_ventana = Pose()
	bridge = cv_bridge.CvBridge()
	cap = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
 
	#cap = cv2.VideoCapture(0)  # Inicio de captura
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

  #Aqui se suscribe a la camara del BEBOP??????
def detect_objeto():
	msg = rospy.Subscriber('bebop/image_raw', Image, callback, queue_size = 10)



if __name__ == '__main__':
	detect_objeto()
	rospy.init_node('ventana_node', anonymous = False)
	pub = rospy.Publisher('publish_ventana', Pose, queue_size=10)
	rate = rospy.Rate(10);
	rospy.spin()

cap.release()
cv2.destroyAllWindows()

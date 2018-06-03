import numpy as np
import cv2

def detect_face(path):
	face_cascade = cv2.CascadeClassifier('/home/ntan/Desktop/a/face_detection/cvdata/haarcascade_frontalface_default.xml')
	img = cv2.imread(path)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE
	)

	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
	cv2.imwrite(path, img)
	return faces
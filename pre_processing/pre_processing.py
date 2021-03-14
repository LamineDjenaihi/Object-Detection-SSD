import cv2

def pre_processing(img):
	#-----resize image---------------------------------------------------------
	img = cv2.resize(img,(300,300),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
	return img
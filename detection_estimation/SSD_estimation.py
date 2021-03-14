import sys 
sys.path.append("C:\\Users\\lamin\\Desktop\\PFE\\traffic_objetct_detection")
from pre_processing.pre_processing import pre_processing
from distance_estimate.calcul_estimate import dist_calculator
from load_modelSSD300.load_modelSSD300 import model_detection
from playsound import playsound
import cv2 
import math
import time
from scipy.misc import imread
from math import sqrt,sin
import numpy as np
import keyboard 
class SSD_estimation_img():
	def __init__(self,model):
		self.model= model
		self.Width=300
		self.Height=300
		self.classes=['arriere_plan', 'voiture', 'camion', 'pieton', 'bicyclette','feu_circulation', 'motocycle', 'bus', 'panneau_stop']
	

	
	

	def prediction_img(self,filename):

		inputs = []
		img = cv2.imread(filename)
		img=pre_processing(img)
		img1 = np.asarray(img)
		inputs.append(img1.copy())
		inputs = np.array(inputs)
		y_pred = self.model.predict(inputs)

		# Decode the raw prediction.

		i = 0

		confidence_threshold = 0.5

		y_pred_thresh = [y_pred[k][y_pred[k,:,1] > confidence_threshold] for k in range(y_pred.shape[0])]

		np.set_printoptions(precision=2, suppress=True, linewidth=90)
		print("Predicted boxes:\n")
		print('    class    conf  xmin    ymin    xmax    ymax')
		print(y_pred_thresh[0])


		classes = ['arriere_plan', 'voiture', 'camion', 'pieton', 'bicyclette',
				'feu_circulation', 'moto', 'bus', 'panneau_stop'] # Just so we can print class names onto the image instead of IDs

		# Draw the predicted boxes in blue
		for box in y_pred_thresh[i]:
			class_id = box[0]
			confidence = box[1]
			xmin = box[2]
			ymin = box[3]
			xmax = box[4]
			ymax = box[5]
			color = (255, 0, 0)
			cls_name=self.classes[int(class_id)] 
			if (cls_name is 'panneau_stop' or cls_name is 'feu_circulation'):
				color= (0, 0, 255)
			else:
				color= (255, 0, 0)
			
			distance = dist_calculator(xmin,ymin,xmax,ymax)
			distance/=12.
			if(distance<=0):
				distance=0
			#cls_name=self.classes[int(class_id)]
			#draw_box 
			colorT = (255, 255, 255)
			tl = round(0.002 * max(img.shape[0:2])) + 1  # line thickness
			c1, c2 = (int(xmin), int(ymin)), (int(xmax), int(ymax))
			cv2.rectangle(img, c1, c2, color, thickness=tl)
			text = "{}: {:.2f}|{:.3f} ".format(cls_name, confidence,distance)+"metre"
			# draw text
			tf = max(tl - 1, 1)  # font thickness
			t_size = cv2.getTextSize(text, 0, fontScale=tl / 8, thickness=tf)[0]
			c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
			cv2.rectangle(img, c1, c2, color, -1)  # filled
			cv2.putText(img, text, (c1[0], c1[1] - 2), 0, tl / 8, colorT, thickness=tf, lineType=cv2.LINE_AA)
		return img




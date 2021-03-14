import sys 
sys.path.append("C:\\Users\\lamin\\Desktop\\PFE\\traffic_objetct_detection")

from pre_processing.pre_processing import pre_processing
from distance_estimate.calcul_estimate import dist_calculator
from playsound import playsound
import cv2 
import math
import time
from scipy.misc import imread
from math import sqrt,sin
import numpy as np
import keyboard
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt,QThread
from PyQt5.QtGui import QPixmap, QImage, QColor
class SSD_estimation_video():
	#change_pixmap_signal = pyqtSignal(np.ndarray)
	def __init__(self,model,video_cap,name):
		super().__init__()
		self.model= model
		self.Width=300
		self.Height=300
		self.classes=['arriere_plan', 'voiture', 'camion', 'pieton', 'bicyclette','feu_circulation', 'motocycle', 'bus', 'panneau_stop']
		self.video_cap=video_cap
		self.fps=0.0
		self.name=name
		self._run_flag=True

   

	def run(self):
		#V_I=
		classes = self.classes # Just so we can print class names onto the image instead of ID
		video_input = cv2.VideoCapture(self.video_cap)
		self.fps=video_input.get(5)
		s=0
		while self._run_flag:
			inputs=[]
			ret_val, frame = video_input.read()
			if ret_val: 
				#img = cv2.flip(frame, 1)
				img=pre_processing(frame)
				img1 = np.asarray(img)
				inputs.append(img1.copy())
				inputs = np.array(inputs)
				y_pred = self.model.predict(inputs)
				i = 0
				confidence_threshold = 0.5
					
				y_pred_thresh = [y_pred[k][y_pred[k,:,1] > confidence_threshold] for k in range(y_pred.shape[0])]
				np.set_printoptions(precision=2, suppress=True, linewidth=2)
				# Draw the predicted boxes in blue
				print("Predicted boxes:\n")
				print('    class    conf  xmin    ymin    xmax    ymax')
				print(y_pred_thresh[0])
				for box in y_pred_thresh[i]:
					class_id = box[0]
					confidence = box[1]
					xmin = box[2]
					ymin = box[3]
					xmax = box[4]
					ymax = box[5]
					cls_name=self.classes[int(class_id)]
					distance = dist_calculator(xmin,ymin,xmax,ymax)
					distance/=12.
					if(distance<=0):
						distance=0
					color = (255, 0, 0) 
					colorT = (255, 255, 255)#and (distance!=distance_old)
					if ((cls_name is 'panneau_stop' or cls_name is 'feu_circulation') ):
						color= (0, 0, 255)
						#while():
						if(s<=3):
							playsound('C:\\Users\\lamin\\Desktop\\PFE\\traffic_objetct_detection\\sonore\\Store_Door_Chime-Mike_Koenig-570742973.wav')
							s+=1
						else:
							time.sleep(30)
							s=0
					else:
						color= (255, 0, 0)
					#draw_bx 
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
			cv2.imshow(self.name, img)
			if cv2.waitKey(1) == 27: 
				break  # esc to quit				
			#prev = time.time()
		#video_input.release()	
		cv2.destroyAllWindows()	
'''
def main():
	ssdd=SSD_estimation_video(None,2)
	ssdd.run()
if __name__ == '__main__':
	main()
'''




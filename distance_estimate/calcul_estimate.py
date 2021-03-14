import math
# Function to calculate the distance of object from the camera lense
def dist_calculator(startX,startY,endX,endY):
	box_width=int (endX-startX)
	box_height=int (endY-startY)
	
	distance = (2*3.14*180)/((box_width+box_height)*360)*1000+3
	
	return distance


	

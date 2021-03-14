'''
import cv2

V_O="C:\\Users\\lamin\\Desktop\\traffic_objetct_detection\\output1.avi"
video_output= cv2.VideoCapture(V_O) 
# Check if camera opened successfully
if (video_output.isOpened()== False):
  print("Error opening video stream or file")
# Read until video is completed
while (video_output.isOpened()):
    # Capture frame-by-frame
    ret, frame = video_output.read()
    if ret == True:
 
        # Display the resulting frame
        cv2.imshow('Frame', frame)
 
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
 
    # Break the loop
    else:
        break

import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
importnumpy as np

class App:
    def __init__(self, window, window_title, video_source=''):
        self.window = window
        self.window.title(window_title)        
        self.video_source = video_source
        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture('http://192.168.1.2:4747/video')
        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack() 
        # Button that lets the user take a snapshot
        self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)
        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update() 
        self.window.mainloop()

    def snapshot(self):
            # Get a frame from the video source
            ret, frame = self.vid.get_frame()
            if ret:
                cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    def update(self):
            # Get a frame from the video source
            ret, frame = self.vid.get_frame()
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
                self.window.after(self.delay, self.update)

class MyVideoCapture:
    def __init__(self, video_source=''):
        # Open the video source
        self.vid = cv2.VideoCapture('http://192.168.1.2:4747/video')
        self.width = self.vid.get(3)
        self.height = self.vid.get(4)
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return  (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)
    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

V_O="C:\\Users\\lamin\\Desktop\\traffic_objetct_detection\\output1.avi"
# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV",video_source='http://192.168.1.2:4747/video')
#vid = MyVideoCapture()
#print(vid.get_frame)

import numpy as np
import cv2
from playsound import playsound
while(True):
    playsound('C:\\Users\\lamin\\Desktop\\traffic_objetct_detection\\Store_Door_Chime-Mike_Koenig-570742973.wav')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap = cv2.VideoCapture(2)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps=cap.get(5)
print(width,height,fps)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',np.array(gray, dtype = np.uint8 ))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

import cv2
#f = "C:\\Users\\lamin\\Desktop\\traffic_objetct_detection\\GTSDB\\{}".format(f)
#-----Reading the image-----------------------------------------------------
img = cv2.imread('C:\\Users\\lamin\\Desktop\\traffic_objetct_detection\\GTSDB\\00890.jpg', 1)
cv2.imshow("img",img) 
cv2.waitKey(0)
cv2.destroyAllWindows()
#-----Converting image to LAB Color model----------------------------------- 
lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#cv2.imshow("lab",lab)

#-----Splitting the LAB image to different channels-------------------------
l, a, b = cv2.split(lab)
#cv2.imshow('l_channel', l)
#cv2.imshow('a_channel', a)
#cv2.imshow('b_channel', b)

#-----Applying CLAHE to L-channel-------------------------------------------
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
cl = clahe.apply(l)
#cv2.imshow('CLAHE output', cl)

#-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
limg = cv2.merge((cl,a,b))
#cv2.imshow('limg', limg)

#-----Converting image from LAB Color model to RGB model--------------------
final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
cv2.imshow('final', final)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.destroyAllWindows()
#_____END_____#
'''

import cv2


def show_webcam(mirror=False):
    cam = cv2.VideoCapture(2)
    while True:
        ret_val, img = cam.read()
        if ret_val: 
            img = cv2.flip(img, 1)
            cv2.imshow('my webcam', img)
            if cv2.waitKey(1) == 27: 
                break  # esc to quit
        
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()


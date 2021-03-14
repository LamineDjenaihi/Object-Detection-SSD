
import sys 
sys.path.append("C:\\Users\\lamin\\Desktop\\PFE\\traffic_objetct_detection")
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap, QImage, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QFrame,QVBoxLayout,QMenuBar
from PyQt5.QtGui import QIcon
from detection_estimation.SSD_estimation import SSD_estimation_img
from detection_estimation.SSD_estimation_video import SSD_estimation_video
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt,QObject
from load_modelSSD300.load_modelSSD300 import model_detection
import os
import numpy as np
import cv2
class window2(QMainWindow):
   def __init__(self):
      super().__init__()
      self.model= model_detection()
      #self.predict_video=SSD_estimation_video()
      self.display_width=300
      self.display_height=300
      stylesheet="QPushButton{background-color: rgb(200,200,200);border: 1px solid gray;color: black;padding: 15px 32px;text-align: center;text-decoration: none;font-size: 16px;font-weight: bold;border-radius: 12px;}""QPushButton:pressed { background-color: (200,200,200) }"
      
      self.widget = QWidget()
      self.widget.setStyleSheet("background-color: rgb(250,250,250)")#rgb(195,134,134)pink;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;
      self.widget.setGeometry(100,100,680,480)#rgb(150,150,150)
      self.setWindowTitle("système D&E")
      self.setFixedSize(680, 480) 
      grid_layout = QGridLayout()
      
      vbox1 = QVBoxLayout()
      vbox2 = QVBoxLayout()
      vbox3 = QVBoxLayout()
      hbox=QHBoxLayout()
      ImgAct = QAction('&Importer Image', self)
      ImgAct.setShortcut('Ctrl+F')
      ImgAct.setStatusTip('Importer Image')
      ImgAct.triggered.connect(self.image)
      VidAct = QAction('&Importer une video', self)
      VidAct.setShortcut('Ctrl+U')
      VidAct.setStatusTip('Importer une video')
      VidAct.triggered.connect(self.video_up)
      LivAct = QAction('&Video en direct', self)
      LivAct.setShortcut('Ctrl+E')
      LivAct.setStatusTip('Video en direct')
      LivAct.triggered.connect(self.video_live)
      exitAct = QAction('&Quitter', self)
      exitAct.setShortcut('Ctrl+Q')
      exitAct.setStatusTip('Quitter')
      exitAct.triggered.connect(QCoreApplication.instance().quit)

      self.menubar = QMenuBar()
      self.menubar.setStyleSheet("background-color: rgb(250,250,250)")
      actionFile = self.menubar.addMenu("fichier")
      actionFile.addAction(ImgAct)
      actionFile.addAction(VidAct)
      actionFile.addAction(LivAct)
      actionFile.addAction(exitAct)
      #actionFile.addSeparator()
      #self.menubar.addMenu(exitAct)
      
      button1 = QPushButton(self.widget)
      button1.setText("Importer une image")
      button1.clicked.connect(self.image)
      button1.setStyleSheet(stylesheet)
      button1.setFixedWidth(250)
      button2 = QPushButton(self.widget)
      button2.setText("Importer une video")
      
      button2.clicked.connect(self.video_up)
      button2.setStyleSheet(stylesheet)
      button2.setFixedWidth(250)
      button3 = QPushButton(self.widget)
      button3.setText("Video en direct")
      
      button3.clicked.connect(self.video_live)
      button3.setStyleSheet(stylesheet)
      button3.setFixedWidth(250)
      button4 = QPushButton(self.widget)
      button4.setText("Quitter")
      
      button4.clicked.connect(QCoreApplication.instance().quit)
      button4.setStyleSheet(stylesheet)
      button4.setFixedWidth(250)
      
      self.image_label = QLabel(self)
      self.image_label.setStyleSheet("border: 10px solid darkgrey;") 
      self.image_label.setFixedWidth(300)
      self.textLabel = QLabel('Ecran')
       
      self.screen = QPixmap(self.display_width, self.display_height)
      self.screen.fill(QColor('Black'))
      
      
       
      self.image_label.setPixmap(self.screen)
      vbox1.addWidget(self.menubar)
      vbox2.addWidget(self.textLabel)
      vbox2.addWidget(self.image_label)
      vbox3.addWidget(button1)
      vbox3.addWidget(button2)
      vbox3.addWidget(button3)
      vbox3.addWidget(button4)
      grid_layout.addLayout(vbox1,0,0)
      grid_layout.addLayout(vbox2,1,2)
      grid_layout.addLayout(vbox3,1,0)
      
      
      self.widget.setLayout(grid_layout)
      
      self.setCentralWidget(self.widget)
      self.show()
      
      

   def convert_cv_qt(self,cv_img):
      """Convert from an opencv image to QPixmap"""
      rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
      h, w, ch = rgb_image.shape
      bytes_per_line = ch * w
      convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
      p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
      return QPixmap.fromImage(p)

   def image(self):
      dialog = QFileDialog()

      options = dialog.Options()
      #options |= dialog.DontUseNativeDialog
      files, dd = dialog.getOpenFileNames(None,"IMAGE", "","JPEG(*.jpg *.jpeg);;PNG(*.png)")
      print(files)
      if(dd):
            prediction_img=SSD_estimation_img(self.model)
            cv_img=prediction_img.prediction_img(files[0])
            qt_img = self.convert_cv_qt(cv_img)
            # display it
            self.image_label.setPixmap(qt_img)
      else:
            pass
   def video_up(self):
      dialog = QFileDialog()

      options = dialog.Options()
      #options |= dialog.DontUseNativeDialog
      files, dd = dialog.getOpenFileNames(None,"VIDEO", "","MP4(*.mp4)")#, options=options
      
      if(dd):
            self.screen.fill(QColor('Black'))
            self.image_label.setPixmap(self.screen)
            predict_vid = SSD_estimation_video(self.model,files[0],'Video')
            predict_vid.run()
      else:
            pass

   def video_live(self):
      #dialog = QFileDialog()
            self.screen.fill(QColor('Black'))
            self.image_label.setPixmap(self.screen)
            predict_live = SSD_estimation_video(self.model,1,'live_webcam')
            predict_live.run()
            if(predict_live.fps==0.0):
                  print("Aucune Camera!!")
                  
   

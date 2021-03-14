import sys 
sys.path.append("C:\\Users\\lamin\\Desktop\\PFE\\traffic_objetct_detection")
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from interface.design2 import window2
class window1(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.widget = QWidget()
		text1="Le système du detection des objets et estimation de distance "
		text2="le système peut détecter des objets du cicrculation routière tel que:\n"+"voiture,bus,motociycle,bicycelette,camion,piéton,feu du circulation,panneau STOP.\n"+"Et il peut estimer la distance entre la caméra et l'objet détecté.\n"
		text3="Remarque:"
		text4="quand le système détecte un panneau STOP ou un feu du circulation dans une vidéo, il lance une sonore."
		stylesheet1="background-color: rgb(50,255,50);color:white;font-size: 16px;font-weight: bold;border-radius: 12px;"
		stylesheet2="background-color: rgb(255,50,50);color:white;font-size: 16px;font-weight: bold;border-radius: 12px;"
		self.widget.setStyleSheet("background-color: rgb(250,250,250)")#rgb(195,134,134)pink;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;
		#widget.setGeometry(100,100,680,480)#rgb(150,150,150)
		self.setWindowTitle("système D&E")
		self.setFixedSize(680, 480)
		grid_layout = QGridLayout()
		vbox1 = QVBoxLayout()
		vbox2 = QHBoxLayout()
		button1 = QPushButton(self.widget)
		button1.setText("Lancer")
		button1.clicked.connect(self.switch)
		button1.setStyleSheet(stylesheet1)#backgself.setCentralWidget(widget)round:transparent;
		button1.setFixedWidth(100)
		button1.setFixedHeight(50)
		button2 = QPushButton(self.widget)
		button2.setText("Quitter")
		button2.clicked.connect(QCoreApplication.instance().quit)
		button2.setStyleSheet(stylesheet2)
		button2.setFixedWidth(100)
		button2.setFixedHeight(50)
		vbox2.addWidget(button1)
		vbox2.addWidget(button2)
		self.textLabel1 = QLabel(text1)
		self.textLabel1.setStyleSheet("color:black;font-size: 20px;font-weight: normal;")
		self.textLabel1.resize(50,100)
		self.textLabel1.setFixedWidth(680)
		self.textLabel1.setFixedHeight(50)
		self.textLabel2 = QLabel(text2)
		self.textLabel2.setStyleSheet("color:black;font-size: 12px;font-weight: normal;")
		self.textLabel2.setFixedWidth(680)
		self.textLabel2.setFixedHeight(50)
		self.textLabel3 = QLabel(text3)
		self.textLabel3.setFixedWidth(680)
		self.textLabel3.setFixedHeight(50)
		self.textLabel3.setStyleSheet("color:black;font-size: 12px;font-weight: bold;")
		self.textLabel4 = QLabel(text4)
		self.textLabel4.setStyleSheet("color:black;font-size: 12px;font-weight: normal;")
		self.textLabel4.setFixedWidth(680)
		self.textLabel4.setFixedHeight(20)
		vbox1.addWidget(self.textLabel1)
		vbox1.addWidget(self.textLabel2)
		vbox1.addWidget(self.textLabel3)
		vbox1.addWidget(self.textLabel4)
		grid_layout.addLayout(vbox1,1,0) 
		grid_layout.addLayout(vbox2,3,1)
		self.widget.setLayout(grid_layout)
		self.setCentralWidget(self.widget)
		#sys.exit(app.exec_())
	def switch(self):
		w1=window2()
		self.setCentralWidget(w1)
		w1.show()

		


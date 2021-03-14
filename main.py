from interface.design1 import window1
from PyQt5.QtWidgets import QApplication
import sys
def main():
	app = QApplication(sys.argv)
	w=window1()
	w.show()
	app.exec_()
	

if __name__ == '__main__':
   main() 
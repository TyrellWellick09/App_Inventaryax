import os, sys
from PyQt5 import   QtWidgets, QtCore, uic
import time 



class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi('Views\start.ui', self)
		#eliminar barra
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		#transparente
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		

 
    def abrirOtraventana(self):
        self.hide()
        self.otraVentana = Menu()
        self.otraVentana.show()



class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi('Views\Menu.ui', self)
		#eliminar barra
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		#transparente
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
       
	


    


        
    	


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = Main()	 
     mi_app.show()
     sys.exit(app.exec_())	

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6 import QtGui


import icons
from ui_interfaz1 import Ui_EmuladorSs1



class inicio(QMainWindow):
    def __init__(self):
        super(inicio, self).__init__()
        # poner icono en la barra
        self.setWindowIcon(QtGui.QIcon('icons/dna_icon_251848.png'))
        # set the title
        self.setWindowTitle("Icon")

        # setting  the geometry of window
        self.setGeometry(0, 0, 400, 300)
 
        # creating a label widget
        #self.label = QLabel("Icon is set", self)
 
        # moving position
        #self.label.move(100, 100)
 
        # setting up border
        #self.label.setStyleSheet("border: 1px solid black;")
        self.ui = Ui_EmuladorSs1()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        
        self.ui.pushButton_2.setChecked(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = inicio()
    window.show()
    sys.exit(app.exec())
    




"""app = QtWidgets.QApplication([])
        self.ui = QtWidgets.QDialog()
        self.ui = uic.loadUi("EmuladorSs12.ui")
        self.ui.show()
        app.exec()"""
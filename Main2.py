from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
from ui_Interfaz2 import *

import icons

class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        #modo translucido
        self.setWindowOpacity(0.9)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        #boton para minimizar
        self.ui.pushButton.clicked.connect(lambda:self.showMinimized())
        #cerrar boton
        self.ui.pushButton_2.clicked.connect(lambda:self.close())
        
        #maximizar
        MyScn = QScreen
    
        self.ui.pushButton_3.clicked.connect(lambda:self.setGeometry(0, 0, MyScn.availableGeometry(QApplication.primaryScreen()).width(), MyScn.availableGeometry(QApplication.primaryScreen()).height()))
        
        QSizeGrip(self.ui.size_f)
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindows()
    sys.exit(app.exec()) 

from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
from ui_Interfaz2 import *
import prueba as pr



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
        #self.ui.pushButton_4.clicked.connect(lambda:ventana.show())
        self.ui.pushButton_3.clicked.connect(lambda:self.setGeometry(0, 0, MyScn.availableGeometry(QApplication.primaryScreen()).width(), MyScn.availableGeometry(QApplication.primaryScreen()).height()))
        #self.ui.pushButton_8.clicked.connect()
        QSizeGrip(self.ui.size_f)
        self.ui.label_7.setText("velocidad:0")
        self.ui.horizontalSlider.setRange(0, 100)
        self.ui.horizontalSlider.setValue(0)
        self.ui.horizontalSlider.setSingleStep(10)
        self.ui.horizontalSlider.setPageStep(20)
        self.ui.horizontalSlider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.ui.horizontalSlider.valueChanged.connect(self.update)
        self.show()
    def update(self, value):
        #self.ui = Ui_MainWindow()
        self.ui.label_7.setText(f'velocidad: {value}')
class Ventana(MainWindows):
    def __init__(self):
        super().__init__()  
        self.ui.label_2 = QLabel(self.ui.frame_5)
        self.ui.label_2.setObjectName(u"label_2")
        self.ui.label_2.setMaximumSize(QSize(130, 30))  
        self.setMouseTracking(True)
        self.pos_inicial = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.pos_inicial = event.pos()

    def mouseMoveEvent(self, event):
        if self.pos_inicial is not None:
            self.move(self.pos() + (event.pos() - self.pos_inicial))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindows()
    sys.exit(app.exec()) 
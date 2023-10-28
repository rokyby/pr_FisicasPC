# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EmuladorSs12TlevBa.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)
 
import icons
class Ui_EmuladorSs1(object):
    def setupUi(self, EmuladorSs1):
        if not EmuladorSs1.objectName():
            EmuladorSs1.setObjectName(u"EmuladorSs1")
        EmuladorSs1.resize(838, 775)
        self.actiondetener = QAction(EmuladorSs1)
        self.actiondetener.setObjectName(u"actiondetener")
        self.actionsalir = QAction(EmuladorSs1)
        self.actionsalir.setObjectName(u"actionsalir")
        self.actioninstrucciones = QAction(EmuladorSs1)
        self.actioninstrucciones.setObjectName(u"actioninstrucciones")
        self.centralwidget = QWidget(EmuladorSs1)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.openGLWidget = QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setObjectName(u"openGLWidget")

        self.gridLayout.addWidget(self.openGLWidget, 1, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setEnabled(True)
        self.icon_only_widget.setMaximumSize(QSize(100, 16777215))
        self.icon_only_widget.setProperty("setWidthForHeightSize", QSize(100, 100))
        self.verticalLayout_5 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(80, 80))
        self.label.setPixmap(QPixmap(u"icons/configuration_preferences_tools_setting_gear_icon_251406.png"))
        self.label.setScaledContents(True)
        self.label.setProperty("setWidthForHeightSize", QSize(50, 50))

        self.verticalLayout_4.addWidget(self.label)

        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Onyx"])
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_3 = QLabel(self.icon_only_widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Onyx"])
        font1.setPointSize(26)
        self.label_3.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_2 = QLabel(self.icon_only_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(31, 31))
        self.label_2.setPixmap(QPixmap(u"icons/8.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setProperty("setWidthForHeightSize", QSize(31, 31))

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalSlider = QSlider(self.icon_only_widget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.horizontalSlider)

        self.label_6 = QLabel(self.icon_only_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(51, 51))
        self.label_6.setPixmap(QPixmap(u"icons/preferences_control_tools_configuration_option_bar_settings_icon_219345.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setProperty("setWidthForHeightSize", QSize(51, 51))

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_5 = QLabel(self.icon_only_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.horizontalSlider_2 = QSlider(self.icon_only_widget)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.horizontalSlider_2)

        self.label_8 = QLabel(self.icon_only_widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_8)

        self.label_7 = QLabel(self.icon_only_widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(47, 41))
        self.label_7.setPixmap(QPixmap(u"icons/vertical_options_setting_control_configuration_icon_229076.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setProperty("setWidthForHeightSize", QSize(47, 41))

        self.verticalLayout_4.addWidget(self.label_7)

        self.horizontalSlider_3 = QSlider(self.icon_only_widget)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.horizontalSlider_3)

        self.line = QFrame(self.icon_only_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.label_9 = QLabel(self.icon_only_widget)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setFamilies([u"Onyx"])
        font2.setPointSize(22)
        self.label_9.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_9)

        self.pushButton = QPushButton(self.icon_only_widget)
        self.pushButton.setObjectName(u"Iniciar")
        self.pushButton.setMaximumSize(QSize(50, 50))
        self.pushButton.setSizeIncrement(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u"icons/lightning_electricity_thunder_current_bolt_icon_251399.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 2, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon1 = QIcon()
        icon1.addFile(u"icons/configuration_preferences_tools_setting_gear_icon_251406.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon2 = QIcon()
        icon2.addFile(u"icons/dna_icon_251848.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pushButton_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon3 = QIcon()
        icon3.addFile(u"icons/preferences_control_tools_configuration_option_bar_settings_icon_219345.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pushButton_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon4 = QIcon()
        icon4.addFile(u"icons/vertical_options_setting_control_configuration_icon_229076.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pushButton_6)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.openGLWidget_2 = QOpenGLWidget(self.widget_3)
        self.openGLWidget_2.setObjectName(u"openGLWidget_2")
        self.openGLWidget_2.setMinimumSize(QSize(0, 690))

        self.gridLayout_2.addWidget(self.openGLWidget_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        EmuladorSs1.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(EmuladorSs1)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 838, 22))
        self.menuarchivo = QMenu(self.menubar)
        self.menuarchivo.setObjectName(u"menuarchivo")
        self.menuayuda = QMenu(self.menubar)
        self.menuayuda.setObjectName(u"menuayuda")
        EmuladorSs1.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuarchivo.menuAction())
        self.menubar.addAction(self.menuayuda.menuAction())
        self.menuarchivo.addAction(self.actiondetener)
        self.menuarchivo.addSeparator()
        self.menuarchivo.addAction(self.actionsalir)
        self.menuayuda.addAction(self.actioninstrucciones)

        self.retranslateUi(EmuladorSs1)
        self.pushButton_2.toggled.connect(self.widget.setVisible)
        self.pushButton_2.toggled.connect(self.icon_only_widget.setHidden)

        QMetaObject.connectSlotsByName(EmuladorSs1)
    # setupUi

    def retranslateUi(self, EmuladorSs1):
        EmuladorSs1.setWindowTitle(QCoreApplication.translate("EmuladorSs1", u"EmuladorSs1", None))
        self.actiondetener.setText(QCoreApplication.translate("EmuladorSs1", u"detener", None))
        self.actionsalir.setText(QCoreApplication.translate("EmuladorSs1", u"salir", None))
        self.actioninstrucciones.setText(QCoreApplication.translate("EmuladorSs1", u"instrucciones", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("EmuladorSs1", u"Configurations", None))
        self.label_3.setText(QCoreApplication.translate("EmuladorSs1", u"Time", None))
        self.label_2.setText("")
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("EmuladorSs1", u"Wheigt", None))
        self.label_8.setText(QCoreApplication.translate("EmuladorSs1", u"Gravity", None))
        self.label_7.setText("")
        self.label_9.setText(QCoreApplication.translate("EmuladorSs1", u"Theme", None))
        self.pushButton.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("EmuladorSs1", u"inicio", None))
        self.menuarchivo.setTitle(QCoreApplication.translate("EmuladorSs1", u"archivo", None))
        self.menuayuda.setTitle(QCoreApplication.translate("EmuladorSs1", u"ayuda", None))
    # retranslateUi


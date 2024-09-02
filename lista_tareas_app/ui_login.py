# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(588, 561)
        font = QFont()
        font.setBold(False)
        LoginWindow.setFont(font)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 75))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout_7.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_7, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.inicio_text = QLabel(self.frame_3)
        self.inicio_text.setObjectName(u"inicio_text")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(False)
        self.inicio_text.setFont(font2)

        self.verticalLayout_4.addWidget(self.inicio_text)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 100))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.correo_text = QLabel(self.frame)
        self.correo_text.setObjectName(u"correo_text")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.correo_text.setFont(font3)

        self.verticalLayout_2.addWidget(self.correo_text)

        self.correo_input = QLineEdit(self.frame)
        self.correo_input.setObjectName(u"correo_input")
        self.correo_input.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.correo_input)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 100))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pass_text = QLabel(self.frame_2)
        self.pass_text.setObjectName(u"pass_text")
        self.pass_text.setFont(font3)

        self.verticalLayout_3.addWidget(self.pass_text)

        self.pass_input = QLineEdit(self.frame_2)
        self.pass_input.setObjectName(u"pass_input")
        self.pass_input.setMinimumSize(QSize(0, 30))
        self.pass_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.pass_input)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 100))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.boton_inicio = QPushButton(self.frame_4)
        self.boton_inicio.setObjectName(u"boton_inicio")
        self.boton_inicio.setMinimumSize(QSize(0, 35))
        self.boton_inicio.setFont(font3)

        self.verticalLayout_5.addWidget(self.boton_inicio)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 100))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.register_button = QPushButton(self.frame_5)
        self.register_button.setObjectName(u"register_button")

        self.horizontalLayout.addWidget(self.register_button)


        self.verticalLayout.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.alerta = QLabel(self.frame_6)
        self.alerta.setObjectName(u"alerta")
        font4 = QFont()
        font4.setBold(True)
        self.alerta.setFont(font4)

        self.verticalLayout_6.addWidget(self.alerta)


        self.verticalLayout.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"TaskFlow", None))
        self.inicio_text.setText(QCoreApplication.translate("LoginWindow", u"Inicio de sesi\u00f3n", None))
        self.correo_text.setText(QCoreApplication.translate("LoginWindow", u"Correo", None))
        self.pass_text.setText(QCoreApplication.translate("LoginWindow", u"Contrase\u00f1a", None))
        self.boton_inicio.setText(QCoreApplication.translate("LoginWindow", u"Acceder", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"No tienes cuenta?", None))
        self.register_button.setText(QCoreApplication.translate("LoginWindow", u"Registrate", None))
        self.alerta.setText("")
    # retranslateUi


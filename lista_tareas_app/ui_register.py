# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        if not RegisterWindow.objectName():
            RegisterWindow.setObjectName(u"RegisterWindow")
        RegisterWindow.resize(800, 600)
        self.centralwidget = QWidget(RegisterWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_6.setFont(font)

        self.verticalLayout_8.addWidget(self.label_6)


        self.verticalLayout.addWidget(self.frame_8, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 60))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 70))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label.setFont(font2)

        self.verticalLayout_5.addWidget(self.label)

        self.nombre_input = QLineEdit(self.frame)
        self.nombre_input.setObjectName(u"nombre_input")
        self.nombre_input.setMinimumSize(QSize(0, 30))

        self.verticalLayout_5.addWidget(self.nombre_input)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 70))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_2)

        self.correo_input = QLineEdit(self.frame_2)
        self.correo_input.setObjectName(u"correo_input")
        self.correo_input.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.correo_input)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 70))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_3)

        self.pass_input = QLineEdit(self.frame_3)
        self.pass_input.setObjectName(u"pass_input")
        self.pass_input.setMinimumSize(QSize(0, 30))
        self.pass_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.pass_input)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(300, 70))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_4)

        self.confirm_pass_input = QLineEdit(self.frame_4)
        self.confirm_pass_input.setObjectName(u"confirm_pass_input")
        self.confirm_pass_input.setMinimumSize(QSize(0, 30))
        self.confirm_pass_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout_6.addWidget(self.confirm_pass_input)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 50))
        self.frame_5.setMaximumSize(QSize(16777215, 100))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.register_button = QPushButton(self.frame_5)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setMinimumSize(QSize(0, 35))
        self.register_button.setFont(font2)

        self.verticalLayout_7.addWidget(self.register_button)


        self.verticalLayout.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.to_login_button = QPushButton(self.frame_9)
        self.to_login_button.setObjectName(u"to_login_button")

        self.horizontalLayout.addWidget(self.to_login_button)


        self.verticalLayout.addWidget(self.frame_9, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.alerta = QLabel(self.frame_7)
        self.alerta.setObjectName(u"alerta")

        self.verticalLayout_9.addWidget(self.alerta)


        self.verticalLayout.addWidget(self.frame_7, 0, Qt.AlignHCenter)

        RegisterWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisterWindow)

        QMetaObject.connectSlotsByName(RegisterWindow)
    # setupUi

    def retranslateUi(self, RegisterWindow):
        RegisterWindow.setWindowTitle(QCoreApplication.translate("RegisterWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("RegisterWindow", u"TaskFlow", None))
        self.label_5.setText(QCoreApplication.translate("RegisterWindow", u"Registrate", None))
        self.label.setText(QCoreApplication.translate("RegisterWindow", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("RegisterWindow", u"Correo", None))
        self.label_3.setText(QCoreApplication.translate("RegisterWindow", u"Contrase\u00f1a", None))
        self.label_4.setText(QCoreApplication.translate("RegisterWindow", u"Confirmar contrase\u00f1a", None))
        self.register_button.setText(QCoreApplication.translate("RegisterWindow", u"Crear cuenta", None))
        self.label_7.setText(QCoreApplication.translate("RegisterWindow", u"Ya tienes cuenta?", None))
        self.to_login_button.setText(QCoreApplication.translate("RegisterWindow", u"Ingresa", None))
        self.alerta.setText("")
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(783, 604)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.welcome_text = QLabel(self.frame)
        self.welcome_text.setObjectName(u"welcome_text")
        font = QFont()
        font.setPointSize(18)
        self.welcome_text.setFont(font)

        self.verticalLayout_2.addWidget(self.welcome_text)


        self.verticalLayout.addWidget(self.frame)

        self.layout_tareas = QFrame(self.centralwidget)
        self.layout_tareas.setObjectName(u"layout_tareas")
        self.layout_tareas.setMaximumSize(QSize(16777215, 750))
        self.layout_tareas.setFrameShape(QFrame.NoFrame)
        self.layout_tareas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.layout_tareas)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea = QScrollArea(self.layout_tareas)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 737, 387))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tareas = QVBoxLayout()
        self.tareas.setSpacing(0)
        self.tareas.setObjectName(u"tareas")

        self.verticalLayout_4.addLayout(self.tareas)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_6.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.layout_tareas)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.new_task_button = QPushButton(self.frame_2)
        self.new_task_button.setObjectName(u"new_task_button")
        self.new_task_button.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.new_task_button.setFont(font1)
        self.new_task_button.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.new_task_button)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.logout_button = QPushButton(self.frame_3)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setMinimumSize(QSize(100, 0))

        self.verticalLayout_5.addWidget(self.logout_button)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.welcome_text.setText(QCoreApplication.translate("MainWindow", u"Bienvenido", None))
        self.new_task_button.setText(QCoreApplication.translate("MainWindow", u"Nueva tarea", None))
        self.logout_button.setText(QCoreApplication.translate("MainWindow", u"Cerrar sesi\u00f3n", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editTask.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_EditTaskWindow(object):
    def setupUi(self, EditTaskWindow):
        if not EditTaskWindow.objectName():
            EditTaskWindow.setObjectName(u"EditTaskWindow")
        EditTaskWindow.resize(800, 600)
        self.centralwidget = QWidget(EditTaskWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 75))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.agregar_tarea_text = QLabel(self.frame)
        self.agregar_tarea_text.setObjectName(u"agregar_tarea_text")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.agregar_tarea_text.setFont(font)

        self.verticalLayout_2.addWidget(self.agregar_tarea_text, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.titulo_text = QLabel(self.frame_2)
        self.titulo_text.setObjectName(u"titulo_text")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.titulo_text.setFont(font1)

        self.verticalLayout_3.addWidget(self.titulo_text)

        self.titulo_tarea_input = QLineEdit(self.frame_2)
        self.titulo_tarea_input.setObjectName(u"titulo_tarea_input")
        self.titulo_tarea_input.setMinimumSize(QSize(0, 35))

        self.verticalLayout_3.addWidget(self.titulo_tarea_input)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 150))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.descripcion_text = QLabel(self.frame_3)
        self.descripcion_text.setObjectName(u"descripcion_text")
        self.descripcion_text.setMaximumSize(QSize(16777215, 30))
        self.descripcion_text.setFont(font1)

        self.verticalLayout_4.addWidget(self.descripcion_text)

        self.desc_tarea_input = QLineEdit(self.frame_3)
        self.desc_tarea_input.setObjectName(u"desc_tarea_input")
        self.desc_tarea_input.setMinimumSize(QSize(0, 100))
        self.desc_tarea_input.setLayoutDirection(Qt.LeftToRight)
        self.desc_tarea_input.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.desc_tarea_input)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(300, 0))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.fecha_text = QLabel(self.frame_4)
        self.fecha_text.setObjectName(u"fecha_text")
        self.fecha_text.setFont(font1)

        self.verticalLayout_5.addWidget(self.fecha_text)

        self.fecha_input = QDateEdit(self.frame_4)
        self.fecha_input.setObjectName(u"fecha_input")
        self.fecha_input.setMinimumSize(QSize(0, 35))
        self.fecha_input.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(12, 0, 0)))

        self.verticalLayout_5.addWidget(self.fecha_input)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.boton_editar_tarea = QPushButton(self.frame_5)
        self.boton_editar_tarea.setObjectName(u"boton_editar_tarea")
        self.boton_editar_tarea.setMinimumSize(QSize(150, 35))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.boton_editar_tarea.setFont(font2)

        self.verticalLayout_6.addWidget(self.boton_editar_tarea)


        self.verticalLayout.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.alerta = QLabel(self.frame_6)
        self.alerta.setObjectName(u"alerta")

        self.verticalLayout_7.addWidget(self.alerta)


        self.verticalLayout.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.cancel_button = QPushButton(self.frame_7)
        self.cancel_button.setObjectName(u"cancel_button")

        self.verticalLayout_8.addWidget(self.cancel_button)


        self.verticalLayout.addWidget(self.frame_7, 0, Qt.AlignRight)

        EditTaskWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditTaskWindow)

        QMetaObject.connectSlotsByName(EditTaskWindow)
    # setupUi

    def retranslateUi(self, EditTaskWindow):
        EditTaskWindow.setWindowTitle(QCoreApplication.translate("EditTaskWindow", u"MainWindow", None))
        self.agregar_tarea_text.setText(QCoreApplication.translate("EditTaskWindow", u"Editar Tarea", None))
        self.titulo_text.setText(QCoreApplication.translate("EditTaskWindow", u"T\u00edtulo", None))
        self.titulo_tarea_input.setPlaceholderText("")
        self.descripcion_text.setText(QCoreApplication.translate("EditTaskWindow", u"Descripci\u00f3n", None))
        self.desc_tarea_input.setPlaceholderText(QCoreApplication.translate("EditTaskWindow", u"A\u00f1ade una descripci\u00f3n", None))
        self.fecha_text.setText(QCoreApplication.translate("EditTaskWindow", u"Fecha l\u00edmite", None))
        self.boton_editar_tarea.setText(QCoreApplication.translate("EditTaskWindow", u"Editar tarea", None))
        self.alerta.setText("")
        self.cancel_button.setText(QCoreApplication.translate("EditTaskWindow", u"Cancelar", None))
    # retranslateUi


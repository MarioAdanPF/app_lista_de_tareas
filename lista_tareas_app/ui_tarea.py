# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tarea.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QSizePolicy, QWidget)

class Ui_tarea_widget(object):
    def setupUi(self, tarea_widget):
        if not tarea_widget.objectName():
            tarea_widget.setObjectName(u"tarea_widget")
        tarea_widget.resize(839, 100)
        tarea_widget.setMinimumSize(QSize(0, 100))
        tarea_widget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setKerning(True)
        tarea_widget.setFont(font)
        self.horizontalLayout = QHBoxLayout(tarea_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(tarea_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 85))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.del_task_button = QPushButton(self.frame)
        self.del_task_button.setObjectName(u"del_task_button")
        self.del_task_button.setMinimumSize(QSize(100, 35))
        self.del_task_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.del_task_button, 0, 2, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.desc_tarea = QLabel(self.frame)
        self.desc_tarea.setObjectName(u"desc_tarea")
        self.desc_tarea.setMinimumSize(QSize(250, 0))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setKerning(True)
        self.desc_tarea.setFont(font1)

        self.gridLayout_2.addWidget(self.desc_tarea, 1, 0, 1, 1)

        self.titulo_tarea_check = QCheckBox(self.frame)
        self.titulo_tarea_check.setObjectName(u"titulo_tarea_check")
        self.titulo_tarea_check.setMinimumSize(QSize(250, 0))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setKerning(True)
        self.titulo_tarea_check.setFont(font2)

        self.gridLayout_2.addWidget(self.titulo_tarea_check, 0, 0, 1, 1)

        self.fecha_text = QLabel(self.frame)
        self.fecha_text.setObjectName(u"fecha_text")

        self.gridLayout_2.addWidget(self.fecha_text, 0, 1, 2, 1, Qt.AlignRight)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.edit_task_button = QPushButton(self.frame)
        self.edit_task_button.setObjectName(u"edit_task_button")
        self.edit_task_button.setMinimumSize(QSize(100, 35))
        self.edit_task_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.edit_task_button, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(tarea_widget)

        QMetaObject.connectSlotsByName(tarea_widget)
    # setupUi

    def retranslateUi(self, tarea_widget):
        tarea_widget.setWindowTitle(QCoreApplication.translate("tarea_widget", u"Form", None))
        self.del_task_button.setText(QCoreApplication.translate("tarea_widget", u"Eliminar", None))
        self.desc_tarea.setText(QCoreApplication.translate("tarea_widget", u"Descripci\u00f3n tarea", None))
        self.titulo_tarea_check.setText(QCoreApplication.translate("tarea_widget", u"Titulo tarea", None))
        self.fecha_text.setText("")
        self.edit_task_button.setText(QCoreApplication.translate("tarea_widget", u"Editar", None))
    # retranslateUi


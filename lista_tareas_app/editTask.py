# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QDate
from ui_editTask import Ui_EditTaskWindow
from datetime import datetime
from helpers import url_api, load_token
from routes import RouteManager
import requests
import json


class EditTaskWindow(QMainWindow):
    def __init__(self, id_tarea, parent=None):
        super().__init__(parent)
        self.ui = Ui_EditTaskWindow()
        self.ui.setupUi(self)

        self.token = load_token()

        self.id_tarea = id_tarea

        self.route_manager = RouteManager()

        self.ui.boton_editar_tarea.clicked.connect(self.editar_tarea)

        self.ui.cancel_button.clicked.connect(lambda: self.route_manager.mandar_a_principal(self, self.token))

        self.url = url_api + f"/tareas/{self.id_tarea}"
        self.headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(self.url, headers=self.headers)
        respuesta_decodificada = response.content.decode('utf-8')
        respuesta_decodificada = json.loads(respuesta_decodificada)

        tarea = respuesta_decodificada["tarea"]

        self.ui.titulo_tarea_input.setText(tarea["titulo"])

        if tarea["descripcion"] != "":
            self.ui.desc_tarea_input.setText(tarea["descripcion"])


        if tarea["fecha_limite"] != None:
            self.fecha_limite = QDate.fromString(tarea["fecha_limite"], "yyyy-MM-dd")
            self.ui.fecha_input.setDate(self.fecha_limite)

    def editar_tarea(self):
        titulo_tarea = self.ui.titulo_tarea_input.text()
        descripcion_tarea = self.ui.desc_tarea_input.text()
        fecha_limite = self.ui.fecha_input.date()
        fecha_str = fecha_limite.toString("yyyy-MM-dd")

        if titulo_tarea:
            if fecha_str != "2024-01-01" and fecha_limite <= datetime.now():
                self.ui.alerta.setText("La fecha límite debe ser mayor a la fecha actual")
                return 0

            elif fecha_str == "2024-01-01":
                info_tarea = {
                    'titulo': titulo_tarea,
                    'descripcion': descripcion_tarea,
                    'fecha_limite': None
                }

                response = requests.put(self.url, json=info_tarea, headers=self.headers)
                respuesta_decodificada = response.content.decode('utf-8')
                respuesta_decodificada = json.loads(respuesta_decodificada)
                print(respuesta_decodificada)

                self.route_manager.mandar_a_principal(self, self.token)

            else:
                info_tarea = {
                    'titulo': titulo_tarea,
                    'descripcion': descripcion_tarea,
                    'fecha_limite': fecha_str
                }

                response = requests.put(self.url, json=info_tarea, headers=self.headers)
                respuesta_decodificada = response.content.decode('utf-8')
                respuesta_decodificada = json.loads(respuesta_decodificada)
                print(respuesta_decodificada)

                self.route_manager.mandar_a_principal(self, self.token)

        else:
            self.ui.alerta.setText("El titulo es obligatorio")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = EditTaskWindow()
    widget.show()
    sys.exit(app.exec())

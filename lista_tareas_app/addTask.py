# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_addTask import Ui_AddTaskWindow
from datetime import datetime
from helpers import url_api, load_token, peticion_post
from routes import RouteManager

class AddTaskWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddTaskWindow()
        self.ui.setupUi(self)
        self.token = load_token()
        self.route_manager = RouteManager()
        self.ui.boton_agregar_tarea.clicked.connect(self.agregar_tarea)
        self.ui.cancel_button.clicked.connect(lambda: self.route_manager.mandar_a_principal(self, self.token))

    def agregar_tarea(self):
        url = url_api + "/tareas"
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
                peticion_post(url=url, info=info_tarea)
                self.route_manager.mandar_a_principal(self, self.token)

            else:
                info_tarea = {
                    'titulo': titulo_tarea,
                    'descripcion': descripcion_tarea,
                    'fecha_limite': fecha_str
                }

                peticion_post(url=url, info=info_tarea)
                self.route_manager.mandar_a_principal(self, self.token)

        else:
            self.ui.alerta.setText("El titulo es obligatorio")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = AddTaskWindow()
    widget.show()
    sys.exit(app.exec())

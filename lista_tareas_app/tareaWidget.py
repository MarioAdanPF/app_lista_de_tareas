# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Signal
from ui_tarea import Ui_tarea_widget
from helpers import url_api, load_token
import sys
import requests
import json
from routes import RouteManager


class TareasWidget(QWidget):
    tarea_eliminada = Signal()
    tarea_editada = Signal()

    def __init__(self, nombre_tarea, id_tarea, descripcion_tarea = "Agrega una descripción", fecha_limite = "Sin fecha límite", completada = False, parent=None):
        super().__init__(parent)
        self.ui = Ui_tarea_widget()
        self.ui.setupUi(self)
        self.url = url_api + f"/tareas/{id_tarea}"
        self.route_manager = RouteManager()

        self.id_tarea = id_tarea
        self.ui.titulo_tarea_check.setText(nombre_tarea)
        self.ui.desc_tarea.setText(descripcion_tarea)
        self.ui.fecha_text.setText(fecha_limite)

        self.ui.titulo_tarea_check.setChecked(completada)

        self.ui.titulo_tarea_check.toggled.connect(self.toggle_completar_tarea)

        self.ui.del_task_button.clicked.connect(self.eliminar_tarea)
        self.ui.edit_task_button.clicked.connect(lambda: self.tarea_editada.emit())


    def toggle_completar_tarea(self):
            if self.ui.titulo_tarea_check.isChecked():
                self.completar_tarea()
            else:
                self.descompletar_tarea()

    def completar_tarea(self):
        self.actualizar_tarea_completada(True)

    def descompletar_tarea(self):
        self.actualizar_tarea_completada(False)

    def actualizar_tarea_completada(self, estado):
        token = load_token()
        headers = {"Authorization": f"Bearer {token}"}
        info_tarea = {
            'completada': estado
        }
        response = requests.put(self.url, json=info_tarea, headers=headers)
        respuesta_decodificada = response.content.decode('utf-8')
        respuesta_decodificada = json.loads(respuesta_decodificada)
        print(f"Tarea {self.id_tarea} actualizada: completada = {estado}")

    def eliminar_tarea(self):
        token = load_token()
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.delete(self.url, headers=headers)
        respuesta_decodificada = response.content.decode('utf-8')
        respuesta_decodificada = json.loads(respuesta_decodificada)
        self.tarea_eliminada.emit()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TareasWidget(nombre_tarea="Terminar proyecto programación", descripcion_tarea="Realizar prototipado en figma, crear base de datos, hacer api...")
    widget.show()
    sys.exit(app.exec())

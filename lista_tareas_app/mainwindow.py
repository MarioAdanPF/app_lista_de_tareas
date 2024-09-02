import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from ui_main import Ui_MainWindow
from tareaWidget import TareasWidget
from helpers import url_api, load_token, delete_token
from routes import RouteManager
import requests
import json

class MainWindow(QMainWindow):
    def __init__(self, parent=None, nombre_usuario=""):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.route_manager = RouteManager()

        self.ui.logout_button.clicked.connect(lambda: self.cerrar_sesion())

        self.cargar_tareas()


    def cargar_tareas(self):
        self.url = url_api + "/tareas"
        self.token_actual = load_token()
        headers = {"Authorization": f"Bearer {self.token_actual}"}
        response = requests.get(self.url, headers=headers)
        respuesta_decodificada = response.content.decode('utf-8')
        respuesta_decodificada = json.loads(respuesta_decodificada)


        if "tareas" in respuesta_decodificada:
            self.tareas = respuesta_decodificada["tareas"]
            nombre_usuario = respuesta_decodificada["username"]
            self.ui.welcome_text.setText(f"Hola {nombre_usuario}! Listo para ser productivo hoy?")

            self.ui.new_task_button.clicked.connect(lambda: self.route_manager.mandar_a_añadir_tarea(self, self.token_actual))

            self.comprobar_tareas()

        else:
            self.ui.welcome_text.setText("La sesión ha expirado, ingresa nuevamente")
            self.ui.logout_button.setText("Iniciar sesión")
            self.ui.new_task_button.setText("Función no disponible")


    def cerrar_sesion(self):
        print("Cerrando sesión")
        delete_token()
        print('Token eliminado correctamente')
        self.route_manager.mandar_a_login(self)


    def agregar_tareas(self):
        for tarea in self.tareas:
            if tarea["completada"]:
                if tarea["fecha_limite"] is not None and tarea["descripcion"] != "":
                    task = TareasWidget(id_tarea=tarea["id"], nombre_tarea=tarea["titulo"], descripcion_tarea=tarea["descripcion"], fecha_limite=f"Fecha límite\n{tarea['fecha_limite']}", completada=True)

                elif tarea["fecha_limite"] is None and tarea["descripcion"] != "":
                    task = TareasWidget(id_tarea=tarea["id"], nombre_tarea=tarea["titulo"], descripcion_tarea=tarea["descripcion"], completada=True)

                elif tarea["fecha_limite"] is None and tarea["descripcion"] == "":
                    task = TareasWidget(id_tarea=tarea["id"], nombre_tarea=tarea["titulo"], completada=True)

                elif tarea["fecha_limite"] is not None and tarea["descripcion"] == "":
                    task = TareasWidget(id_tarea=tarea["id"], nombre_tarea=tarea["titulo"], fecha_limite=f"Fecha límite\n{tarea['fecha_limite']}", completada=True)

            else:
                if tarea["fecha_limite"] is not None and tarea["descripcion"] != "":
                    task = TareasWidget(id_tarea=tarea["id"], nombre_tarea=tarea["titulo"], descripcion_tarea=tarea["descripcion"], fecha_limite=f"Fecha límite\n{tarea['fecha_limite']}")

                elif tarea["fecha_limite"] is None and tarea["descripcion"] != "":
                    task = TareasWidget(id_tarea=tarea["id"], nombre_tarea=tarea["titulo"], descripcion_tarea=tarea["descripcion"])

                elif tarea["fecha_limite"] is None and tarea["descripcion"] == "":
                    task = TareasWidget(id_tarea=tarea["id"], nombre_tarea=tarea["titulo"])

                elif tarea["fecha_limite"] is not None and tarea["descripcion"] == "":
                    task = TareasWidget(id_tarea=tarea["id"], nombre_tarea=tarea["titulo"], fecha_limite=f"Fecha límite\n{tarea['fecha_limite']}")

            self.ui.tareas.addWidget(task)
            task.tarea_eliminada.connect(lambda t=task: self.eliminar_tarea_widget(t))
            task.tarea_editada.connect(lambda t=task: self.route_manager.mandar_a_editar_tarea(self, self.token_actual, t.id_tarea))


    def eliminar_tarea_widget(self, tarea_widget):
        self.ui.tareas.removeWidget(tarea_widget)
        tarea_widget.deleteLater()

        self.tareas = [tarea for tarea in self.tareas if tarea['id'] != tarea_widget.id_tarea]

        if len(self.tareas) == 0:
            self.mostrar_mensaje_sin_tareas()


    def comprobar_tareas(self):
        while self.ui.tareas.count() > 0:
            widget = self.ui.tareas.takeAt(0).widget()
            if widget is not None:
                widget.deleteLater()

        if len(self.tareas) == 0:
            self.mostrar_mensaje_sin_tareas()
        else:
            self.agregar_tareas()


    def mostrar_mensaje_sin_tareas(self):
        no_tareas_label = QLabel("Aún no tienes tareas, crea una!")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        no_tareas_label.setFont(font)
        self.ui.tareas.addWidget(no_tareas_label)
        no_tareas_label.setAlignment(Qt.AlignCenter)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

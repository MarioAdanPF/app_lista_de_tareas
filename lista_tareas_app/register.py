# This Python file uses the following encoding: utf-8
import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_register import Ui_RegisterWindow
import json
from mainwindow import MainWindow
from routes import RouteManager

from helpers import url_api

class RegisterWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_RegisterWindow()

        self.ui.setupUi(self)

        self.route_manager = RouteManager()

        self.ui.register_button.clicked.connect(self.capturar_info)

        self.ui.to_login_button.clicked.connect(lambda: self.route_manager.mandar_a_login(self))


    def capturar_info(self):
        self.username = self.ui.nombre_input.text()
        self.mail = self.ui.correo_input.text()
        self.password = self.ui.pass_input.text()
        self.passwordConfirm = self.ui.confirm_pass_input.text()

        if len(self.username) == 0 or len(self.password) == 0 or len(self.mail) == 0:
            print('Faltan agregar campos')

            self.ui.alerta.setText('Falta completar campos')

        elif "@" not in self.mail or "." not in self.mail:
            print("El correo no es valido")
            self.ui.alerta.setText('Ingresa un correo valido')

        elif self.password != self.passwordConfirm:
            print("Las contraseñas deben coincidir")
            self.ui.alerta.setText('Las contraseñas deben coincidir')

        else:
            self.ui.alerta.setText('Cuenta creada con exito')
            print('Cuenta creada con las siguientes credenciales')
            print(f'''
            Correo: {self.mail}
            User: {self.username}
            Password: {self.password}
            ''')
            self.crear_usuario(self.username, self.mail, self.password)

    def crear_usuario(self, username, correo, password):
        url = url_api + '/usuarios/registro'

        info_user = {
            'nombre': username,
            'email': correo,
            'passw': password
        }

        response = requests.post(url, json=info_user)

        respuesta_decodificada = response.content.decode('utf-8')

        respuesta_decodificada = json.loads(respuesta_decodificada)

        print(respuesta_decodificada)

        if "Error" in respuesta_decodificada:
            print('Usuario duplicado')
            self.ui.alerta.setText('Ese correo ya está registrado')
            return 1

        elif 'Nuevo usuario' in respuesta_decodificada:
            print('Se creó un nuevo usuario')
            self.ui.alerta.setText('Se creó un nuevo usuario')
            self.route_manager.mandar_a_login(self)
            return 0

        else:
            print('Error interno')
            self.ui.alerta.setText('Error interno')
            return 1

    def manda_a_login(self):
        self.ventana_login = MainWindow()
        # Mostramos esa nueva ventana
        self.ventana_registro.show()
        # Para no tener dos ventanas abiertas, cerramos la anterior
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = RegisterWindow()
    widget.show()

    sys.exit(app.exec())

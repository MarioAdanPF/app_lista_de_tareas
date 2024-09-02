import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_login import Ui_LoginWindow
from helpers import url_api
from routes import RouteManager
import requests
import json


class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.boton_inicio.clicked.connect(self.iniciar_sesion)
        self.route_manager = RouteManager()
        self.ui.register_button.clicked.connect(lambda: self.route_manager.mandar_a_registro(self))


    def capturar_info(self):
        email = self.ui.correo_input.text()
        passw = self.ui.pass_input.text()
        return email, passw


    def iniciar_sesion(self):
        url = url_api + '/usuarios/login'

        email, password = self.capturar_info()

        if email and password:

            info_a_enviar = {
                'email': email,
                'passw': password
            }

            response = requests.post(url, json=info_a_enviar)

            respuesta_decodificada = response.content.decode('utf-8')

            respuesta_decodificada = json.loads(respuesta_decodificada)

            print(respuesta_decodificada)

            if 'Error' in respuesta_decodificada:
                print('El correo o contraseña no coinciden')
                self.ui.alerta.setText("El correo o contraseña no coinciden")

            elif 'Token' in respuesta_decodificada:
                print('Sesión iniciada correctamente')
                token = respuesta_decodificada['Token']
                self.route_manager.mandar_a_principal(self, token)

            else:
                print('Error en el servidor')
                self.ui.alerta.setText('Error interno del servidor')

        else:
            self.ui.alerta.setText("Faltan campos por completar")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = LoginWindow()
    widget.show()
    sys.exit(app.exec())

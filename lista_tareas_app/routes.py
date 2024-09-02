from helpers import save_token
# Este archivo se va a encargar de manejar las redirecciones

class RouteManager:
    def __init__(self):
        self.current_window = None

    # Mandar al usuario a la vista login
    def mandar_a_login(self, ventana_anterior):
        from login import LoginWindow
        self.current_window = LoginWindow()
        self.current_window.show()

        ventana_anterior.close()

    # Mandar al usuario a la vista de registro
    def mandar_a_registro(self, ventana_anterior):
        from register import RegisterWindow
        self.current_window = RegisterWindow()
        self.current_window.show()

        ventana_anterior.close()

    # Mandar al usuario a la vista principal
    def mandar_a_principal(self, ventana_actual, token):
        from mainwindow import MainWindow

        save_token(token)

        self.current_window = MainWindow()
        self.current_window.show()

        ventana_actual.close()

    def mandar_a_añadir_tarea(self, ventana_anterior, token):
        from addTask import AddTaskWindow

        save_token(token)

        self.current_window = AddTaskWindow()
        self.current_window.show()

        ventana_anterior.close()

    def mandar_a_editar_tarea(self, ventana_anterior, token, id_tarea):
        from editTask import EditTaskWindow

        save_token(token)

        self.current_window = EditTaskWindow(id_tarea)
        self.current_window.show()

        ventana_anterior.close()

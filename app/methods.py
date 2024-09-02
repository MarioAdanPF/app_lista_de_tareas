from app.extensions import db
from .models.tareas import Task
from .models.usuarios import User
from flask_jwt_extended import create_access_token
from datetime import timedelta

def login(email, passw):
    user = User.get_user_by_email(email=email)
    caducidad = timedelta(hours=1)

    if user and (user.check_passw(passw=passw)):
        access_token = create_access_token(identity = user.id, expires_delta = caducidad)
        return {'Mensaje': 'Loggeado',
                'Token': access_token
            }, 200

    else:
        return {'Error': 'Correo o contraseña no existen' }, 400


def user_register(nombre, email, passw):
    print(f"Nombre: {nombre}, Email: {email}, Passw: {passw}")
    if not all([nombre, email, passw]):
        return {'Error': 'Todos los campos son obligatorios'}, 400
    
    user = User.get_user_by_email(email=email)
    if user is not None:
        return {'Error': 'Este correo ya está registrado'}, 403
    
    nuevo_usuario = User(nombre=nombre, email=email)
    nuevo_usuario.set_passw(passw=passw)
    nuevo_usuario.save()
    
    return {'Nuevo usuario': {
            'email': email,
            'nombre': nombre
        }
    }, 200


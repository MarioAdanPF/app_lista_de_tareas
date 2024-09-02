from flask_restful import Resource
from flask import request
from .methods import *
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from .models.usuarios import User

class HelloWorld(Resource):
    
    @jwt_required()
    def get(self):
        return {'message': 'Hola mundo desde la API', 'status': 200}



class User_register(Resource):
    def post(self):
        data = request.json
        nombre = data.get('nombre')
        email = data.get('email')
        passw = data.get('passw')
        
        if not all([nombre, email, passw]):
            return {'Error': 'Todos los campos son obligatorios'}, 400
        
        respuesta, status = user_register(nombre, email, passw)
        return respuesta, status



class User_login(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        passw = data.get('passw')

        respuesta, status = login(email, passw)

        return respuesta, status
    


class Tareas(Resource):

    @jwt_required()
    def get(self, tarea_id=None):
        # Obtener el ID del usuario autenticado
        user_id = get_jwt_identity()
        
        # Si se proporciona tarea_id, buscar la tarea específica
        if tarea_id is not None:
            tarea = Task.query.filter_by(id=tarea_id, usuario_id=user_id).first()
            if tarea:
                return {'tarea': tarea.to_dict()}, 200
            else:
                return {'message': 'Tarea no encontrada'}, 404
        
        # Si tarea_id es None, devolver todas las tareas
        nombre_user = User.query.filter_by(id=user_id).first().nombre
        tareas = Task.query.filter_by(usuario_id=user_id).all()
        return {'tareas': [tarea.to_dict() for tarea in tareas], 'username': nombre_user}, 200



    @jwt_required()
    def post(self):
        # Crear una nueva tarea para el usuario autenticado
        user_id = get_jwt_identity()
        data = request.json
        titulo = data.get('titulo')
        descripcion = data.get('descripcion')
        fecha_limite = data.get('fecha_limite')

        if fecha_limite is not None:
            fecha_limite = datetime.strptime(fecha_limite, '%Y-%m-%d')
            if fecha_limite <= datetime.now():
                return {'message': 'La fecha límite debe ser mayor a la fecha actual'}, 400

        if not titulo:
            return {'message': 'El título es obligatorio'}, 400
        
        nueva_tarea = Task(
            usuario_id=user_id,
            titulo=titulo,
            descripcion=descripcion,
            fecha_limite=fecha_limite
        )
        
        nueva_tarea.save()
        
        return {'message': 'Tarea creada con éxito', 'tarea': nueva_tarea.to_dict()}, 201



    @jwt_required()
    def put(self, tarea_id):
        # Actualizar una tarea específica del usuario autenticado
        user_id = get_jwt_identity()
        tarea = Task.query.filter_by(id=tarea_id, usuario_id=user_id).first()
        
        if not tarea:
            return {'message': 'Tarea no encontrada'}, 404
        
        data = request.json
        tarea.titulo = data.get('titulo', tarea.titulo)
        tarea.descripcion = data.get('descripcion', tarea.descripcion)
        tarea.completada = data.get('completada', tarea.completada)
        tarea.fecha_limite = data.get('fecha_limite', tarea.fecha_limite)
        
        db.session.commit()
        
        return {'message': 'Tarea actualizada con éxito', 'tarea': tarea.to_dict()}, 200



    @jwt_required()
    def delete(self, tarea_id):
        # Eliminar una tarea específica del usuario autenticado
        user_id = get_jwt_identity()
        tarea = Task.query.filter_by(id=tarea_id, usuario_id=user_id).first()
        
        if not tarea:
            return {'message': 'Tarea no encontrada'}, 404
        
        tarea.delete()
        
        return {'message': 'Tarea eliminada con éxito'}, 200



class APIRoutes:
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')
        api.add_resource(User_register, '/usuarios/registro')
        api.add_resource(User_login, '/usuarios/login')
        api.add_resource(Tareas, '/tareas', '/tareas/<int:tarea_id>')


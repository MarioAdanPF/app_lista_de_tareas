from app.extensions import db

class Task(db.Model):
    __tablename__ = 'tarea'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    completada = db.Column(db.Boolean, default=False)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    fecha_limite = db.Column(db.Date)

    usuario = db.relationship('User', backref=db.backref('tareas', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'usuario_id': self.usuario_id,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'completada': self.completada,
            'fecha_creacion': self.fecha_creacion.isoformat() if self.fecha_creacion else None,
            'fecha_limite': self.fecha_limite.isoformat() if self.fecha_limite else None
        }
    
    def completar(self):
        self.completada = True
        db.session.commit()

    def descompletar(self):
        self.completada = False
        db.session.commit()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'<Tarea {self.titulo}>'
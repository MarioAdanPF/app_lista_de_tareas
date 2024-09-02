from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    passw = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f'<Usuario es {self.nombre}>'
    
    def set_passw(self, passw):
        if not passw:
            raise ValueError("La contraseña no puede estar vacía")
        self.passw = generate_password_hash(password=passw)

    def check_passw(self, passw):
        return check_password_hash(self.passw, passw)

    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
        
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
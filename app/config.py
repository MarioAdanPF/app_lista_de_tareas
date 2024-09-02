class Config:
    # Cambia el valor de SQLALCHEMY_DATABASE_URI por el valor de la URI de tu base de datos
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://m_perez:mapf0118@172.31.224.1:5432/lista_de_tareas_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '71b10854fc4585ad6088ec660656be3d'
    JWT_ALGORITHM = 'HS256'
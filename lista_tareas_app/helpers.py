import jwt
import os
import datetime
import requests
import json

token_file_path = 'token.txt'

url_api = "https://066a-38-156-15-104.ngrok-free.app"


def delete_token():
    with open(token_file_path, 'w') as file:
        file.write('')

def save_token(token):
    with open(token_file_path, 'w') as file:
        file.write(token)

def load_token():
    if os.path.exists(token_file_path):
        with open(token_file_path, 'r') as file:
            return file.read()
    else:
        return None

def decode_token(token):
    payload = jwt.decode(token, algorithms=["HS256"], options={'verify_signature': False})
    return payload

def token_is_valid(token):
    info_token = decode_token(token)

    expiration = datetime.datetime.fromtimestamp(info_token['exp'])
    return expiration > datetime.datetime.now()


def peticion_post(url, info):
    token_actual = load_token()

    headers = {"Authorization": f"Bearer {token_actual}"}

    response = requests.post(url, json=info, headers=headers)

    respuesta_decodificada = response.content.decode('utf-8')

    respuesta_decodificada = json.loads(respuesta_decodificada)

    return respuesta_decodificada



def get_tasks():
    token = load_token()

    if token is None or not token_is_valid(token):
        raise Exception("El token no es válido o no se encuentra. Inicia sesión de nuevo.")

    tasks_endpoint = f"{url_api}/tareas/"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(tasks_endpoint, headers=headers)

    if response.status_code == 200:
        return response.json()

    else:
        return {"error": "No se pudieron obtener las tareas.", "status_code": response.status_code}


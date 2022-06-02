from dataclasses import dataclass


from enum import Enum

class BCStatus(Enum):
    SUCESS = ("000", "Operación realizada con éxito...")
    FATAL_ERROR = ("001", "Se produjo un error...")
    NOT_FOUND = ("002", "No se encontraron registros...")
    BAD_REQUEST = ("003", "Petición inválida...")
    BD_ERROR = ("004", "Error en la base de datos...")
    LOGIN_FAILED = ("005","Error al hacer el login")
    INVALID_USER_OR_PASSWORD = ("006","Error, usuario o contraseña incorrectas")
    DUPLICATED_NAME_USER = ("007","Error, el nombre de usuario ya existe")
    DUPLICATED_EMAIL_USER = ("008","Error, el correo ya existe")
    DUPLICATED_PLAQUE_TRUCK_NUMBER = ("009","Error, el número de placa introducido ya existe.")
    DUPLICATED_TRUCK_NUMBER = ("010","Error, el número de camión introducido ya existe.")
    
    def __init__(self, code: str, description: str): 
        self.code = code
        self.description = description
    
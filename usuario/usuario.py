from .utils.roles import Rol

class Usuario:
    num_control: str
    nombre: str
    apellido: str
    contrasena: str
    rol: Rol #*ESTUDIANTE, MAESTRO, COORDINADOR
    
    def __init__(self,numero_de_control:str, nombre:str, apellido:str, contrasena:str, rol:Rol):
        self.num_control=numero_de_control
        self.nombre=nombre
        self.apellido= apellido
        self.contrasena = contrasena
        self.rol = rol
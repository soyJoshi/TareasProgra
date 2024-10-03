from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Estudiante(Usuario):
    curp: str
    fecha_nacimiento: datetime
    
    def __init__(self,num_control: str, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime, contrasena:str):
        super().__init__(numero_de_control=num_control, nombre= nombre, apellido= apellido, contrasena=contrasena,rol=Rol.ESTUDIANTE)
        self.curp = curp
        self.fecha_nacimiento =fecha_nacimiento
        
    def mostrar_info_estudiante(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Numero de control: {self.num_control}, \nNombre completo: {nombre_completo}, \nCURP:{self.curp}, \nFecha de Nacimiento: {self.fecha_nacimiento}, \nrol:{self.rol.value}"
        return info
        

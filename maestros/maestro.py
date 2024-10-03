from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Maestro(Usuario):
    rfc: str
    sueldo: float
    ano_nacimiento: datetime
    
    def __init__(self,num_control: str, nombre: str, apellido: str, rfc: str, sueldo: float,fecha_naci: datetime, contrasena:str):
        super().__init__(numero_de_control=num_control, nombre=nombre, apellido=apellido, contrasena=contrasena, rol=Rol.MAESTRO)
        self.rfc = rfc
        self.sueldo = sueldo
        self.fecha_naci =fecha_naci
        
    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Numero de control: {self.num_control}, \nNombre completo: {nombre_completo}, \nRFC:{self.rfc}, \nFecha de Nacimiento: {self.fecha_naci}, \nSueldo: {self.sueldo}"
        return info
from datetime import datetime
class Maestro:
    num_control: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float
    ano_nacimiento: datetime
    
    def __init__(self,num_control: str, nombre: str, apellido: str, rfc: str, sueldo: float,fecha_naci: datetime):
        self.num_control = num_control
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo
        self.fecha_naci =fecha_naci
        
    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Numero de control: {self.num_control}, \nNombre completo: {nombre_completo}, \nRFC:{self.rfc}, \nFecha de Nacimiento: {self.fecha_naci}, \nSueldo: {self.sueldo}"
        return info
from datetime import datetime

class Estudiante:
    num_control: str
    nombre: str
    apellido: str
    curp: str
    fecha_nacimiento: datetime
    
    def __init__(self, num_control: str, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime):
        self.num_control = num_control
        self.nombre = nombre
        self.apellido = apellido
        self.curp = curp
        self.fecha_nacimiento =fecha_nacimiento
        
    def mostrar_info_estudiante(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Numero de control: {self.num_control}, \nNombre completo: {nombre_completo}, \nCURP:{self.curp}, \nFecha de Nacimiento: {self.fecha_nacimiento}"
        return info
        

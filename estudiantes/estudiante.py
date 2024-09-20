from datetime import datetime

class Estudiante:
    num_control: str
    nombre: str
    apellido: str
    curp: str
    fecha_nacimiento: datetime
    
    def __init__(self,num_control: str, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime):
        self.num_control = "22121052"
        self.nombre = nombre
        self.apellido = apellido
        self.curp = curp
        self.fechafecha_nacimiento =fecha_nacimiento
        
from datetime import datetime
class Maestro:
    num_control: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float
    ano_nacimiento: datetime
    
    def __init__(self, nombre: str, apellido: str, rfc: str, sueldo: float,fecha_naci: datetime):
        self.num_control = "22121052"
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo
        self.fecha_naci =fecha_naci
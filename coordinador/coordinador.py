from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Coordinador(Usuario):
    sueldo: float
    rfc: str
    anos_antiguedad: int
    
    def __init__(self,num_control: int,nombre:str,apellido:str,contrasena: str, sueldo: float, rfc: str,anos_antiguedad: int, rol: Rol):
        super().__init__(numero_de_control=num_control, nombre=nombre, apellido=apellido, contrasena=contrasena, rol=Rol.COORDINADOR)
        self.sueldo= sueldo
        self.rfc = rfc
        self.anos_antiguedad = anos_antiguedad
        
    def mostrar_info_coordinador(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Numero de control: {self.num_control}, \nNombre completo: {nombre_completo}, \nRFC:{self.rfc}, \nrol:{self.rol.value}, \nAnos de Antiguedad:{self.anos_antiguedad}"
        return info

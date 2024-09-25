class Materia:
    
    "id: MT{ultimos2digitos Nombbre}{semestre}{cantidad creditos}{random 1, 1000}"
    nombre: str
    descripcion: str
    semestre: int
    creditos: int
    num_cont: str
     
    def __init__(self,num_cont, nombre: str, descripcion: str, semestre: int, creditos: int):
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos
        self.num_cont = num_cont
        
    def mostrar_info_materia(self):
        info = f"Materia: {self.nombre},  \nDescripcion: {self.descripcion}, \nSemestre: {self.semestre}, \nCreditos: {self.creditos}, \nID: {self.num_cont}"
        return info
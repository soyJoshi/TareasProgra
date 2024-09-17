import random

class Medico:
    id = 0
    nombre = ""
    ano_nacimiento = 0
    rfc = ""
    direccion = ""
    
    def __init__(self, nombre, ano_nacimiento, rfc, direccion):
        self.id = random.randint(1, 1000)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.rfc = rfc
        self.direccion = direccion
        
    def info_med(self):
        print("\nId:", self.id)
        print(f"Nombre: {self.nombre}") #Hace lo mismo que la linea 19. La f es de formateado
        print("Año de nacimiento: ", self.ano_nacimiento)
        print("rfc: ", self.rfc)
        print("Dirección: ", self.direccion)  
        
    # @property
    # def id(self):
    #     return self.id
    # @property
    # def nombre(self):
    #     return self.nombre
    # @property
    # def ano_nacimiento(self):
    #     return self.ano_nacimiento
    # @property
    # def rfc(self):
    #     return self.rfc
    # @property
    # def direccion(self):
    #     return self.direccion
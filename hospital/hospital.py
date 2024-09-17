from typing import List
from paciente.paciente import Paciente
from medico.medico import Medico
from consulta.consulta import Consulta

class Hospital:
    pacientes: List[Paciente] = []
    medicos: List[Medico] = []
    consultas: List[Consulta] = []
    
    def registrar_consulta(self, id_paciente, id_medico):
        if not self.validar_cantidad_usuarios():
            return 
        print("\nValidacion exitosa")
        
        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("\nNo se puede registrar la consulta, no existe el medico o el paciente")
            return
        print("\nContinuar con el registro")
        
    def mostrar_pacientes(self):
        print("\n____Pacientes en el sistema____")
        for paciente in self.pacientes:
            paciente.mostrar_informacion()    
        
    def mostrar_medicos(self):
        print("\n____Medicos en el sistema____")
        for medico in self.medicos:
            medico.info_med()
        
    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)
    
    def mostrar_pacientes_menores_de_edad(self):
        print("\n____Pacientes menores de edad____")
        ano_referencia = 2024  
        for paciente in self.pacientes:
            edad = ano_referencia - paciente.ano_nacimiento
            if edad < 18:
                paciente.mostrar_informacion()
                
    def mostrar_pacientes_mayores_de_edad(self):
        print("\n____Pacientes mayores de edad____")
        ano_referencia = 2024  
        for paciente in self.pacientes:
            edad = ano_referencia - paciente.ano_nacimiento
            if edad >= 18:
                paciente.mostrar_informacion()
            
        
    def registrar_medico(self, medico):
        self.medicos.append(medico)
        
    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
        return False
    def validar_existencia_medico(self, id_medico):
        for paciente in self.medicos:
            if paciente.id == id_medico:
                return True
            
        return False
                
        
        
    def validar_cantidad_usuarios(self):
        if (len(self.pacientes) == 0):
            print("\nNo puedes registrar una consulta, noe existen pacientes")
            return False

        if (len(self.medicos) == 0):
            print("\nNo puedes registrar una consulta, noe existen medicos")
            return False
        
        return True
    
    def eliminar_paciente(self, id_paciente_eliminar):
        for paciente in self.pacientes:
            if paciente.id == id_paciente_eliminar:
                self.pacientes.remove(paciente)
                print("\nse elimino el paciente de ID: ", id_paciente_eliminar)
                break
   
    def eliminar_doctor(self, id_doctor_eliminar):
        for medico in self.medicos:
            if medico.id == id_doctor_eliminar:
                self.medicos.remove(medico)
                print("\nse elimino el medico de ID: ", id_doctor_eliminar)
                break
    
from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime 
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []
    
    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
    
    def registrar_maestros(self, maestro: Maestro):
        self.lista_maestros.append(maestro)
        
    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)
        
    def generar_num_control(self):
        #L- 2024 - 09 - long estudinates + 1- +random(0,10000)
        ano= datetime.now().year
        mes = datetime.now().month
        long_estudiantes = len(self.lista_estudiantes)
        aleatorio = randint(0, 10000)
        numero_control = f"l{ano}{mes}{long_estudiantes + 1}{aleatorio}"
        return numero_control
    
    def num_control_maestro(self, ano_nacimiento, rfc, nombre):
        #-{la longitud de la lista de los profesores más uno}
        iniciales_nom = nombre[:2].upper()
        dia_actual = datetime.now().day
        long_maestros = len(self.lista_maestros)
        aleatorio = randint(500, 5000)
        ultimas_rfc = rfc[-2:].upper()
        numero_control = f"M{ano_nacimiento}{dia_actual}{aleatorio}{iniciales_nom}{ultimas_rfc}{long_maestros + 1}"
        return numero_control
    
    def id_materia(self, nombre, creditos, semestre):
        dig_nom = nombre[-2:].upper()
        semestre_materia = semestre
        aleatorio = randint(1, 1000)
        creditos_materia = creditos
        numero_control = f"MT{dig_nom}{semestre_materia}{creditos_materia}{aleatorio}"
        return numero_control
    
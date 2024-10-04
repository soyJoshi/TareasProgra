from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime 
from random import randint
from carrera.carrera import Carrera
from semestre.semestre import Semestre

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []
    lista_carreras: List[Carrera] = []
    lista_semestres: List[Semestre] = []
    
    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
    
    def registrar_maestros(self, maestro: Maestro):
        self.lista_maestros.append(maestro)
        
    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)
    
    def registrar_carrera(self, carrera: Carrera):
        self.lista_carreras.append(carrera)
        
    def registrar_grupo(self, grupo: Grupo):
        id_semestre = grupo.id_semestre
        
        for semestre in self.lista_semestres:
            if id_semestre == semestre.id:
                semestre.registrar_grupo_en_semestre(grupo)
                break
        self.lista_grupos.append(grupo)
        
    def registrar_semestre(self, semestre: Semestre):
        id_carrera = semestre.id
        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre)
                break
        self.lista_semestres.append(semestre)
        
    def listar_estudinates(self):
        print("**ESTUDINATES**")
        for estudiante in self.lista_estudiantes:
            print("\n")
            print(estudiante.mostrar_info_estudiante())
            
    def listar_maestro(self):
        print("**MAESTROS**")
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro())
    
    def listar_materia(self):
        print("**MATERIAS**")
        for materia in self.lista_materias:
            print(materia.mostrar_info_materia())
            
    def listar_grupo(self):
        print("**GRUPOS**")
        for grupo in self.lista_grupos:
            print(grupo.mostrar_info_grupo())
            
    def listar_semestre(self):
        print("**SEMESTRES**")
        for semestre in self.lista_semestres:
            print(semestre.mostrar_info_semestre())
            
    def listar_carrera(self):
        print("**CARRERAS**")
        for carrera in self.lista_carreras:
            print(carrera.mostrar_info_carrera())
            
    def eliminar_estudinate(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.num_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudinate eliminado")
                return
            
        print(f"No se encontro el estudiante con numero de control:{numero_control}")
        
    def eliminar_maestro(self, numero_control: str):
        for maestro in self.lista_maestros:
            if maestro.num_control == numero_control:
                self.lista_maestros.remove(maestro)
                print("Maestro eliminado")
                return
            
        print(f"No se encontro el estudiante con numero de control:{numero_control}")
        
    def eliminar_materia(self, numero_control: str):
        for materia in self.lista_materias:
            if materia.num_cont == numero_control:
                self.lista_materias.remove(materia)
                print("Materia eliminada")
                return
            
        print(f"No se encontro el estudiante con numero de control:{numero_control}")
        
        #listar maestro y materia eliminar maestro y materia
        
        
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
    
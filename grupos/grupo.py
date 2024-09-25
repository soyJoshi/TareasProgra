from typing import List
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia

class Grupo:
    id: int
    alumnos: List[Estudiante] = []
    maestros: List[Maestro] = []
    materias: List[Materia] = []
    tipo: chr
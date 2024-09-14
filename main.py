from estudiante import Estudiante
from curso import Curso

estudiante_uno = Estudiante("Mateo", 25, 22121048)
estudiante_dos = Estudiante("Roberto", 18, 22121090)
estudiante_tres = Estudiante("Laura", 10, 22121029)

curso_uno = Curso("Matematicas", 120, "Agtemio")
curso_dos = Curso("Taller de Lectura", 420, "Lopez")
curso_tres = Curso("Filosofia", 90, "Pedrito")

estudiante_uno.agregar_curso(curso_uno)
estudiante_dos.agregar_curso(curso_uno)
estudiante_tres.agregar_curso(curso_uno)
estudiante_uno.agregar_curso(curso_tres)
estudiante_uno.agregar_curso(curso_dos)
estudiante_dos.agregar_curso(curso_dos)
estudiante_tres.agregar_curso(curso_dos)


estudiante_uno.mostrar_info()
estudiante_dos.mostrar_info()
estudiante_tres.mostrar_info()

curso_uno.mostrar_info_curso()
curso_dos.mostrar_info_curso()
curso_tres.mostrar_info_curso()

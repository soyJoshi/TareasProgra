from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from semestre.semestre import Semestre
from datetime import datetime
from grupos.grupo import Grupo
from carrera.carrera import Carrera

class Menu:
    escuela = Escuela()
    usuario_estudiante: str = "juan123"
    contraseña_estudiante: str = "12345*"
    
    usuario_maestro: str = "Miguel"
    contraseña_maestro: str = "456789"
    
    def login(self):
        intentos = 0
        while intentos < 5:
            print("\n**** BIENVENIDO ****")
            print("Inicia Sesion para continuar")
            
            nombre_usuario = input("Ingresa tu usuario: ")
            contraseña_usuario = input("Ingresa la contraseña: ")
            
            if nombre_usuario == self.usuario_estudiante:
                
                if contraseña_usuario == self.contraseña_estudiante:
                    self.msotrar_menu_estudiante()
                    intentos = 0
                else:
                    intentos = self.mostrar_sesion_fallido(intentos_usuario=intentos)
                    
            elif nombre_usuario == self.usuario_maestro:
                if contraseña_usuario == self.contraseña_maestro:
                    self.msotrar_menu_maestros()
                    intentos = 0
                else:
                    intentos = self.mostrar_sesion_fallido(intentos_usuario=intentos)
            else:
                intentos = self.mostrar_sesion_fallido(intentos_usuario=intentos)
        print("Maximos intentos alcanzados, adiooooos amigoooous")   
        
    def mostrar_sesion_fallido(self, intentos_usuario):
            print("Usuario o Contraseña incorrectos. Intenta de nuevo")
            return intentos_usuario+1
            
        
    def msotrar_menu_estudiante(self):
        opcion = 0
        while opcion !=3:
            print("\n**MINDBOX**")
            print("1. Ver horarios")
            print("2. Ver grupos")
            print("3. Ver maestros")
            print("4. Ver semestres")
            print("5. Salir")
            #!Agregar opciones que creemos que van 
            
            opcion = int(input("Ingresa una opcion: "))
            
            if opcion == 3:
                break
            
    
    
    def msotrar_menu_maestros(self):
        opcion = 0
        while opcion !=5:
            print("\n**MINDBOX**")
            print("1. Ver horarios")
            print("2. Ver grupos")
            print("2. Ver materias")
            print("2. Ver alumnos")
            print("5. Salir")
            #?Agregar opciones que creemos que van
            #
            opcion = int(input("Ingresa una opcion: "))
            
            if opcion == 5:
                break 
            
    def msotrar_menu(self):


        while True:
            print("**MINDBOX**")
            print("1. Registrar Estudinate")
            print("2. Registrar Maestro")
            print("3. Registrar Materia")
            print("4. Registrar Grupo")
            print("5. Registrar Horario")
            print("6. Mostrar Estudiantes")
            print("7. Mostrar Maestros")
            print("8. Mostrar Materias")
            print("9. Mostrar Grupos")
            print("10. Mostrar Semestres")
            print("11. Mostrar Carreras")
            print("12. Eliminar Estudiante")
            print("13. Eliminar Maestro")
            print("14. Eliminar Materia")
            print("15. Registrar Carrera")
            print("16. Registrar Semestre")
            print("17. Salir")
            
            opcion = input("Ingresa una opcion para continuar: ")
            
            if opcion == "1":
                print("\nSeleccionaste *Registrar estudiante*")
                
                num_control = self.escuela.generar_num_control()
                print("#control: ", num_control)
                
                nombre = input("Ingresa el nombre del estudiante:")
                apellido = input("Ingresa el apellido del estudiante:")
                curp = input("Ingresa la CURP del estudiante:")
                ano = int(input("Ingresa el año de nacimiento del estudiante:"))
                mes = int(input("Ingresa el mes de nacimiento del estudiante:"))
                dia = int(input("Ingresa el dia de nacimiento del estudiante:"))
                fecha_nacimiento = datetime(ano, mes, dia)
                
                contrasena= input("Ingresa la contraseña del estudiante: ")
                
                estudiante=Estudiante(num_control=num_control,nombre=nombre, apellido=apellido,curp=curp,fecha_nacimiento=fecha_nacimiento, contrasena=contrasena)
                self.escuela.registrar_estudiante(estudiante=estudiante)
                
                
            elif opcion == "2":
                print("\nSeleccionaste *Registrar maestro*")
                
                nombre = input("Ingresa el nombre del maestro:")
                apellido = input("Ingresa el apellido del maestro:")
                rfc = input("Ingresa el RFC del maestro:")
                ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro:"))
                sueldo = float(input("Ingresa el sueldo del maestro:"))
                
                num_control = self.escuela.num_control_maestro(nombre=nombre, rfc=rfc, ano_nacimiento=ano_nacimiento)
                
                print("#control: ", num_control)
                contrasena= input("Ingresa la contraseña del Maestro: ")
                maestro= Maestro(num_control=num_control ,nombre=nombre, apellido=apellido, rfc=rfc, fecha_naci=ano_nacimiento, sueldo=sueldo, contrasena=contrasena)
                self.escuela.registrar_maestros(maestro=maestro)
                
                
            elif opcion == "3":
                
                print("\nSeleccionaste *Registrar Materia*")
                
                nombre = input("Ingresa el nombre de la materia: ")
                descripcion = input("Ingresa la descripcion: ")
                semestre = int(input("Ingresa el semestre de la materia: "))
                creditos= int(input("Ingresa los creditos de la materia: "))
                id = self.escuela.id_materia(nombre=nombre, semestre=semestre, creditos=creditos)
                print("id de la materia: ", id )
                materia = Materia(id,nombre,descripcion,semestre,creditos)
                self.escuela.registrar_materia(materia=materia)
                
            elif opcion == "4":
                print("\n Seleccionaste Registrar un nuevo grupo")
                tipo = input("ingresa el tipo de grupo (A/B): ")
                id_semestre = input("Ingresa el ID del semetsre al que pertenece el grupo: ")
                grupo = Grupo(tipo=tipo, id_semestre= id_semestre)
                self.escuela.registrar_grupo(grupo)
                
                
            elif opcion == "5":
                pass
            elif opcion == "6":
                self.escuela.listar_estudinates()
                
            elif opcion == "7":
                self.escuela.listar_maestro()
                
            elif opcion == "8":
                self.escuela.listar_materia()
                
            elif opcion == "9":
                self.escuela.listar_grupo()
                
            elif opcion == "10":
                self.escuela.listar_semestre()
                
            elif opcion == "11":
                self.escuela.listar_carrera()
                
            elif opcion == "12":
                print("Seleccionaste eliminar un estudiante")
                numero_control = input("Ingresa el numero de control del estudiante")
                self.escuela.eliminar_estudinate(numero_control=numero_control)
                
            elif opcion == "13":
                
                print("Seleccionaste eliminar un maestro")
                num_control = input("Ingresa el numero de control del maestro: ")
                self.escuela.eliminar_maestro(numero_control=num_control)
                
            elif opcion == "14":
                
                print("Seleccionaste eliminar un materia")
                num_control = input("Ingresa el numero de control del maestro: ")
                self.escuela.eliminar_materia(numero_control=num_control)
            
            elif opcion == "15":
                print("\n seleccionaste registrar carrera:")
                nombre = input("ingresa el nombre de la carrera: ")
                carrera= Carrera(nombre=nombre)
                
                self.escuela.registrar_carrera(carrera=carrera)
            
            elif opcion == "16":
                print("\nSeleccionaste registrar un semestre: ")
                numero = input("Ingresa el numero del semestre: ")
                id_carrera = input("Ingresa el ID de la carrera: ")
                semestre = Semestre(numero, id_carrera)
                self.escuela.registrar_semestre(semestre)
                
                
                
            elif opcion == "17":
                print("\nADIOS")
                break
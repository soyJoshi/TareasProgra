from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from maestros.maestro import Maestro
from materias.materia import Materia

escuela = Escuela()

while True:
    print("**MINDBOX**")
    print("1. Registrar Estudinate")
    print("2. Registrar Maestro")
    print("3. Registrar Materia")
    print("4. Registrar Grupo")
    print("5. Registrar Horario")
    
    opcion = input("Ingresa una opcion para continuar: ")
    
    if opcion == "1":
        print("\nSeleccionaste *Registrar estudiante*")
        
        num_control = escuela.generar_num_control()
        print("#control: ", num_control)
        
        nombre = input("Ingresa el nombre del estudiante:")
        apellido = input("Ingresa el apellido del estudiante:")
        curp = input("Ingresa la CURP del estudiante:")
        ano = int(input("Ingresa el año de nacimiento del estudiante:"))
        mes = int(input("Ingresa el mes de nacimiento del estudiante:"))
        dia = int(input("Ingresa el dia de nacimiento del estudiante:"))
        fecha_nacimiento = datetime(ano, mes, dia)
        escuela.registrar_estudiante(estudiante=Estudiante)
        
        
    elif opcion == "2":
        print("\nSeleccionaste *Registrar maestro*")
        
        nombre = input("Ingresa el nombre del maestro:")
        apellido = input("Ingresa el apellido del maestro:")
        rfc = input("Ingresa el RFC del maestro:")
        ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro:"))
        sueldo = float(input("Ingresa el sueldo del maestro:"))
        
        num_control = escuela.num_control_maestro(nombre=nombre, rfc=rfc, ano_nacimiento=ano_nacimiento)
        
        print("#control: ", num_control)
        escuela.registrar_maestros(maestro=Maestro)
        
        
    elif opcion == "3":
        
        print("\nSeleccionaste *Registrar Materia*")
        
        nombre = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripcion: ")
        semestre = int(input("Ingresa el semestre de la materia: "))
        creditos= int(input("Ingresa los creditos de la materia: "))
        id = escuela.id_materia(nombre=nombre, semestre=semestre, creditos=creditos)
        print("id de la materia: ", id )
        escuela.registrar_materia(materia=Materia)
        
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        print("\nADIOS")
        break
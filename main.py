from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from maestros.maestro import Maestro
from materias.materia import Materia

escuela = Escuela()


while True:
    print("\n**MINDBOX**")
    print("1. Registrar Estudinate")
    print("2. Registrar Maestro")
    print("3. Registrar Materia")
    print("4. Registrar Grupo")
    print("5. Registrar Horario")
    print("6. Mostrar Estudiantes")
    print("7. Mostrar Maestro")
    print("8. Mostrar Materias")
    print("9. Mostrar Grupos")
    print("10. Eliminar Estudiante")
    print("11. Eliminar Maestro")
    print("12. Eliminar Materia")
    print("13. Salir")
    
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
        estudiante=Estudiante(num_control=num_control,nombre=nombre, apellido=apellido,curp=curp,fecha_nacimiento=fecha_nacimiento)
        escuela.registrar_estudiante(estudiante=estudiante)
        
        
    elif opcion == "2":
        print("\nSeleccionaste *Registrar maestro*")
        
        nombre = input("Ingresa el nombre del maestro:")
        apellido = input("Ingresa el apellido del maestro:")
        rfc = input("Ingresa el RFC del maestro:")
        ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro:"))
        sueldo = float(input("Ingresa el sueldo del maestro:"))
        
        num_control = escuela.num_control_maestro(nombre=nombre, rfc=rfc, ano_nacimiento=ano_nacimiento)
        
        print("#control: ", num_control)
        maestro= Maestro(num_control=num_control ,nombre=nombre, apellido=apellido, rfc=rfc, fecha_naci=ano_nacimiento, sueldo=sueldo)
        escuela.registrar_maestros(maestro=maestro)
        
        
    elif opcion == "3":
        
        print("\nSeleccionaste *Registrar Materia*")
        
        nombre = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripcion: ")
        semestre = int(input("Ingresa el semestre de la materia: "))
        creditos= int(input("Ingresa los creditos de la materia: "))
        id = escuela.id_materia(nombre=nombre, semestre=semestre, creditos=creditos)
        print("id de la materia: ", id )
        materia = Materia(id,nombre,descripcion,semestre,creditos)
        escuela.registrar_materia(materia=materia)
        
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        escuela.listar_estudinates()
        
    elif opcion == "7":
        escuela.listar_maestro()
        
    elif opcion == "8":
        escuela.listar_materia()
        
    elif opcion == "9":
        pass
    elif opcion == "10":
        print("Seleccionaste eliminar un estudiante")
        numero_control = input("Ingresa el numero de control del estudiante: ")
        escuela.eliminar_estudinate(numero_control=numero_control)
        
    elif opcion == "11":
        
        print("Seleccionaste eliminar un maestro")
        num_control = input("Ingresa el numero de control del maestro: ")
        escuela.eliminar_maestro(numero_control=num_control)
        
    elif opcion == "12":
        
        print("Seleccionaste eliminar un materia")
        num_control = input("Ingresa el ID de la materia: ")
        escuela.eliminar_materia(numero_control=num_control)
        
    elif opcion == "13":
        print("\nADIOS")
        break
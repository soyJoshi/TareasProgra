from paciente.paciente import Paciente
from hospital.hospital import Hospital
from medico.medico import Medico

hospital = Hospital()


while True:
    print("\n*** BIENVENIDO ***")
    print("opciones en el sistema:")
    print("1.Registrar pacientes")
    print("2.Registrar medico")
    print("3.mostrar pacientes")
    print("4.mostrar medicos")
    print("5.Eliminar paciente")
    print("6.Eliminar Medico")
    print("7.Mostrar pacientes menores de edad")
    print("8.Mostrar pacientes mayores de edad")
    print("9.Salir")
    
    opcion_usuario = input("selecciona la opcion deseada: ")
    
    if opcion_usuario == "1":
        print("seleccionaste registrar un paciente")
        
        nombre = input("ingresa el nombre: ")
        ano_nacimiento = int(input("ingresa el año de nacimiento: "))
        peso = float(input("ingresa el peso: "))
        estatura = float(input("ingresa la estatura: "))
        direccion = input("ingresa la direccion: ")
        
        paciente = Paciente(nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente=paciente)
        print("\nPaciente registrado con exito")
        
    elif opcion_usuario == "2":
        print("seleccionaste registrar un medico")
        
        nombre = input("ingresa el nombre: ")
        ano_nacimiento = int(input("ingresa el año de nacimiento: "))
        rfc = input("ingresa el RFC: ")
        direccion = input("ingresa la direccion: ")
        
        medico = Medico(nombre=nombre, ano_nacimiento=ano_nacimiento, rfc=rfc, direccion=direccion)
        hospital.registrar_medico(medico=medico)
        print("\nMedico registrado con exito")
    
    elif opcion_usuario == "3":
        hospital.mostrar_pacientes()
        
    elif opcion_usuario =="4":
        hospital.mostrar_medicos() 
        
    elif opcion_usuario =="5":
        id_eliminar = int(input("Ingrese el ID del paciente a eliminar: "))
        hospital.eliminar_paciente(id_eliminar)
        print("Paciente Eliminado correctamente") 
        
    elif opcion_usuario =="6":
        id_eliminar = int(input("Ingrese el ID del medico a eliminar: "))
        hospital.eliminar_doctor(id_eliminar)
        print("Medico Eliminado correctamente")  
        
    elif opcion_usuario =="7":
        hospital.mostrar_pacientes_menores_de_edad() 
        
    elif opcion_usuario =="8":
        hospital.mostrar_pacientes_mayores_de_edad()
        
    elif opcion_usuario == "9":
        print("hasta luego")
        break
      
    
    
        
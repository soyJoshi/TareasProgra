from paciente import Paciente
from hospital import Hospital
from medico import Medico

hospital = Hospital()

paciente = Paciente("Juan", 2004, 76, 1.78, "Avenida Madero")
paciente_dos = Paciente("Lorenzo", 2006, 80, 1.98, "Avenida Madero")
paciente_tres = Paciente("Karen", 2007, 60, 1.65, "San Jose")
hospital.registrar_paciente(paciente = paciente)
hospital.registrar_paciente(paciente = paciente_dos)
hospital.registrar_paciente(paciente = paciente_tres)

medico = Medico("Alberto", 1900, "ALB4917BNDDDF","Av. Periodismo")
medico_2 = Medico("Ernesto", 1982, "584KSJAK41KLK","Av. Pedregal")
hospital.registrar_medico(medico = medico)
hospital.registrar_medico(medico = medico_2)

hospital.registrar_consulta(id_paciente = 1, id_medico = 2)

while True:
    print("\n*** BIENVENIDO ***")
    print("opciones en el sistema:")
    print("1.Mostrar pacientes")
    print("2.Mostrar pacientes menores de edad")
    print("3.Mostrar pacientes mayores de edad")
    print("4.Mostrar Medicos")
    print("5.Eliminar paciente")
    print("6.Eliminar Medico")
    print("7.Salir")
    
    opcion = input("Ingresa la opcion que deseas: ")
    if opcion == "1":
        hospital.mostrar_pacientes()
        
    elif opcion == "2":
        hospital.mostrar_pacientes_menores_de_edad()
    
    elif opcion == "3":
        hospital.mostrar_pacientes_mayores_de_edad()
        
    elif opcion == "4":
        hospital.mostrar_medicos()
        
    elif opcion == "5":
        id_a_eliminar = int(input("Ingresa el ID del paciente a eliminar: "))
        hospital.eliminar_paciente(id_a_eliminar)
        print("paciente eliminado correctamente")
    
    elif opcion == "6":
        id_a_eliminar = int(input("Ingresa el ID del paciente a eliminar: "))
        hospital.eliminar_doctor(id_a_eliminar)
        print("Medico eliminado correctamente")
       
    else:
        print("\nAdios")
        break

        
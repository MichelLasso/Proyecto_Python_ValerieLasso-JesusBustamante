#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import random
from os import system

nose = []
aprobados = set()
desaprobados = set()
notamodulo = []
aprobado = []
desaprobado = []
Sputnik = []
Apolo = []
Artemis = []

simodulo = "Modulo aprobado"
nomodulo = "Modulo desaprobado"
si= "Aprobado"
no="Desaprobado"

with open('academico.json','r') as openfile:
    miJSON= json.load(openfile)

with open("inscritos.json","r") as openfile:
    inscritos= json.load(openfile)

with open('trainer.json','r') as openfile:
    trai= json.load(openfile)

with open('coordinador.json','r') as openfile:
    coor= json.load(openfile)

with open('rutas.json','r') as openfile:
    rutas= json.load(openfile)

with open('notamodulo.json','r') as openfile:
    notamodulo= json.load(openfile)

with open("aprobados.json","r") as openfile:
    aprobado= json.load(openfile)

with open('desaprobados.json','r') as openfile:
    desaprobado= json.load(openfile)

with open('camTraRu.json','r') as openfile:
    nose = json.load(openfile)


for i in range (len(miJSON)):
        if (miJSON[i]["salon"]=="Sputnik"):
            Sputnik.append(miJSON[i])

for i in range (len(miJSON)):
        if (miJSON[i]["salon"]=="Apolo"):
            Apolo.append(miJSON[i])

for i in range (len(miJSON)):
        if (miJSON[i]["salon"]=="Artemis"):
            Artemis.append(miJSON[i])



print("------------------------------------------------")
print("                 CAMPUSLAND                     ")
print("------------------------------------------------\n")

opcion = input(str("""       Elige tu cargo para iniciar sesión      

                1. Trainer
                2. Coordinador
------------------------------------------------\n"""))



if opcion == "Trainer":
   
    system("cls")

    print("------------------------------------------------")   
    print("             BIENVENIDO TRAINER                 ")
    print("------------------------------------------------\n")   
    print("")
            
    usuario = int(input("Número de Identificación: "))
    print("")
    password = input("Password: ")

    for i in trai:
        for x in i["trainer"]:
            if x["id"] == usuario:
                if "contrasena" in x and x["contrasena"] == password:
                    print("Ingreso válido Trainer", x["nombre"])
                else:
                    print("Contraseña incorrecta")
            else:
                print("ID inválido")
    
if opcion == "Coordinador":

    system("cls")  

    print("------------------------------------------------")   
    print("           BIENVENIDO COORDINADOR               ")
    print("------------------------------------------------\n")   
    print("")
            
    usuario = int(input("Número de Identificación: "))
    print("")
    Contraseña = input("Contraseña: ")
    print("")
    system("cls")

    for i in coor:
        for x in i["coordinador"]:

            if x["id"] == usuario:

                if "contrasena" in x and x["contrasena"] == Contraseña:
                    print("Ingreso exitoso Coordinador", x["nombre"])
                    print("")

                    respuestaUsuario = int(input("Elije una opción\n\n1. Inscribir campers\n2. Registrar notas\n3. Crear nuevas rutas\n4. Módulo de matrículas\n5. Consultar campers en alto riesgo\n6. Módulo de reportes\n\n"))
                    
                    if respuestaUsuario == 1:
                        print("--------------------------------------------------------")
                        print("             Inscripción de estudiantes                 ")
                        print("--------------------------------------------------------\n\n")
                        
                        

                        identificacion = int(input("Identificación\n"))
                        print("")
                        nombres = input("Nombres\n")
                        print("")
                        apellidos = input("Apellidos\n")
                        print("")
                        direccion = input("Dirección\n")
                        print("")
                        acudiente = input("Nombres y apellidos de acudiente\n")
                        print("")
                        nfijo = input("Número fijo\n")
                        print("")
                        celular = input("Número celular\n")
                        print("")
                        estado = input("Estado (inscrito)\n")

                        inscritosnew = {

                            "identificacion": identificacion,
                            "nombres": nombres,
                            "apellidos": apellidos,
                            "direccion": direccion,
                            "acudiente": acudiente,
                            "nfijo": nfijo,
                            "celular": celular,
                            "estado": estado
                        } 

                
                        inscritos[0]["inscritos"] += [inscritosnew]

                        with open("inscritos.json", 'w') as f:
                            json.dump(inscritos,f,indent=4)



                    if respuestaUsuario == 2:
                        
                        system("cls")

                        print("------------------------------------------------")   
                        print("                INGRESAR NOTAS                  ")
                        print("------------------------------------------------\n")   
                        print("")

                        print("------------------------------------------------")   
                        print("             1. Prueba inicial\n             2. Módulo      ")
                        print("------------------------------------------------\n")   
                        print("")
                        nota = int(input(""))
                        print("")

                        if nota==1:

                            contador = 1
                            for i in inscritos:
                                for x in i["inscritos"]:

                                    print(contador, f"{x["nombres"]} {x["apellidos"]}\n")
                                    contador = contador + 1

                                estudiante = input("Ingrese el nombre del estudiante que desea revisar\n")
                                print("")
                                apellido = input("Ingrese el apellido del estudiante que desea revisar\n")

                                for i in inscritos:

                                    for x in i["inscritos"]:

                                        if x["nombres"] == estudiante:
                                            if "apellidos" in x and x["apellidos"] == apellido:
                                                system("cls")
                                                print("------------------------------------------------")   
                                                print(f"  DATOS: {x["nombres"]} {x["apellidos"]}")
                                                print("------------------------------------------------\n")   
                                                print("")

                                                
                                                print(f"  Identificación: {x["identificacion"]}")
                                                print(f"  Dirección: {x["direccion"]}")
                                                print(f"  Acudiente: {x["acudiente"]}")
                                                print(f"  Número Fijo: {x["nfijo"]}")
                                                print(f"  Celular: {x["celular"]}")
                                                print(f"  Estado: {x["estado"]}")
                                                print("")

                                                bool = True
                                                while bool:

                                                    print("Ingrese las notas de la prueba inicial \n")
                                                    PorcentajeMayor = int(input("Nota práctica 70% :\n"))
                                                    PorcentajeMenor = int(input("Nota teórica 30% :\n"))
                                                    

                                                    if 100 >= PorcentajeMayor and PorcentajeMenor >= 1:
                                                        resultado = ((PorcentajeMayor * 0.7) + (PorcentajeMenor * 0.30))

                                                        if resultado >= 60:
                                                            if x["identificacion"] not in aprobados:
                                                                print("")
                                                                x["estado"] = [resultado, si]
                                                                aprobado += [x]
                                                                aprobados.add(x["identificacion"])
                                                                print("")        
                                                                print(x["nombres"], x["apellidos"])
                                                                print(si)

                                                        else:
                                                            if x["identificacion"] not in desaprobado:
                                                                print("")
                                                                x["estado"] = [resultado, no]
                                                                desaprobado += [x]
                                                                desaprobados.add(x["identificacion"])
                                                                print("")        
                                                                print(x["nombres"], x["apellidos"])
                                                                print(no)
                                                            
                                                        bool = False
                                                    else:
                                                        print("La nota supera el límite ")
                                                        print("Ingrese las notas nuevamente")

                                                    
                                                    for item in inscritos:
                                                        
                                                        if resultado>=60:
                                                            if x not in aprobado:
                                                                aprobados.add(x["identificacion"])
                                                                item["estado"] = [resultado, si]
                                                        else:
                                                            if x not in desaprobado:
                                                                aprobados.add(x["identificacion"])
                                                                item["estado"] = [resultado, no]

                                                    
                                                    with open('desaprobados.json','w') as f:
                                                        json.dump(desaprobado,f,indent=4)

                                                    with open("aprobados.json", 'w') as f:
                                                        json.dump(aprobado,f,indent=4)
                                            

                        elif nota==2:

                            contador = 1
                            for i in aprobado:
    

                                    print(contador, f"{i["nombres"]} {i["apellidos"]}\n")
                                    contador = contador + 1

                            estudiante = input("Ingrese el nombre del estudiante que desea revisar\n")
                            print("")
                            apellido = input("Ingrese el apellido del estudiante que desea revisar\n")

                            for i in aprobado:

                                
                                    if i["nombres"] == estudiante:
                                        if "apellidos" in i and i["apellidos"] == apellido:
                                            system("cls")
                                            print("------------------------------------------------")   
                                            print(f"  DATOS: {i["nombres"]} {i["apellidos"]}")
                                            print("------------------------------------------------\n")   
                                            print("")

                                            
                                            print(f"  Identificación: {i["identificacion"]}")
                                            print(f"  Dirección: {i["direccion"]}")
                                            print(f"  Acudiente: {i["acudiente"]}")
                                            print(f"  Número Fijo: {i["nfijo"]}")
                                            print(f"  Celular: {i["celular"]}")
                                            print(f"  Estado: {i["estado"]}")
                                            print("")

                                            bool = True
                                            while bool:

                                                print("Ingrese las notas correspondientes del estudiante\n")
                                                PorcentajeMayor = int(input("Nota práctica 60% :\n"))
                                                PorcentajeMenor = int(input("Nota teórica 30% :\n"))
                                                diez = int(input("Nota de Trabajos 10% :\n"))

                                                if 100 >= PorcentajeMayor and PorcentajeMenor >= 1:
                                                    resultado = ((PorcentajeMayor * 0.6) + (PorcentajeMenor * 0.30) + (diez * 0.1))

                                                    if resultado >= 60:
                                                        print("")
                                                        i["estado"] = simodulo
                                                        print(i["estado"])
                                                        notamodulo += [i]
                                                    else:
                                                        print("")
                                                        i["estado"] = nomodulo
                                                        print(i["estado"])
                                                        notamodulo += [i]
                                                        

                                                    bool = False
                                                else:
                                                    print("La nota supera el límite ")
                                                    print("Ingrese las notas nuevamente")

                                                
                                                for item in aprobado:
                                                    if resultado>=60:
                                                        item["estado"] = simodulo
                                                    else:
                                                        item["estado"] = nomodulo

                                                

                                                with open("notamodulo.json", 'w') as f:
                                                    json.dump(notamodulo,f, indent=4)
                    

                                    
                    elif respuestaUsuario == 3:

                        system("cls")
                        print("Las rutas de entrenamiento existentes son: ")
                        print("")

                        for i in rutas:
                            for x in i["modulos"]:
                                print("-------------------------------------------------------------")
                                print(x["ruta"])
                                print("")
                                print(x["fundamentos"]) 
                                print(x["web"])
                                print(x["formal"])
                                print(x["datos"])
                                print(x["backend"])
                                print("-------------------------------------------------------------")
                                print("")

                        crear = input("¿Quieres crear una nueva ruta de entrenamientos?(si/no)\n")
                        print("")

                        if crear == "si":
                            
                            print("--------------------------------------------------------")
                            print("Ingrese los temas de cada módulo correspondiente")
                            print("")
                            nombre = input("Ingrese el nombre de la nueva ruta\n")
                            print("")
                            fundamento = input("Temas de Fundamentos de la Programación\n")
                            print("")
                            web = input("Programación Web\n")
                            print("")
                            formal = input("Programación Formal\n")
                            print("")
                            datos = input("Bases de Datos\n")
                            print("")
                            backend = input("Backend\n")

                            modulo = {

                                "ruta": nombre,
                                "fundamentos": fundamento,
                                "web": web,
                                "formal": formal,
                                "datos": datos,
                                "backend": backend
                            }

                            nueva_ruta = {
                                "ruta": nombre,
                                "modulos": [modulo]
                            }

                            rutas += [nueva_ruta]

                            with open("rutas.json", 'w') as f:
                                json.dump(rutas,f,indent=4)

                            system("cls")
                            
                            print("------------------------------------------------")   
                            print("              RUTAS ACTUALIZADAS                ")
                            print("------------------------------------------------\n")   
                            print("")
                            
                            for i in rutas:
                                for x in i["modulos"]:
                                    print("-------------------------------------------------------------")
                                    print(x["ruta"])
                                    print("")
                                    print(x["fundamentos"]) 
                                    print(x["web"])
                                    print(x["formal"])
                                    print(x["datos"])
                                    print(x["backend"])
                                    print("-------------------------------------------------------------")
                                    print("")

                    elif respuestaUsuario == 4:
                        
                        print("------------------------------------------------")   
                        print("              MÓDULO DE MATRICULAS                ")
                        print("------------------------------------------------\n")   
                        print("")

                        for i in aprobado:
                            i["id"] = random.choice(trai)
                            i["ruta"] = random.choice(rutas)

                        with open("camTraRu.json", "w") as openfile:
                            json.dump(aprobado, openfile, indent=4)

                        print(nose)
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                        # print("Campers Aprobados")
                        # print("")

                        # contador = 1
                        # for i in aprobado:
                           

                        #         print(contador, f"{i["nombres"]} {i["apellidos"]} : {i["estado"]}\n")
                        #         contador = contador + 1

                        

                                                    #                         8. La coordinación académica desea contar con un módulo de matriculas que le permita
                                                    # asignar los campers aprobados, trainer encargado, ruta de entrenamiento asignada, fecha de inicio, fecha finalización y salón de entrenamiento.






                    elif respuestaUsuario==6:
                        
                        print("------------------------------------------------")   
                        print("              MÓDULO DE REPORTES                ")
                        print("------------------------------------------------\n")   
                        print("")
                        modulo = int(input("""      

                        1. Listar los campers que se encuentren en estado de inscrito.
                        2. Listar los campers que aprobaron el examen inicial.
                        3. Listar los entrenadores que se encuentran trabajando con *CampusLands*.
                        4. Listar los campers que cuentan con bajo rendimiento.
                        5. Listar los campers y trainers que se encuentren asociados a una ruta de entrenamiento.
                        6. Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.
                        ------------------------------------------------\n"""))
                        if modulo==1:

                            system("cls")
                            
                            print("------------------------------------------------")   
                            print("              CAMPERS INSCRITOS                 ")
                            print("------------------------------------------------\n")   

                            print("Acontinuación se mostrará los campers que se han inscrito en Campus con el estado actual")
                            contador = 1

                            for i in miJSON:

                                for x in i["estudiantes"]:

                                    print(contador, x["nombres"], x["apellidos"])
                                    print(x["estado"])
                                    print("")
                                    contador=contador+1

                        if modulo==2:

                            system("cls")
                            
                            print("------------------------------------------------")   
                            print("              CAMPERS APROBADOS                 ")
                            print("------------------------------------------------\n")   

                            for i in aprobado:
                                    
                                    contador=1
                                    print(contador, i["nombres"], i["apellidos"])
                                    print(i["estado"])
                                    print("")
                                    contador=contador+1

                        if modulo==3:

                            system("cls")

                            print("------------------------------------------------")   
                            print("                  TRAINERS                      ")
                            print("------------------------------------------------\n") 

                            contador=1
                            for i in trai:
                                for x in i["trainer"]:
                                    print(contador, x["nombre"])
                                    print("")
                                    contador=contador+1

                        if modulo==4:

                            system("cls")

                            print("------------------------------------------------")   
                            print("         CAMPERS CON BAJO RENDIMIENTO           ")
                            print("------------------------------------------------\n") 

                            contador=1

                            for i in notamodulo:
                               
                                if i["estado"]=="Modulo desaprobado":
                                    
                                    print(contador, i["nombres"], i["apellidos"])
                                    print(i["estado"])
                                    print("")
                                    contador=contador+1




                else:
                    print("Contraseña incorrecta")
            else:
                print("ID inválido") 
                                    
                                    

                                

                                

                                
                                        


                                        



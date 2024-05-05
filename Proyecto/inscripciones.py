#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import json #llamar el json
from os import system #para limpiar pantalla
import copy

#listas vacias de los json
nose = []
notamodulo = []
aprobado = []
desaprobado = []
Sputnik = []
Apolo = []
Artemis = []

#ASIGNACION DE VARIABLES QUE USAREMOS MAS ADELANTE//NOTAS
simodulo = "Modulo aprobado"
nomodulo = "Modulo desaprobado"
si= "Aprobado"
no="Desaprobado"

#CREAR LISTAS PARA LOS JSON
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

with open('rutrai.json','r') as openfile:
    rutica = json.load(openfile)


for i in range (len(miJSON)):#BORRAR
        if (miJSON[i]["salon"]=="Sputnik"):
            Sputnik.append(miJSON[i])

for i in range (len(miJSON)):#BORRAR
        if (miJSON[i]["salon"]=="Apolo"):
            Apolo.append(miJSON[i])

for i in range (len(miJSON)):#BORRAR
        if (miJSON[i]["salon"]=="Artemis"):
            Artemis.append(miJSON[i])


bool=True
while bool==True:
    system("cls")
    print("------------------------------------------------")#PRIMER MENU
    print("                 CAMPUSLAND                     ")
    print("------------------------------------------------\n")

    opcion = input(str("""       Elige tu cargo para iniciar sesión      

                    1. Trainer
                    2. Coordinador
                    3. Camper
    ------------------------------------------------\n"""))


    if opcion == "Trainer":
        system("cls")

        print("------------------------------------------------")   
        print("             BIENVENIDO TRAINER                 ")
        print("------------------------------------------------\n")   
        print("")
        
        while True: #BUCLE INFINITO Y TERMINA HASTA QUE EL USUARIO INGRESE EL ID U CONTRASEÑA VALIDOS

            usuario = int(input("Número de Identificación: "))#DATO 1 DEL TRAINER/ID
            print("")
            password = input("Contraseña: ")#DATO 2 DEL TRAINER/CONTRASEÑA

            usuario_valido = False

            for i in trai: #RECOORE LA LISTA DE TRAINERS
                for x in i["trainer"]:

                    if x["id"] == usuario: #SI EL ID DEL TRAINER COINCIDE CON EL QUE ESTA EN EL JSON
                        
                        if "contrasena" in x and x["contrasena"] == password:#SI LA CONTRASEÑA DEL USURIO COINCIDE CON EL QUE ESTA EN EL JSON 

                            system("cls")#Borrar Pantalla                      
                            print("Ingreso válido Trainer", x["nombre"]) #IMPRIME UN MENSAJE DE VALIDACION

                            opcionmenut= input ("menu......\n2. Cerrar Sesión\n")

                            if opcionmenut==1:
                                print("faltan cositas")
                            
                            elif opcionmenut==2:

                                system("cls")

                                print("------------------------------------------------")   
                                print("                 CERRAR SESION                  ")
                                print("------------------------------------------------\n") 

                                sino=int(input("Desea cerrar sesión? \n1.Si\n2.No\n"))

                                if sino==1:
                                    
                                    system("cls")
                                    print("Cerrando sesión...")
                                    time.sleep(3)
                            
                            usuario_valido = True #FINALIZACION DEL BUCLE
                            
                            break  # SALIR EL BUCLE
                        else:
                            print("\nContraseña incorrecta\n")
                            break  # SALIR DEL BUCLE EXTERNO /SE REPITE LA PREGUNTA

            if usuario_valido:#SI LOS DATOS SON VALIDOS TERMINA EL BUCLE
                    break  #PARA QUE NO ME MUESTRE UNA LISTA DE LOS TRAINERS QUE NO COINCIDEN CON LOS DATOS
            else:
                system("cls")#BPRRAR PANTALLA
                print("ID inválido. Por favor, intenta de nuevo.\n")
                    
        break

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

                        respuestaUsuario = int(input("Elije una opción\n\n1. Inscribir campers\n2. Registrar notas\n3. Crear nuevas rutas\n4. Módulo de matrículas\n5. Consultar campers en alto riesgo\n6. Módulo de reportes\n7. Cerrar sesión\n\n"))
                        
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
                                                                
                                                                print("")
                                                                x["estado"] = si
                                                                aprobado += [x]
                                                                print("")        
                                                                print(x["nombres"], x["apellidos"])
                                                                print(si)
                                                                print("")
                                                                
                                                                salon = int(input("Elija el área de entrenamiento del alumno\n\n1.Sputnik\n2.Apolo\n3.Artemis\n\n"))

                                                                for a in miJSON:

                                                                    Cambiocursando = copy.deepcopy(x)
                                                                    Cambiocursando["estado"] = "Cursando"

                                                                    
                                                                    if salon == 1 and a["salon"] == "Sputnik":
                                                                        
                                                                        miJSON[0]["estudiantes"] += [Cambiocursando]
                                                                                

                                                                    if salon == 2 and a["salon"] == "Apolo":
                                                                        
                                                                        miJSON[1]["estudiantes"] += [Cambiocursando]
                                                                        

                                                                    if salon == 3 and a["salon"] == "Artemis":
                                                                        
                                                                        miJSON[2]["estudiantes"] += [Cambiocursando]
                                                                

                                                            else:
                                                                    
                                                                print("")
                                                                x["estado"] = no
                                                                desaprobado += [x]
                                                                print("")        
                                                                print(x["nombres"], x["apellidos"])
                                                                print(no)
                                                         
                                                            bool = False

                                                        else:
                                                            print("La nota supera el límite ")
                                                            print("Ingrese las notas nuevamente")

                                                        
                                                        for item in inscritos:
                                                            
                                                            if resultado>=60:
                                                                item["estado"] = si
                                                            else:
                                                                item["estado"] = no


                                                        with open('desaprobados.json','w') as f:
                                                            json.dump(desaprobado,f,indent=4)

                                                        with open("aprobados.json", 'w') as f:
                                                            json.dump(aprobado,f,indent=4)

                                                        with open("academico.json", "w") as f:
                                                            json.dump(miJSON,f, indent=4)
                                                

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
                                                        i["estado"] = "Cursante, módulo aprobado"
                                                        print(i["estado"])
                                                        notamodulo += [i]
                                                                    
                                                    else:
                                                        print("")
                                                        i["estado"] = "Cursante, módulo desaprobado"
                                                        print(i["estado"])
                                                        notamodulo += [i]
                                                
                                                    bool = False
                                                else:
                                                    print("La nota supera el límite ")
                                                    print("Ingrese las notas nuevamente")

                                                
                                                for item in aprobado:
                                                    if resultado>=60:
                                                        item["estado"] = "Cursante, modulo aprobado"
                                                    else:
                                                        item["estado"] = "Cursante, modulo desaprobado"


                                                with open("academico.json", "w") as f:
                                                    json.dump(miJSON,f, indent=4)

                                                with open("notamodulo.json", 'w') as f:
                                                    json.dump(notamodulo,f, indent=4)
                    

                                        
                        elif respuestaUsuario == 3:

                            system("cls")
                            print("Las rutas de entrenamiento existentes son: ")
                            print("")

                            for i in rutas: #MOSTRAR TODAS LAS RUTAS QUE HAY
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
                                print("--------------------------------------------------------")
                                print("")#ELEGIR LOS MODULOS DE LA RUTA CON UN MENU
                                nombre = input("Ingrese el nombre de la nueva ruta\n\n")
                                print("")

                                formal = int(input("Programación Formal:\n1.Java\n2.JavaScript\n3.C#\n\n"))
                                print("")
                                if formal == 1:
                                    formal = "Java"

                                elif formal == 2:
                                    formal = "JavaScript"

                                elif formal == 3:
                                    formal = "C#"

                                datos = int(input("Bases de Datos: Principal:\n1.Mysql\n2.MongoDb\n3.Postgresql\n\n"))
                                print("")
                                if datos == 1:
                                    datos = "Mysql"

                                elif datos == 2:
                                    datos = "MongoDb"

                                elif datos == 3:
                                    datos = "Postgresql"

                                datos2 = int(input("Bases de Datos: Alternativa:\n1.Mysql\n2.MongoDb\n3.Postgresql\n\n"))
                                print("")
                                if datos2 == 1:
                                    datos2 = "Mysql"

                                elif datos2 == 2:
                                    datos2 = "MongoDb"

                                elif datos2 == 3:
                                    datos2 = "Postgresql"

                                backend = int(input("Backend:\n1.NetCore\n2.Spring Boot\n3.NodeJS\n4.Express\n\n"))
                                print("")
                                if backend == 1:
                                    backend = "Netcore"

                                if backend == 2:
                                    backend = "Spring Boot"

                                if backend == 3:
                                    backend = "NodeJS"

                                if backend == 4:
                                    backend = "Express"

                                modulo = {

                                    "ruta": nombre,
                                    "fundamentos": ["fundamentos de la programacion: Introduccion a la algoritmia, PSeint, Python"],#NO CAMBIAN
                                    "web": ["Programacion Web: HTML, CSS, Bootstrap"],#NO CAMBIAN
                                    "formal": ["Programacion Formal ", formal],#SE PUEDE ELEGIR
                                    "datos": ["Base de Datos Principal ", datos],#SE PUEDE ELEGIR
                                    "datos2": ["Base de Datos Alternativa ", datos2],#SE PUEDE ELEGIR
                                    "backend": ["Backend", backend]#SE PUEDE ELEGIR
                                }
                                #PARA CREAR EN EL JSON LA NUEVA RUTA
                                nueva_ruta = {
                                    "ruta": nombre,
                                    "modulos": [modulo]#AGREGAR EL MODULO A LA RUTA
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
                                        print(x["datos2"])
                                        print(x["backend"])
                                        print("-------------------------------------------------------------")
                                        print("")

                        elif respuestaUsuario == 4:
                            # 8. La coordinación académica desea contar con un módulo de matriculas que le permita
                            # asignar los campers aprobados, trainer encargado, ruta de entrenamiento asignada,
                            #fecha de inicio, fecha finalización y salón de entrenamiento.
                            print("------------------------------------------------")   
                            print("              MÓDULO DE MATRICULAS                ")
                            print("------------------------------------------------\n")   
                            print("")

                            #Asignar ruta a Trainer
                            opc = int(input("¿Qué deseas hacer?\n1.Asignación de Rutas a Trainers\n2.Asignación de trainers y rutas a estudiantes\n3.Asignar fecha de incio y finalización\n\n"))

                            if opc == 1:
                                print("---Asignación de Rutas a Trainers---")

                                contador=1
                                for i in trai:
                                    for x in i["trainer"]:
                                        print(contador, x["nombre"])
                                        print("")
                                        contador=contador+1

                                trainer = input("Ingrese el nombre del trainer\n\n")

                                for i in trai:
                                    for x in i["trainer"]:
                                        if x["nombre"] == trainer:
                                            system("cls")
                                            print("------------------------------------------------")   
                                            print(f"         ASIGNACION: {x["nombre"]}            ")
                                            print("------------------------------------------------\n")   
                                            print("")

                                            contador = 1
                                            for i in rutas:
                                                print(contador, i["ruta"])
                                                print("")
                                                contador = contador + 1

                                            aggruta = input("¿Qué ruta desea asignar? Escriba su nombre\n\n")

                                            for i in rutas:
                                                if i["ruta"] == aggruta:
                                                    i["ruta"] = i["ruta"]
                                                    break

                                            try:
                                                with open("rutrai.json", "r") as f:
                                                    existente = json.load(f)
                                            except FileNotFoundError:
                                                existente = [] 

                                            existente.append({"nombre": x["nombre"], "ruta": i["ruta"]})

                                            with open("rutrai.json", "w") as openfile:
                                                json.dump(existente, openfile, indent=4)


                              #Asignar trainer y ruta a estudiantes
                            elif opc == 2:
                                
                                print("----------------------------------------------------")
                                print("    Asignación de trainers y rutas a estudiantes    ")
                                print("----------------------------------------------------")
                                print("")

                                asignar = int(input("¿En qué salón se encuentra el estudiante?\n\n1.Sputnik\n2.Apolo\n3.Artemis\n\n"))

                                if asignar == 1:
                                    system("cls")
                                    print("Estudiantes Sputnik")
                                    print("")

                                    contador = 1
                                    for i in Sputnik:
                                        for x in i["estudiantes"]:

                                            print(contador, f"{x["nombres"]} {x["apellidos"]}\n")
                                            contador = contador + 1

                                    estudiante = input("Ingrese el nombre del estudiante\n\n")
                                    print("")
                                    apellido = input("Ingrese el apellido del estudiante\n\n")
                                    print("")

                                    for i in Sputnik:
                                        
                                        for x in i["estudiantes"]:
                                            if x["nombres"] == estudiante:
                                                if "apellidos" in x and x["apellidos"] == apellido:
                                                    
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

                                print("Trainers y rutas que puedes asignar:\n")

                                contador = 1
                                for i in rutica:
                                        print(contador,f" Trainer: {i["nombre"]} - Ruta: {i["ruta"]}")
                                        contador = contador + 1
                                





                            # print("Campers Aprobados\n")
                            # contador=1
                            # for i in aprobado:
                            
                            #     print(contador, i["nombres"], i["apellidos"])
                            #     print(i["estado"])
                            #     print("")
                            #     contador=contador+1

                            # estudiante = input("Ingrese el nombre del estudiante\n")
                            # print("")
                            # apellido = input("Ingrese el apellido del estudianten\n")

                            # for i in aprobado:
                                    
                            #     if i["nombres"] == estudiante:
                            #         if "apellidos" in i and i["apellidos"] == apellido:

                            #             system("cls")
                            #             print("------------------------------------------------")   
                            #             print(f" ASIGNACION: {i["nombres"]} {i["apellidos"]}")
                            #             print("------------------------------------------------\n")   
                            #             print("")
                                        
                            #             print("---TRAINERS---")
                            #             contador=1
                            #             for i in trai:
                            #                 for x in i["trainer"]:
                            #                     print(contador, x["nombre"])
                            #                     print("")
                            #                     contador=contador+1

                            #             aggTrainer=input("Asignar Trainer\n")
                            #             for i in trai:
                            #                 for x in i["trainer"]:
                            #                     if  x["nombre"]==aggTrainer:
                                                    
                            #                         i["estudiantes"]["nombres"]["trainer"]=i
                                                    
                            #                         miJSON += [i]
                            #                         with open("aprobados.json", 'r+') as f:
                            #                             json.dump(miJSON,f, indent=4)
                            #                         print(x["trainer"])

                            

                                                        




                                                    #print("")

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

                        elif respuestaUsuario==7:
                            
                            system("cls")

                            print("------------------------------------------------")   
                            print("                 CERRAR SESION                  ")
                            print("------------------------------------------------\n") 

                            sino=int(input("Desea cerrar sesión? \n1.Si\n2.No\n"))

                            if sino==1:

                                system("cls")
                                print("Cerrando sesión...")
                                time.sleep(3)
                            
                            




                    else:
                        print("Contraseña incorrecta")
                else:
                    print("ID inválido") 
    break
                                    
    bool==False                               

                                

                                

                                
                                        


                                        



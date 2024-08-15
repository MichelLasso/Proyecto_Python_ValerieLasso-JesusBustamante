#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import datetime
import json #llamar el json
from os import system #para limpiar pantalla
import copy

#listas vacias de los json

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

with open('rutrai.json','r') as openfile:
    rutica = json.load(openfile)

with open("promedioNotas.json","r") as openfile:
    notaP= json.load(openfile)

with open("entradaSesion.json","r") as openfile:
    entradaSesionjson= json.load(openfile)

bool=True
while bool==True:

    pregunta = "si"
    while pregunta.lower() == "si":
        system("cls")
        print("------------------------------------------------")#PRIMER MENU
        print("                 CAMPUSLAND                     ")
        print("------------------------------------------------\n")

        opcion = str(input("""       Elige tu cargo para iniciar sesión 
                                
                        1. Camper
                        2. Trainer
                        3. Coordinador
        ------------------------------------------------\n"""))
        if opcion == "Camper":

            system("cls")

            usuario = input("Ingrese su nombre de usuario\n")
            print("")
            password = int(input("Ingrese su contraseña (ID)\n"))
            print("")

            for i in miJSON:
                for x in i["estudiantes"]:
                    if x["nombres"] == usuario:
                        if "identificacion" in x and x["identificacion"] == password:

                            system("cls")

                            print("------------------------------------------------")   
                            print(f"  DATOS: {x["nombres"]} {x["apellidos"]}")
                            print("------------------------------------------------\n")   
                            print("")

                        
                            print("Dirección: ", x["direccion"])
                            print("Acudiente: ",x["acudiente"])
                            print("Teléfono fijo: ",x["nfijo"])
                            print("Celular: ",x["celular"])
                            print("Estado: ",x["estado"])
                            print("Trainer: ",x["trainer"])
                            print("Ruta: ",x["ruta"])
                            print("Fecha de inicio: ",x["inicio"])
                            print("Fecha de finalización: ",x["finalizacion"])

                            fechasesion = datetime.date.today()
                            actividad = "Revision de sus datos personales"
                            estadoplat = "Activo"

                            entrada = {
                                "id": password,
                                "fecha": fechasesion.strftime("%Y-%m-%d"),
                                "actividad": actividad,
                                "EstadoPlataforma": estadoplat
                            }

                            entradaSesionjson +=[entrada]

                            with open("entradaSesion.json", "w")as b:
                                json.dump(entradaSesionjson, b, indent=4)

                            pregunta = input("\n¿Desea continuar viendo sus datos? Si no, se volverá al menú principal. (si/no)\n")
                            if pregunta.lower() != "si":
                                bool = False

                                tamaño = len(entradaSesionjson)

                                entradaSesionjson[tamaño-1]["EstadoPlataforma"] = "finalizado"

                                with open("entradaSesion.json", "w")as b:
                                    json.dump(entradaSesionjson, b, indent=4)

                            break                     
        break
    
    if opcion == "Trainer":
        
        
        system("cls")

        print("------------------------------------------------")   
        print("             BIENVENIDO TRAINER                 ")
        print("------------------------------------------------\n")   
        print("")
    

        
        usuario = int(input("Número de Identificación: "))#DATO 1 DEL TRAINER/ID
        print("")
        password = input("Contraseña: ")#DATO 2 DEL TRAINER/CONTRASEÑA

        

        for i in trai: #RECORRE LA LISTA DE TRAINERS
            for x in i["trainer"]:

                if x["id"] == usuario: #SI EL ID DEL TRAINER COINCIDE CON EL QUE ESTA EN EL JSON
                    
                    if "contrasena" in x and x["contrasena"] == password:#SI LA CONTRASEÑA DEL USURIO COINCIDE CON EL QUE ESTA EN EL JSON 

                        system("cls")#Borrar Pantalla                     
                        print("Ingreso válido Trainer", x["nombre"]) #IMPRIME UN MENSAJE DE VALIDACION

                        bool = True
                        while bool == True:
                            
                            opcionmenut= int(input ("\n---------------TRAINER--------------\n1. Información Personal\n2. Cerrar Sesión\n"))

                            if opcionmenut==1:
                                
                                system("cls")

                                print("------------------------------------------------")   
                                print("                     DATOS                      ")
                                print("------------------------------------------------\n")   
                                print("")
                            
                                for i in trai:
                                    for a in i["trainer"]:
                                        if a["nombre"] == x["nombre"]:
                                            print("Nombre: ", x["nombre"], x["apellidot"])
                                            print("Identificación: ",x["id"])
                                            print("Contraseña: ",x["contrasena"])

                                            for b in rutica:
                                                if b["nombre"] == x["nombre"]:
                                                    x["ruta"] = b["ruta"]
                                                    print("Ruta asignada: ",x["ruta"])
                                                    print("")
                                        
                                    nose = input("Presione enter para continuar")
                                    system("cls")

                        
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
                                    break
     
                    else:
                        system("cls")
                        print("\nContraseña incorrecta\n")

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

                        respuestaUsuario = int(input("Elije una opción\n\n1. Inscribir campers\n2. Registrar notas\n3. Crear nuevas rutas\n4. Módulo de matrículas\n5. Módulo de reportes\n6. Cerrar sesión\n\n"))
                        
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
                                system("cls")
                                seleccion = input("¿En qué salón se encuentra el estudiante\n1.Sputnik\n2.Apolo\n3.Artemis\n\n")

                                contador = 1
                                for i in miJSON:
                                    if i["salon"] == seleccion:
                                        estudiantes = i["estudiantes"]
                                        break


                                for x in estudiantes:
                                    print(contador, f"{x["nombres"]} {x["apellidos"]}\n")
                                    contador = contador + 1

                                estudiante = input("Ingrese el nombre del estudiante\n\n")
                                print("")
                                apellido = input("Ingrese el apellido del estudiante\n\n")
                                print("")

                                for i in estudiantes:
                                    
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
                                                print(f"  Trainer: {i["trainer"]}")
                                                print(f"  Ruta:  {i["ruta"]}")
                                                print("")

                                            i["modulos"] = {}

                                            notas = 0

                                            for modulo in range(1, 6):
                                                system("cls")
                                                print("Ingrese las notas correspondientes del estudiante para el módulo", modulo)
                                                
                                                PorcentajeMayor = int(input("Nota práctica 60% :\n"))
                                                PorcentajeMenor = int(input("Nota teórica 30% :\n"))
                                                diez = int(input("Nota de Trabajos 10% :\n"))

                                                if 100 >= PorcentajeMayor and PorcentajeMenor >= 1:
                                                    resultado = ((PorcentajeMayor * 0.6) + (PorcentajeMenor * 0.30) + (diez * 0.1))
                                                    notas += resultado

                                                    if resultado >= 60:
                                                        print("")
                                                        i["modulos"][f"Modulo {modulo}"] = (f"[{resultado}] [{"Modulo aprobado"}]")
                                                        print("Modulo Aprobado\n")
                                                        
                                                                    
                                                    else:
                                                        print("")
                                                        i["modulos"][f"Modulo {modulo}"] = (f"[{resultado}] [{"Modulo desaprobado"}]")
                                                        print("Modulo Desaprobado\n")

                                                else:
                                                    print("La nota supera el límite ")
                                                    print("Ingrese las notas nuevamente")

                                            notamodulo += [i]           
                                            promedio = notas/5
                                            i["promedio"] = promedio

                                            if promedio < 60:
                                                moduloP = {
                                                    
                                                    "Nombre": i["nombres"],
                                                    "Apellido": i["apellidos"],
                                                    "Promedio": i["promedio"]
                                                    }
                                                    #PARA CREAR EN EL JSON LA NUEVA RUTA
                                                riesgo = {
                                                        "Riesgo" : "Riesgo Alto",
                                                        "Notas": [moduloP]#AGREGAR EL MODULO A LA RUTA
                                                    }

                                                notaP += [riesgo]
                                                

                                                with open("promedioNotas.json", "w") as f:
                                                    json.dump(notaP, f, indent=4)

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
                            
                            print("------------------------------------------------")   
                            print("              MÓDULO DE MATRICULAS                ")
                            print("------------------------------------------------\n")   
                            print("")

                            #Asignar ruta a Trainer
                            opc = int(input("¿Qué deseas hacer?\n1.Asignación de Rutas a Trainers\n2.Asignación de trainers y rutas a estudiantes - Asignar fecha de incio y finalización\n\n"))

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
                                    for i in miJSON:
                                        if i["salon"] == "Sputnik":
                                            estudiantes = i["estudiantes"]
                                            break


                                    for x in estudiantes:
                                        print(contador, f"{x["nombres"]} {x["apellidos"]}\n")
                                        contador = contador + 1

                                    estudiante = input("Ingrese el nombre del estudiante\n\n")
                                    print("")
                                    apellido = input("Ingrese el apellido del estudiante\n\n")
                                    print("")

                                    for i in estudiantes:
                                        
                                            if i["nombres"] == estudiante:
                                                if "apellidos" in i and i["apellidos"] == apellido:
                                                    
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

                                    print("Trainers y rutas que puedes asignar:\n")

                                    contador = 1
                                    for i in rutica:
                                        print(contador,f" Trainer: {i["nombre"]} - Ruta: {i["ruta"]}")
                                        contador = contador + 1

                                    print("")
                                    aggtrainer = input("Elige un trainer (cada trainer ya cuenta con una ruta establecida)\n\n")

                                    for i in rutica:
                                        if i["nombre"] == aggtrainer:
                                            asigRuta = i["ruta"]
                                            break


                                    iniFecha = input("Ingrese la fecha de inicio del estudiante (dd/mm/aaaa)\n\n")
                                    print("")
                                    finFecha = input("Ingrese la fecha de finalización del estudiante (dd/mm/aaaa)\n\n")

                                    for i in estudiantes:
                                        
                                            if i["nombres"] == estudiante:
                                                if "apellidos" in i and i["apellidos"] == apellido:
                                                    i["trainer"] = aggtrainer
                                                    i["ruta"] = asigRuta
                                                    i["inicio"] = iniFecha
                                                    i["finalizacion"] = finFecha
                                

                                    with open("academico.json", "w") as openfile:
                                        json.dump(miJSON, openfile, indent=4)

                                if asignar == 2:
                                    system("cls")
                                    print("Estudiantes Apolo")
                                    print("")

                                    contador = 1
                                    for i in miJSON:
                                        if i["salon"] == "Apolo":
                                            estudiantes = i["estudiantes"]
                                            break


                                    for x in estudiantes:
                                        print(contador, f"{x["nombres"]} {x["apellidos"]}\n")
                                        contador = contador + 1

                                    estudiante = input("Ingrese el nombre del estudiante\n\n")
                                    print("")
                                    apellido = input("Ingrese el apellido del estudiante\n\n")
                                    print("")

                                    for i in estudiantes:
                                        
                                            if i["nombres"] == estudiante:
                                                if "apellidos" in i and i["apellidos"] == apellido:
                                                    
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

                                    print("Trainers y rutas que puedes asignar:\n")

                                    contador = 1
                                    for i in rutica:
                                        print(contador,f" Trainer: {i["nombre"]} - Ruta: {i["ruta"]}")
                                        contador = contador + 1

                                    print("")
                                    aggtrainer = input("Elige un trainer (cada trainer ya cuenta con una ruta establecida)\n\n")

                                    for i in rutica:
                                        if i["nombre"] == aggtrainer:
                                            asigRuta = i["ruta"]
                                            break


                                    iniFecha = input("Ingrese la fecha de inicio del estudiante (dd/mm/aaaa)\n\n")
                                    print("")
                                    finFecha = input("Ingrese la fecha de finalización del estudiante (dd/mm/aaaa)\n\n")

                                    for i in estudiantes:
                                        
                                            if i["nombres"] == estudiante:
                                                if "apellidos" in i and i["apellidos"] == apellido:
                                                    i["trainer"] = aggtrainer
                                                    i["ruta"] = asigRuta
                                                    i["inicio"] = iniFecha
                                                    i["finalizacion"] = finFecha
                                

                                    with open("academico.json", "w") as openfile:
                                        json.dump(miJSON, openfile, indent=4)

                                if asignar == 3:
                                    system("cls")
                                    print("Estudiantes Artemis")
                                    print("")

                                    contador = 1
                                    for i in miJSON:
                                        if i["salon"] == "Artemis":
                                            estudiantes = i["estudiantes"]
                                            break


                                    for x in estudiantes:
                                        print(contador, f"{x["nombres"]} {x["apellidos"]}\n")
                                        contador = contador + 1

                                    estudiante = input("Ingrese el nombre del estudiante\n\n")
                                    print("")
                                    apellido = input("Ingrese el apellido del estudiante\n\n")
                                    print("")

                                    for i in estudiantes:
                                        
                                            if i["nombres"] == estudiante:
                                                if "apellidos" in i and i["apellidos"] == apellido:
                                                    
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

                                    print("Trainers y rutas que puedes asignar:\n")

                                    contador = 1
                                    for i in rutica:
                                        print(contador,f" Trainer: {i["nombre"]} - Ruta: {i["ruta"]}")
                                        contador = contador + 1

                                    print("")
                                    aggtrainer = input("Elige un trainer (cada trainer ya cuenta con una ruta establecida)\n\n")

                                    for i in rutica:
                                        if i["nombre"] == aggtrainer:
                                            asigRuta = i["ruta"]
                                            break

                                    iniFecha = input("Ingrese la fecha de inicio del estudiante (dd/mm/aaaa)\n\n")
                                    print("")
                                    finFecha = input("Ingrese la fecha de finalización del estudiante (dd/mm/aaaa)\n\n")


                                    for i in estudiantes:
                                        
                                            if i["nombres"] == estudiante:
                                                if "apellidos" in i and i["apellidos"] == apellido:
                                                    i["trainer"] = aggtrainer
                                                    i["ruta"] = asigRuta
                                                    i["inicio"] = iniFecha
                                                    i["finalizacion"] = finFecha
                                

                                    with open("academico.json", "w") as openfile:
                                        json.dump(miJSON, openfile, indent=4)

                        elif respuestaUsuario==5:
                            
                            print("------------------------------------------------")   
                            print("              MÓDULO DE REPORTES                ")
                            print("------------------------------------------------\n")   
                            print("")
                            modulo = int(input("1. Listar los campers que se encuentren en estado de inscrito\n2. Listar los campers que aprobaron el examen inicial\n3. Listar los entrenadores que se encuentran trabajando con *CampusLands*\n4. Listar los campers que cuentan con bajo rendimiento\n5. Listar los campers y trainers que se encuentren asociados a una ruta de entrenamiento\n6. Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado\n"))    
                            print("")
                            
                            if modulo == 1:
                                

                                pregunta = "si"
                                while pregunta.lower() == "si":
                                    system("cls")
                                    print("------------------------------------------------")   
                                    print("              CAMPERS INSCRITOS                 ")
                                    print("------------------------------------------------\n")   

                                    print("Acontinuación se mostrará los campers que se han inscrito en Campus con el estado actual")
                                    contador = 1

                                    for i in inscritos:

                                        for x in i["inscritos"]:

                                            print(contador, x["nombres"], x["apellidos"])
                                            print(x["estado"])
                                            print("")
                                            contador=contador+1
                                            

                                    pregunta = input("\n¿Desea volver al menú? (si/no)\n")
                                    if pregunta.lower() != "si":
                                        bool = False
                                    break          
                                    
                       
                            if modulo == 2:
                                pregunta = "si"
                                while pregunta.lower() == "si":
                                    system("cls")
                                    
                                    print("------------------------------------------------")   
                                    print("              CAMPERS APROBADOS                 ")
                                    print("------------------------------------------------\n")   

                                    contador=1
                                    for i in aprobado:

                                        print(contador, i["nombres"], i["apellidos"])
                                        print(i["estado"])
                                        print("")
                                        contador=contador+1

                                    pregunta = input("\n¿Desea volver al menú? (si/no)\n")
                                    if pregunta.lower() != "si":
                                        bool = False
                                    break

                            if modulo == 3:

                                pregunta = "si"
                                while pregunta.lower() == "si":
                                    system("cls")

                                    print("------------------------------------------------")   
                                    print("                  TRAINERS                      ")
                                    print("------------------------------------------------\n") 

                                    contador=1
                                    for i in trai:
                                        for x in i["trainer"]:
                                            print(contador, x["nombre"], x["apellidot"])
                                            print("")
                                            contador=contador+1

                                    pregunta = input("\n¿Desea volver al menú? (si/no)\n")
                                    if pregunta.lower() != "si":
                                        bool = False
                                    break

                            if modulo == 4:

                                pregunta = "si"
                                while pregunta.lower() == "si":
                                    system("cls")

                                    print("------------------------------------------------")   
                                    print("         CAMPERS CON BAJO RENDIMIENTO           ")
                                    print("------------------------------------------------\n") 

                                    contador=1
                                    for i in notaP:
                                        for x in i["Notas"]:
                                            
                                            print(contador, x["Nombre"], x["Apellido"])
                                            print("")
                                            contador=contador+1

                                    pregunta = input("\n¿Desea volver al menú? (si/no)\n")
                                    if pregunta.lower() != "si":
                                        bool = False
                                    break
                        
                            if modulo == 5:

                                pregunta = "si"
                                while pregunta.lower() == "si":
                                    system("cls")

                                    print("------------------------------------------------")   
                                    print("  Trainers y estudiantes asociados a una ruta   ")
                                    print("------------------------------------------------\n")

                                    asoc = input("¿Qué ruta desea ver?\n1.Java\n2.NodeJS\n3.NetCore\n4.PHP\n\n")
                                    print("")

                                    for i in miJSON:
                                        for x in i["estudiantes"]:
                                            if "ruta" in x and x["ruta"] == asoc:
                                                print("Camper: ", x["nombres"], x["apellidos"])
                                                print("Trainer: ", x["trainer"])
                                                print("Ruta: ", x["ruta"])
                                                print("")

                                    pregunta = input("\n¿Desea volver al menú? (si/no)\n")
                                    if pregunta.lower() != "si":
                                        bool = False
                                    break

                            if modulo == 6:

                                pregunta = "si"
                                while pregunta.lower() == "si":
                                    system("cls")

                                    contador = {}

                                    for i in notamodulo:
                                        ruta = i["ruta"]
                                        trainer = i["trainer"]

                                    if ruta not in contador:
                                        contador[ruta] = {}
                                    if trainer not in contador[ruta]:
                                        contador[ruta][trainer] = {"Aprobados": 0, "Desaprobados": 0}

                                    for b, resultado in i["modulos"].items():
                                    
                                        if "aprobado" in resultado:
                                            contador[ruta][trainer]["Aprobados"] += 1
                                        
                                        elif "desaprobado" in resultado:
                                            contador[ruta][trainer]["Desaprobados"] += 1

                                            
                                    print(json.dumps(contador, indent=4, ensure_ascii=False)) 

                                    pregunta = input("\n¿Desea volver al menú? (si/no)\n")
                                    if pregunta.lower() != "si":
                                        bool = False
                                    break 

                        elif respuestaUsuario == 6:
                            
                            system("cls")

                            print("------------------------------------------------")   
                            print("                 CERRAR SESION                  ")
                            print("------------------------------------------------\n") 

                            sino=int(input("Desea cerrar sesión? \n1.Si\n2.Salir del programa\n"))

                            if sino == 1:

                                system("cls")
                                print("Cerrando sesión...")
                                time.sleep(3)
                                
                            if sino == 2:
                                system("cls")
                                print("Adios")
                                time.sleep(1)
                                bool = False
                                break

                            

                    else:
                        print("Contraseña incorrecta")
                else:
                    print("ID inválido") 
    
               
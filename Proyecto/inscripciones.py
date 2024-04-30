#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from os import system

Sputnik=[]
si="Aprobado"
no="Desaprobado"

with open('academico.json','r') as openfile:
    miJSON= json.load(openfile)

for i in range (len(miJSON)):
        if (miJSON[i]["salon"]=="Sputnik"):
            Sputnik.append(miJSON[i])

with open('trainer.json','r') as openfile:
    trai= json.load(openfile)
    

with open('coordinador.json','r') as openfile:
    coor= json.load(openfile)

def guardarArchivo(miData):
    with open("academico.json","w") as outfile:
        json.dump(miData,outfile)


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

    for i in coor:
        for x in i["coordinador"]:

            if x["id"] == usuario:

                if "contrasena" in x and x["contrasena"] == Contraseña:
                    print("Ingreso exitoso Coordinador", x["nombre"])
                    print("")

                    respuestaUsuario = int(input("""                          Elije una opción       
                          
                          1. Registrar notas
                          2. Crear nuevas rutas
                          3. Módulo de matrículas
                          4. Consultar campers en alto riesgo
                          5. Módulo de reportes\n"""))
                    
                    if respuestaUsuario == 1:
                        
                        system("cls")

                        print("------------------------------------------------")   
                        print("                INGRESAR NOTAS                  ")
                        print("------------------------------------------------\n")   
                        print("")

                        salon = input("Ingresa el salón: \n1. Sputnik\n2. Apolo\n3. Artemis\n\n")
                        system("cls")
                        
                        print("Estudiantes Sputnik")
                        print("")

                        contador = 1
                        for i in Sputnik:
                            for x in i["estudiantes"]:

                                print(contador, f"{x["nombres"]} {x["apellidos"]}\n")
                                contador = contador + 1

                        estudiante = input("Ingrese el nombre del estudiante que desea revisar\n")
                        print("")
                        apellido = input("Ingrese el apellido del estudiante que desea revisar\n")

                        for i in Sputnik:
                            for x in i["estudiantes"]:
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

                                        bool = True
                                        while bool:
                                            PorcentajeMayor = int(input("Nota práctica 60% :\n"))
                                            PorcentajeMenor = int(input("Nota teórica 30% :\n"))

                                            if 100 >= PorcentajeMayor and PorcentajeMenor >= 1:
                                                resultado = ((PorcentajeMayor * 0.6) + (PorcentajeMenor * 0.30))

                                                if resultado >= 60:
                                                    print(si)
                                                else:
                                                    print(no)

                                                bool = False
                                            else:
                                                print("La nota supera el límite ")
                                                print("Ingrese las notas nuevamente")

                                            # Guarda el promedio en el archivo JSON
                                            # Asumiendo que quieres agregar el promedio a cada elemento de Sputnik
                                            for item in Sputnik:
                                                if resultado>=60:
                                                    item["promedio"] = si
                                                else:
                                                    item["promedio"] = no

                                            
                                            Sputnik["estudiantes"]["promedio"] = resultado
                                            with open("academico.json", 'w') as f:
                                                json.dump(Sputnik,f,indent=4)

                                    else:
                                        print("El apellido no concuerda con el nombre")            
                                else:
                                    print("Nombre no encontrado")
                                                            
                else:
                    print("Contraseña incorrecta")
            else:
                print("ID inválido") 
                                    
                                    

                                

                                

                                
                                        


                                        



#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from os import system

Sputnik=[]

with open('academico.json','r') as openfile:
    miJSON= json.load(openfile)

for i in range (len(miJSON)):
        if (miJSON[i]["salon"]=="Sputnik"):
            Sputnik.append(miJSON[i])
print(Sputnik)

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

                        salon = input("Ingresa el salón: \n1. Sputnik\n2. Apolo\n3. Artemis\n")

                        
                        contador = 0
                        for i in Sputnik:
                            contador = contador + 1
                            for x in i["estudiantes"]:

                                print(contador, x["nombres"]), print(x["apellidos"])
                            

                        estudiante = input("Ingrese el nombre del estudiante que desea revisar\n")
                        apellido = input("Ingrese el apellido del estudiante que desea revisar\n")

                        for i in Sputnik:
                            for x in i["estudiantes"]:
                                if x["nombres"] == estudiante:
                                    if "apellidos" in x and x["apellidos"] == apellido:
                                        print("------------------------------------------------")   
                                        print("     DATOS: ", x["nombres"] and x["apellidos"]   )
                                        print("------------------------------------------------\n")   
                                        print("")
                                    
                                    else:
                                        print("El apellido no concuerda con el nombre")

                                else:
                                    print("Nombre no encontrado")

                            
                            


                    




                else:
                    print("Contraseña incorrecta")
            else:
                print("ID inválido")
        


        



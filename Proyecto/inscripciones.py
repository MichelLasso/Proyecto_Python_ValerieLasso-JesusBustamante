#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from os import system
import jpathpy



with open('academico.json','r') as openfile:
    miJSON= json.load(openfile)



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
    password = input("Password: ")
    print("")

    for i in coor:
        for x in i["coordinador"]:
            if x["id"] == usuario:
                if "contrasena" in x and x["contrasena"] == password:
                    print("Ingreso exitoso Coordinador", x["nombre"])
                    print("")

                    respuesta = input("""                          Elije una opción       
                          
                          1. Registrar notas
                          2. Crear nuevas rutas
                          3. Módulo de matrículas
                          4. Consultar campers en alto riesgo
                          5. Módulo de reportes\n""")
                    
                    




                else:
                    print("Contraseña incorrecta")
            else:
                print("ID inválido")
        


        



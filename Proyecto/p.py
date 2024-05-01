# if respuestaUsuario==5:
                        
#                         print("------------------------------------------------")   
#                         print("              MÓDULO DE REPORTES                ")
#                         print("------------------------------------------------\n")   
#                         print("")
#                         modulo = input(int("""      

#                         1. Listar los campers que se encuentren en estado de inscrito.
#                         2. Listar los campers que aprobaron el examen inicial.
#                         3. Listar los entrenadores que se encuentran trabajando con *CampusLands*.
#                         4. Listar los campers que cuentan con bajo rendimiento.
#                         5. Listar los campers y trainers que se encuentren asociados a una ruta de entrenamiento.
#                         6. Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.
#                         ------------------------------------------------\n"""))
#                         if modulo==1:

#                             system("cls")
                            
#                             print("------------------------------------------------")   
#                             print("              CAMPERS INSCRITOS                 ")
#                             print("------------------------------------------------\n")   

#                             contador = 1

#                             for i in miJSON:

#                                 for x in i["estudiantes"]:

#                                     print(contador, x["nombres"], x["apellidos"])
#                                     contador = contador + 1
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
    notamodulo += [i]

    with open("promedioNotas.json", "w") as f:
        json.dump(notaP, f, indent=4)

    with open("notamodulo.json", 'w') as f:
        json.dump(notamodulo,f, indent=4)


# Supongamos que estos son tus trainers y salones
trainers = ["Trainer1", "Trainer2", "Trainer3", "Trainer4", "Trainer5", "Trainer6"]
salones = ["Salon1", "Salon2", "Salon3"]

# Crea un diccionario para almacenar los horarios de los trainers
horarios = {}

# Asigna cada trainer a un salon
for i in range(len(trainers)):
    salon = salones[i % len(salones)]  # Asigna los salones en orden, repitiendo si es necesario
    if salon not in horarios:
        horarios[salon] = []
    horarios[salon].append({"trainer": trainers[i], "horario": (i % 4 + 1) * 4})

# Imprime los horarios
for salon, trainers in horarios.items():
    print(f"{salon}:")
    for trainer in trainers:
        print(f"  {trainer['trainer']}: {trainer['horario']}-00 a {trainer['horario']+4}-00")
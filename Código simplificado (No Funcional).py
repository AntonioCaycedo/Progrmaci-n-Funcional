#Ahora generamos el mismo proyecto sin tener en cuenta el paradigma funcional

# Lista de proyectos como diccionarios
proyectos = [
    {"Nombre": "Síntesis de alcoholes", "Área": "Química Orgánica", "Presupuesto": 30000, "Activo": True},
    {"Nombre": "Estudio de hidrocarburos", "Área": "Química Orgánica", "Presupuesto": 25000, "Activo": False},
    {"Nombre": "Reacciones de alquenos", "Área": "Química Orgánica", "Presupuesto": 40000, "Activo": True},
    {"Nombre": "Catálisis enzimática", "Área": "Catálisis", "Presupuesto": 35000, "Activo": True},
]

# Actualizar datos directamente, modificando la lista definida anteriormente
for p in proyectos:
    if p["Nombre"] == "Estudio de hidrocarburos":
        p["Presupuesto"] = 30000
    elif p["Nombre"] == "Catálisis enzimática":
        p["Activo"] = False

# Mostrar resultados e imprimirlos
for p in proyectos:
    estado = "Activo" if p["Activo"] else "Inactivo"
    print(f"{p['Nombre']} | {p['Área']} | ${p['Presupuesto']} | {estado}")

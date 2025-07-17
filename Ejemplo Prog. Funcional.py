#Vamos a crear un proyecto de un laboratorio químico, donde documentaremos los proyectos que se llevan a cabo en el mismo


#Definimos una función pura para crear un proyecto asignandolo a un diccionario
def nuevo_proyecto(nombre, area , presupuesto, activo):
  return{
    "Tipo":"Proyecto",
    "Nombre": nombre,
    "Area de estudio": area,
    "Presupuesto": presupuesto,
    "Activo": activo
  }

#Definimos una función pura para ver los proyectos sin modificar ninguna lista o función externa
def ver_proyecto(nombre):
  return f"{nombre['Nombre']} {nombre['Area de estudio']}  {nombre['Presupuesto']} {nombre['Activo']}"


#Definimos un función para actualizar los datos de un proyecto, no obstante, esta no modifica el diccionario creado anteriormente, sino que crea un nuevo diccionario para los elementos actualizados, de modo que cumple con el paradigma funcional
def actualizar_proyecto(proyecto, propiedad, valor):
  return {
    **proyecto, propiedad: valor 
  }


#Creamos una lista con proyectos nuevos como una nueva estructura de datos
proyectos_actuales = [
  nuevo_proyecto("Síntesis de alcoholes", "Química Orgánica", 30000, True),
  nuevo_proyecto("Estudio de hidrocarburos", "Química Orgánica", 25000, False),
  nuevo_proyecto("Reacciones de alquenos", "Química Orgánica", 40000, True),
  nuevo_proyecto("Catálisis enzimática", "Catálisis", 35000, True),
]


#observamos los datos obtenidos, dicha funcion, aunque genera una salida, se considera funcional pues es la única forma de mostrar un resultado
print("\n ----Proyectos----")
for p in proyectos_actuales:
  print(ver_proyecto(p))

#formamos una nueva lista la cual no modifica ninguno de los objetos anteriormente declarados, por lo cual no tiene efectos secundarios
proyectos_actualizados = [
        actualizar_proyecto(p, "Presupuesto", 30000) if p["Nombre"] == "Estudio de hidrocarburos" else actualizar_proyecto(p, "Activo", False) if p["Nombre"] == "Catálisis enzimática" else p for p in proyectos_actuales
    ]

#Finalmente, imprimimos los datos obtenidos para los proyectos actualizados
print("\n ----Proyectos actualizados----")
for p in proyectos_actualizados:
  print(ver_proyecto(p))


from datetime import date
import os
import time

listar_tareas = []

def agregar_tarea():
    descripcion = input("Ingrese el nombre de la tarea: ")

    tarea = {"descripcion": descripcion,
	        "fecha": date.today().strftime("%d/%m/%y"),
            "completada": False}
    
    listar_tareas.append(tarea)
    print(descripcion, "Se agregó a la lista de tareas correctamente.")
  
def listar_tareas():
    print("Lista de tus tareas:")
    lista = 0
    for iterar in listar_tareas:
        print(lista, iterar)
        lista += 1

def eliminar_tareas():
    listar_la_tarea()
    eliminar = int(input("Eliminar la tarea: "))
    listar_tareas.pop(eliminar)
    print("Su tarea fue eliminada de la lista")

def completar_tu_tarea():
    listar_la_tarea()
    completar = int(input("Completar la tarea: "))
    listar_tareas [completar] ["completada"] = True
    print("Su tarea ha sido completada")


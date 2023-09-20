from datetime import date
import time
import os


lista_tareas = []

def agregar_tarea():
    descripcion = input("Ingrese el nombre de la tarea: ")

    tarea = {"descripcion": descripcion,
            "fecha": date.today().strftime("%d/%m/%y"),
            "completada": False}
    
    lista_tareas.append(tarea)
    print(descripcion, "Se agregó a la lista de tareas correctamente.")

def listar_tareas():
    print("Listar tareas:")
    listar = 0
    for ab in lista_tareas:
        print(listar, ab)
        listar += 1

def eliminar_tarea():
    listar_tareas()
    eliminarTarea = int(input("Eliminar tarea: "))
    lista_tareas.pop(eliminarTarea)
    print("La tarea ha sido eliminada correctamente.")

def completar_tarea():
    listar_tareas()
    completar = int(input("Completar tarea: "))
    lista_tareas[completar] ["completada"] = True
    print("La tarea ha sido completada correctamente")

def menu():
    funciones = ["Agregar tarea", "Eliminar tarea", "Listar tareas", "Completar tarea", "Salir",]
    print("Bienvenido al menu de tareas. ", "\n")
    contador = 1
    for opciones in funciones:
        print(contador, opciones)
        contador += 1    
    
def main():
    i=0
    while i==0:
        time.sleep(2)
        os.system("cls")
        menu()
        elegir = int(input("Seleccione una opcion: "))
        if elegir == 1:
            agregar_tarea()
        elif elegir == 2:
            eliminar_tarea()
        elif elegir == 3:
            listar_tareas()
        elif elegir == 4:
            completar_tarea()
        elif elegir == 5:
            print("Saludos!")
            i=2
        else:
            print("Opcion invalida")
        
main()
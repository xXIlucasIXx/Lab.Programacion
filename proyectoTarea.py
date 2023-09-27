import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lista_tareas.insert(tk.END, f"{fecha_hora} - {tarea}")
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Campo vacío", "Por favor ingresa una tarea.")

def eliminar_tarea():
    try:
        seleccion = lista_tareas.curselection()
        lista_tareas.delete(seleccion)
    except:
        messagebox.showwarning("Ninguna tarea seleccionada", "Por favor selecciona una tarea.")

def marcar_completada():
    try:
        seleccion = lista_tareas.curselection()
        lista_tareas.itemconfig(seleccion, {'bg':'#C2F4C2'}) 
    except:
        messagebox.showwarning("Ninguna tarea seleccionada", "Por favor selecciona una tarea.")


ventana = tk.Tk()
ventana.title("Gestor de Tareas")


lista_tareas = tk.Listbox(ventana, selectbackground='#A5F2F3', selectforeground='black', width=50, height=15)
lista_tareas.pack(padx=10, pady=10)


entrada_tarea = tk.Entry(ventana, font=("Arial", 12))
entrada_tarea.pack(pady=5)


boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(side=tk.LEFT, padx=5)
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(side=tk.LEFT, padx=5)
boton_completar = tk.Button(ventana, text="Marcar Completada", command=marcar_completada)
boton_completar.pack(side=tk.LEFT, padx=5)


ventana.mainloop()
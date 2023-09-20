import funciones

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. crear")
    print ("2. eliminar")
    print ("3. completar")
    print ("4. listar")
    print ("5. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        funciones.agregar_tarea()
    elif opcion == 2:
        funciones.eliminar_la_tarea()
    elif opcion == 3:
        funciones.completar_tu_tarea()
    elif opcion == 4:
       funciones.listar_la_tarea()    
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
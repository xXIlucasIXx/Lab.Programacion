def contar_palabras(cadena):
  
    palabras = cadena.split()
    
    return len(palabras)

texto = "El señor de los anillos."
num_palabras = contar_palabras(texto)
print("Contiene", num_palabras, "palabras.")
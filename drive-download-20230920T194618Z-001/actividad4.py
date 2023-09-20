def traduccion(palabra):
    diccionario = {
        'perro': 'dog',
        'gato': 'cat',
        'computadora': 'computer',
        'casa': 'home',
       
    }
    palabra = palabra.lower()

    if palabra in diccionario:
        return diccionario[palabra]
 
      
palabra_espanol = input('Ingresa una palabra en español: ')
traduccion = traduccion(palabra_espanol)
print('La traducción es:', traduccion)

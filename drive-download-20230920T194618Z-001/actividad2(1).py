alumno1 = {
    'nombre': 'Lucas',
    'edad': 15,
    'apellido': 'Coman'
}

alumno2 = {
    'nacimiento':'22/12/2007',
    'pais': 'argentina',
    'telefono': '1126427345'
}


alumno = alumno1.copy()
alumno.update(alumno2)


print(alumno)


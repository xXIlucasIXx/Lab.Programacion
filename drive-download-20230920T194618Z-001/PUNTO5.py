def validar_contrasnia(password):
    largo = len(password)
    if largo < 8:
     return False 
     mayus = 0
     minus = 0 
     digit = 0
    for letra in password:
        if letra.isdigit():
         digit += 1
        if letra.islower():
            minus += 1
        if letra.isupper():
            mayus += 1
    if mayus and minus and digit:
     return True, False
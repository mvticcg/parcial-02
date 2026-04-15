"""
duoc ha contratado sus servicios para realizar un login en python, el login debe validar usuario y clave.

USUARIO CORRECTO: alumno
CONTRASEÑA CORRECTA: duocuc2026
"""

usuario = input("Ingrese el usuario: ")
if usuario == ("alumno"):
    print ("USUARIO CORRECTO")

    password = input("Ingrese la contraseña: ")

    if password == ("duocuc2026"):
        print ("CONTRASEÑA CORRECTA")
    else: 
        print("CONRASEÑA INCORRECTA")
else:  
    print("INGRESA EL USUARIO CORRECTO")







user = "Matias"
password = "beateamo0607"
intentos = 0

while intentos < 5:
    user_input = input("Ingrese su usuario: ")
    password_input = input("Ingrese su contraseña: ")

    if user_input == user and password_input == password:
        print(f"Bienvenido a Banco Estado, {user_input}")
        break
    else:
        intentos += 1
        print(f"Acesso incorrecto. Intento {intentos} de 5.")
        if intentos == 5:
            print("Ha superado el número de intentos permitidos jejejje.")
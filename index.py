# try

try: 
    resultado = float
    num1 = float(input("Por favor, mete un numero: "))
    num2 = float(input("Por favor, mete un numero: "))

    resultado = num1 / num2 

    print(f" el resultado de esta division es: {resultado}")
    if num2 == 0:

        raise ZeroDivisionError # Lanza el error o provoca el error el error manual

  

except ValueError:
    print(" ERROR MANO, INGERsa unnuevo numero")

except ZeroDivisionError:
    print("error, no se puede dividir por cero")    


